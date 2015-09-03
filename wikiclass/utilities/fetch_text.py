"""
Reads a list of observations with 'page_title', 'timestamp' and 'label' fields
and adds a 'text' field.

Usage:
    fetch_text --api=<url> [--observations=<path>] [--output=<path>] [--verbose]
    fetch_text -h | --help

Options:
    -h --help                Show this documentation.
    --api=<url>              The url of a MediaWiki API e.g.
                             "https://en.wikipedia.org/w/api.php"
    --observations=<path>    Path to a containting observations with extracted
                             labels. [default: <stdin>]
    --output=<path>          Path to a file to write new observations
                             (with text) out to. [default: <stdout>]
    --verbose                Prints dots to <stderr>
"""
import json
import sys
import traceback

from docopt import docopt
from mw import api
from mw.api.errors import APIError


def main(argv=None):
    args = docopt(__doc__, argv=argv)

    if args['--observations'] == '<stdin>':
        observations = (json.loads(line) for line in sys.stdin)
    else:
        observations = (json.loads(line) for line in open(args['--observations']))

    if args['--output'] == '<stdout>':
        output = sys.stdout
    else:
        output = open(args['--output'])

    session = api.Session(args['--api'])

    verbose = args['--verbose']

    run(observations, output, session, verbose)

def run(observations, output, session, verbose):

    for ob in observations:

        doc = None
        try:
            doc = get_last_text_before(session, ob['page_title'],
                                       ob['timestamp'])
        except Exception:
            sys.stderr.write(traceback.format_exc() + "\n")

        if doc is None:
            if verbose: sys.stderr.write("?");sys.stderr.flush()
        else:
            ob['page_id'] = doc['page'].get("pageid")
            ob['rev_id'] = doc.get("revid")
            ob['text'] = doc.get("*", "")
            json.dump(ob, output)
            output.write("\n")
            if verbose: sys.stderr.write(".");sys.stderr.flush()

    if verbose: sys.stderr.write("\n");sys.stderr.flush()

def get_last_text_before(session, page_title, timestamp):
    docs = session.revisions.query(titles=[page_title], start=timestamp,
                                   limit=1, direction="older",
                                   properties=["ids", "content"])
    docs = list(docs)
    if len(docs) == 0:
        return None
    else:
        return docs[0]
