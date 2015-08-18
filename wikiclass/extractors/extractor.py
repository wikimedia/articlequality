import sys

import mwparserfromhell as mwp
from mw.lib import reverts


class Extractor:

    def __init__(self, name, namespaces):
        self.name = str(name)
        self.namespaces = set(namespaces)


    def extract(self, page, verbose=False):
        """
        Processes an :class:`mw.xml_dump.Page` and returns a generator of
        first-observations of a project/label pair.

        :Parameters:
            page : :class:`mw.xml_dump.Page`
                Page to process
            verbose : print dots to stderr

        """
        if page.namespace not in self.namespaces:
            pass
        else:
            labelings = {}
            last_labels = set()
            detector = reverts.Detector()

            # Process all of the revisions looking for new class labels
            for revision in page:

                revert = detector.process(revision.sha1, revision.id)

                project_labels = set(pl for pl in
                                     self.extract_labels(revision.text))

                if revert is not None:
                    # This revision is a revert.
                    for rev_id in revert.reverteds:
                        if rev_id in labelings:
                            for lab in labelings[rev_id]:
                                lab['reverted'] = True

                    if revert.reverted_to in labelings:
                        for lab in labelings[revert.reverted_to]:
                            lab['reverted'] = False

                    if verbose:
                        sys.stderr.write("r")
                else:
                    # This revision is not a revert.  Get the new labels
                    new_labels = project_labels - last_labels

                    # Log some verbose stuff
                    if verbose and len(new_labels) > 0:
                        sys.stderr.write("l")
                    else:
                        sys.stderr.write(".")

                    # Update lookup of rev_ids that affect labelings
                    if len(new_labels) > 0:
                        labelings[revision.id] = [
                            {'rev_id': revision.id,
                             'project': project, 'label': label,
                             'timestamp': revision.timestamp,
                             'reverted': False}
                             for project, label in new_labels
                        ]

                # Update state so we make an appropriate comparison next time
                last_labels = project_labels

            # Find first labelings and filter out reverted labelings
            first_observations = {}
            for observations in labelings.values():
                for ob in observations:
                    if ob['reverted']: continue
                    pair = (ob['project'], ob['label'])
                    if pair in first_observations:
                        if ob['timestamp'] < first_observations[pair]['timestamp']:
                            first_observations[pair] = ob
                    else:
                        first_observations[pair] = ob

            # All cleaned up.  Yield what we've got.
            for ob in first_observations.values():
                yield ob

    def extract_labels(self, text):
        raise NotImplementedError()


class TemplateExtractor(Extractor):

    def __init__(self, name, namespaces, from_template):
        self.from_template = from_template

        super().__init__(name, namespaces)

    def extract_labels(self, text):

        parsed_text = mwp.parse(text)
        templates = parsed_text.filter_templates()
        assessments = []
        for template in templates:

            project_label = self.from_template(template)

            if project_label is not None:
                yield project_label
