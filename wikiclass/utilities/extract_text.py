"""
``$ wikclass extract_text -h``
::

    Extracts text & metadata for labelings using XML dumps.

    Usage:
        extract_text <dump-file>... [--labelings=<path>] [--output=<path>]
                                    [--threads=<num>] [--verbose]
        extract_text -h | --help

    Options:
        -h --help           Show this screen.
        <dump-file>         An XML dump file to process
        --labelings=<name>  The path to a file containing labeling events.
                            [default: <stdin>]
        --output=<path>     The path to a file to dump observations to
                            [default: <stdout>]
        --threads=<num>     If a collection of files are provided, how many
                            processor threads should be prepare?
                            [default: <cpu_count>]
        --verbose           Prints dots to <stderr>
"""
import json
import logging
import os.path
import re
import sys
from itertools import groupby
from multiprocessing import cpu_count

import docopt
import mwtypes
import mwxml


def main(argv=None):
    args = docopt.docopt(__doc__, argv=argv)

    dump_paths = args['<dump-file>']

    if args['--labelings'] == "<stdin>":
        labelings = (json.loads(line) for line in sys.stdin)
    else:
        path = os.path.expanduser(args['--labelings'])
        labelings = (json.loads(line) for line in open(path))
    grouped_labelings = groupby(labelings, key=lambda l: l['page_title'])
    page_labelings = {title: sorted(list(labs), key=lambda l: l['timestamp'])
                      for title, labs in grouped_labelings}

    if args['--threads'] == "<cpu_count>":
        threads = cpu_count()
    else:
        threads = int(args['--threads'])

    if args['--output'] == "<stdout>":
        output = sys.stdout
    else:
        output = open(os.path.expanduser(args['--output']), "w")

    verbose = args['--verbose']

    run(dump_paths, page_labelings, output, threads, verbose=verbose)


def run(dump_paths, page_labelings, output, threads, verbose=False):
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.WARNING,
        format='%(asctime)s %(levelname)s:%(name)s -- %(message)s'
    )


    if len(dump_paths) == 0:
        labelings = extract_text(mwxml.Dump.from_file(sys.stdin),
                                 page_labelings, verbose=verbose)

    else:
        labelings = mwxml.map(lambda d, p: \
                                    extract_text(d, page_labelings, verbose),
                              dump_paths, threads=threads)

    for labeling in labelings:
        json.dump(labeling, output)
        output.write("\n")


def extract_text(dump, page_labelings, verbose=False):
    """
    Extracts article text and metadata for labelings from an XML dump.

    :Parameters:
        dump : :class:`mwxml.Dump`
            The XML dump file to extract text & metadata from
        labelings : `iterable`(`dict`)
            A collection of labeling events to add text to
        verbose : `bool`
            Print dots and stuff

    :Returns:
        An `iterator` of labelings augmented with 'page_id', 'rev_id' and
        'text'.  Note that labelings of articles that can't be looked up will
        not be included.
    """
    for page in dump:

        if page.namespace == 0 and page.title in page_labelings:
            if verbose:
                sys.stderr.write("\n{0}: ".format(page.title))
                sys.stderr.flush()

            labelings = page_labelings[page.title]

            last_revision = None
            for revision in page:
                while last_revision is not None and \
                      len(labelings) > 0 and \
                      revision.timestamp > mwtypes.Timestamp(labelings[0]['timestamp']):
                    labeling = labelings.pop()
                    labeling['page_id'] = page.id
                    labeling['rev_id'] = last_revision.id
                    if not_an_article(last_revision.text):
                        labeling['text'] = None
                    else:
                        labeling['text'] = last_revision.text

                    yield labeling

                    if verbose:
                        sys.stderr.write("t")
                        sys.stderr.flush()

                # Don't update last_revision if the text was deleted
                if revision.text is not None:
                    last_revision = revision


REDIRECT_RE = re.compile("#redirect", re.I)


def not_an_article(text):
    return (text is None or
            len(text) < 50 or
            REDIRECT_RE.match(text))
