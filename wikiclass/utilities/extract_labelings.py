"""
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
from mw import xml_dump


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

    verbose = args['--output']

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
        label_events = dump2labels(xml_dump.Iterator.from_file(sys.stdin),
                                   extractor, verbose=verbose)

    else:
        label_events = xml_dump.map(dump_paths,
                                    lambda d, p: \
                                        dump2labels(d, extractor, verbose),
                                    threads=threads)

    for page_title, project, label, timestamp in label_events:
        ob = {'page_title': page_title, 'project': project,
              'timestamp': timestamp.short_format(), 'label': label}

        json.dump(ob, output)
        output.write("\n")

def dump2labels(dump, extractor=None, verbose=False):

    if extractor is None:
        extractor = load_extractor(dump.dbname)

    for page in dump:

        if verbose:
            sys.stderr.write("\n{0}: ".format(page.title))
            sys.stderr.flush()

        for obs in extractor.extract(page, verbose=verbose):
            yield normalize_title(page.title, page.namespace), obs['project'], \
                  obs['label'], obs['timestamp']

def normalize_title(title, namespace):
    if namespace > 0:
        return title.split(":", 1)[1]
    else:
        return title
