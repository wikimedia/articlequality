"""
Extracts labels from an XML dump and writes out labeled observations for
each change in assessment class.  Will match extraction method to the dump

Usage:
    extract_labelings <dump-file>... [--extractor=<name>] [--theads=<num>]
                                     [--output=<path>]
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
    --verbose    Prints dots to <stderr>
"""
import json
import os.path
import sys

import docopt


def main(argv=None):
    args = docopt(__doc__, argv=argv)

    dump_paths = args['<dump-file>']

    if args['--extractor'] == "<match>":
        extractor = None
    else:
        from .. import extractors
        if hasattr(extractors, args['--extractor']):
            extractor = getattr(extractors, args['--extractor'])
        else:
            raise RuntimeError("No extractor available for '{0}'"
                               .format(args['--extractor']))

    if args['--threads'] == "<cpu_count>":
        threads = cpu_count()
    else:
        threads = int(args['--threads'])

    if args['--output'] == "<stdout>":
        output = sys.stdout
    else:
        output = open(os.path.expanduser(args['--output']), "w")

    run(dump_paths, threads, verbose, output, extractor=extractor)

def run(dump_paths, threads, verbose, output, extractor=None):
    if len(dump_paths) == 0:
        label_events = dump2labels(xml_dump.Iterator.from_file(sys.stdin),
                                   extractor, verbose=verbose)

    else:
        label_events = xml_dump.map(dump_paths,
                                    lambda d, p: \
                                        dump2labels(d, extractor, verbose),
                                    threads=threads)

    for page_title, project, timestamp, label in label_events:
        ob = {'page_title': page_title, 'project': project
              'timestamp': timestamp, 'label': label}

        json.dump(ob, output)
        output.write("\n")

def dump2labels(dump, extractor=None, verbose=False):

    if extract is None:
        wiki = dump.dbname
        from .. import extractors
        if hasattr(extractors, wiki):
            extractor = getattr(extractors, wiki)
        else:
            raise RuntimeError("No extractor available for '{0}'".format(wiki))

    for page in dump:

        if verbose:
            sys.stderr.write("{0}: ".format(page.title))

        for proj, label, ts, count in extractor.extract(page, verbose=verbose)
            yield page.title, proj, label, ts, count
