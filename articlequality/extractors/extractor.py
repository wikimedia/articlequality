"""
.. autoclass:: articlequality.Extractor
    :members:

.. autoclass:: articlequality.TemplateExtractor
    :members:
    :inherited-members:
"""

import logging
import sys
import traceback
from collections import OrderedDict

import mwparserfromhell as mwp
import mwreverts

logger = logging.getLogger(__name__)


class Extractor:
    """
    Implements an labeling event extraction strategy.

    :Parameters:
        name : `str`
            A name for the extraction strategy
        doc : `str`
            Documentation describing the extraction strategy
        namespace : `iterable`(`int`)
            A set of namespaces that will be considered when performing an
            extraction
    """
    def __init__(self, name, doc, namespaces):
        self.__name__ = str(name)
        self.__doc__ = str(doc)
        self.namespaces = set(namespaces)

    def extract(self, page, verbose=False):
        """
        Processes an :class:`mwxml.Page` and returns a generator of
        first-observations of a project/label pair.

        :Parameters:
            page : :class:`mwxml.Page`
                Page to process
            verbose : `bool`
                print dots to stderr

        """
        if page.namespace not in self.namespaces:
            pass
        else:
            if verbose:
                sys.stderr.write("\n{0}: ".format(page.title))
                sys.stderr.flush()

            revisions = OrderedDict()
            detector = mwreverts.Detector()

            # Process all of the revisions looking for reverts
            for revision in page:

                revert = detector.process(revision.sha1, revision.id)
                try:
                    revision_text = revision.text or ""
                    project_labels = set(pl for pl in
                                         self.extract_labels(revision_text))
                except Exception:
                    logger.warning("Could not extract labels from text:")
                    logger.warning(traceback.format_exc())
                    continue

                revisions[revision.id] = {
                    'id': revision.id,
                    'timestamp': revision.timestamp,
                    'was_reverted': False,
                    'is_a_revert': revert is not None,
                    'reverted': revert.reverteds if revert is not None else [],
                    'project_labels': project_labels
                }

                if revert is not None:
                    # This revision is a revert.
                    self.invert_reverted_status(
                        revisions[revision.id]['reverted'],
                        revisions)

            # Re-process revisions only considering those that were not
            # reverted
            last_labels = set()
            for rev_id, revision in revisions.items():
                if revision['was_reverted']:
                    if verbose:
                        sys.stderr.write("r")
                        sys.stderr.flush()
                    continue

                # Get the new labels
                new_labels = revision['project_labels'] - last_labels
                last_labels = revision['project_labels']

                # Log some verbose stuff
                if verbose:
                    if len(new_labels) > 0:
                        sys.stderr.write("l")
                    else:
                        sys.stderr.write(".")
                    sys.stderr.flush()

                for project, label in new_labels:
                    yield {'rev_id': revision['id'],
                           'timestamp': revision['timestamp'],
                           'project': project,
                           'wp10': label}

    def invert_reverted_status(self, reverteds, revisions):
        """
        This method recursively searches the reverted status of revisions and
        inverts the status when reverts are themselves reverted.
        """
        for rev_id in reverteds:
            revisions[rev_id]['was_reverted'] = \
                not revisions[rev_id]['was_reverted']
            if revisions[rev_id]['is_a_revert']:
                self.invert_reverted_status(revisions[rev_id]['reverted'],
                                            revisions)

    def extract_labels(self, text):
        raise NotImplementedError()


class TemplateExtractor(Extractor):
    """
    Implements a template-based extraction strategy based on a `from_template`
    function that takes a template and returns a (project, label) pair.

    :Parameters:
        from_template : `func`
            A function that takes a template and returns a (project, label)
            pair
    """
    def __init__(self, *args, from_template, **kwargs):
        self.from_template = from_template

        if 'filter_text' in kwargs:
            self.filter_text = kwargs.get('filter_text')
            kwargs.pop('filter_text', None)

        super().__init__(*args, **kwargs)

    def extract_labels(self, text):
        """
        Extracts a set of labels for a version of text by parsing templates.

        :Parameters:
            text : `str`
                Wikitext markup to extract labels from

        :Returns:
            An iterator over (project, label) pairs
        """
        # filter_text is an initial fast pass to weed out wikitext that
        # can't contain the template (eg. because the template name
        # never appears)
        if hasattr(self, 'filter_text'):
            if not self.filter_text(text):
                return

        parsed_text = mwp.parse(text)
        templates = parsed_text.filter_templates()
        for template in templates:

            yield from self.from_template(template)
