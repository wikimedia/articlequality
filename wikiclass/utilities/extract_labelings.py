"""
``$ wikclass extract_labelings -h``
::

    Extracts labels from an XML dump and writes out labeled observations for
    each change in assessment class.  Will match extraction method to the dump.

    Usage:
        extract_labelings <dump-file>... [--extractor=<name>] [--threads=<num>]
                                         [--output=<path>] [--verbose]
        extract_labelings -h | --help

    Options:
        -h --help           Show this screen.
        <dump-file>         An XML dump file to process
        --extractor=<name>  The dbname of the wiki extractor to use (e.g. 'enwiki')
                            [default: <match>]
        --threads=<num>     If a collection of files are provided, how many
                            processor threads should be prepare?
                            [default: <cpu_count>]
        --output=<path>     The path to a file to dump observations to
                            [default: <stdout>]
        --verbose           Prints dots to <stderr>
"""
import json
import logging
import os.path
import sys
from importlib import import_module
from multiprocessing import cpu_count

import docopt
import mwxml


def main(argv=None):
    args = docopt.docopt(__doc__, argv=argv)

    dump_paths = args['<dump-file>']

    if args['--extractor'] == "<match>":
        extractor = None
    else:
        extractor = load_extractor(args['--extractor'])

    if args['--threads'] == "<cpu_count>":
        threads = cpu_count()
    else:
        threads = int(args['--threads'])

    if args['--output'] == "<stdout>":
        output = sys.stdout
    else:
        output = open(os.path.expanduser(args['--output']), "w")

    verbose = args['--verbose']

    run(dump_paths, threads, output, verbose=verbose, extractor=extractor)

def load_extractor(extractor_name):
    try:
        return import_module("wikiclass.extractors." + extractor_name)
    except ImportError:
        raise RuntimeError("Could not load extractor for '{0}'"
                           .format(extractor_name))

def run(dump_paths, threads, output, verbose=False, extractor=None):
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.WARNING,
        format='%(asctime)s %(levelname)s:%(name)s -- %(message)s'
    )


    if len(dump_paths) == 0:
        label_events = dump2labels(mwxml.Dump.from_file(sys.stdin),
                                   extractor, verbose=verbose)

    else:
        label_events = mwxml.map(lambda d, p: \
                                    dump2labels(d, extractor, verbose),
                                 dump_paths,threads=threads)

    for labeling in label_events:

        json.dump(labeling, output)
        output.write("\n")

def extract_labelings(dump, extractor=None, verbose=False):
    """
    Extracts labeling events from :class:`mwxml.Dump`.

    :Parameters:
        dump : :class:`mwxml.Dump`
            The XML dump file to extract labelings from
        extractor : :class:`wikiclass.Extractor`
            An extractor to apply to the XML dump.  If no extractor is
            provided, an extract will be looked up based on <dbname> in the XML
            dump's <siteinfo> block.
        verbose : `bool`
            Print dots and stuff to stderr

    :Returns:
        An iterator of dicts containing:

        * page_title -- The normalized title of the article
        * project -- A project (often a WikiProject) associated with the label
        * timestamp -- The timestamp the labeling was observed
        * label -- The quality label that was extracted
    """

    if extractor is None:
        extractor = load_extractor(dump.site_info.dbname)

    for page in dump:

        if verbose:
            sys.stderr.write("\n{0}: ".format(page.title))
            sys.stderr.flush()

        for obs in extractor.extract(page, verbose=verbose):
            yield {'page_title': normalize_title(page.title, page.namespace),
                   'project': obs['project'],
                   'timestamp': obs['timestamp'].short_format(),
                   'label': obs['label']}

def normalize_title(title, namespace):
    if namespace > 0:
        title_parts = title.split(":", 1)
        if len(title_parts) == 2:
            title = title_parts[1]

    return title.split("/", 1)[0]
