"""
Reads a list of observations with 'page_title', 'timestamp' and 'label' fields
and adds a 'text' field.

Usage:
    fetch_text --api=<url>
    fetch_text -h | --help

Options:
    -h --help                Show this documentation.
    --api=<url>              The url of a MediaWiki API e.g.
                             "https://en.wikipedia.org/w/api.php"
    --observations=<path>    Path to a containting observations with extracted
                             labels.
    --output=<path>          Path to a file to write new observations
                             (with text) out to.
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

    obs = (json.loads(line) for line in sys.stdin)

    session = api.Session(args['--api'])

    run(obs, session)

def run(obs, session):

    for ob in obs:

        doc = None
        try:
            doc = get_last_text_before(session, ob['page_title'],
                                       ob['timestamp'])
        except Exception:
            sys.stderr.write(traceback.format_exc() + "\n")

        if doc is None:
            if verbose: sys.stderr.write("?")
        else:
            ob['text'] = doc.get("*", "")
            json.dump(ob, sys.stdout)
            sys.stdout.write("\n")
            if verbose: sys.stderr.write(".")

    if verbose: sys.stderr.write("\n")

def get_last_text_before(session, page_title, namespace=0, timestamp):
    docs = session.revisions.query(titles=[page_title], before=timestamp,
                                   limit=1, directions="older")
    docs = list(docs)
    if len(docs) == 0:
        return None
    else:
        return docs[0]
