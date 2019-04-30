"""
``$ articlequality fetch_text -h``
::

    Fetches text & metadata for labelings using a MediaWiki API.

    Usage:
        fetch_text --api-host=<url> [--labelings=<path>] [--output=<path>]
                                    [--verbose]

    Options:
        -h --help           Show this documentation.
        --api-host=<url>    The hostname of a MediaWiki e.g.
                            "https://en.wikipedia.org"
        --labelings=<path>  Path to a containting observations with extracted
                            labels. [default: <stdin>]
        --output=<path>     Path to a file to write new observations
                            (with text) out to. [default: <stdout>]
        --verbose           Prints dots and stuff to stderr
"""
import sys

import mwapi
from docopt import docopt
from revscoring.utilities.util import dump_observation, read_observations

from .extract_text import not_an_article


def main(argv=None):
    args = docopt(__doc__, argv=argv)

    if args['--labelings'] == '<stdin>':
        labelings = read_observations(sys.stdin)
    else:
        labelings = read_observations(open(args['--labelings']))

    if args['--output'] == '<stdout>':
        output = sys.stdout
    else:
        output = open(args['--output'])

    session = mwapi.Session(args['--api-host'],
                            user_agent="ArticleQaulity fetch_text utility.")

    verbose = args['--verbose']

    run(labelings, output, session, verbose)


def run(labelings, output, session, verbose):

    for labeling in fetch_text(session, labelings, verbose=verbose):
        if labeling['text'] is not None:
            dump_observation(labeling, output)


def fetch_text(session, labelings, verbose=False):
    """
    Fetches article text and metadata for labelings from a MediaWiki API.

    :Parameters:
        session : :class:`mwapi.Session`
            An API session to use for querying
        labelings : `iterable`(`dict`)
            A collection of labeling events to add text to
        verbose : `bool`
            Print dots and stuff

    :Returns:
        An `iterator` of labelings augmented with 'page_id', 'rev_id' and
        'text'.  Note that labelings of articles that aren't found will not be
        included.
    """

    for labeling in labelings:
        rev_doc = get_last_rev_before(session, labeling['page_title'],
                                      labeling['timestamp'])

        if rev_doc is None:
            if verbose:
                sys.stderr.write("?")
                sys.stderr.write(
                    labeling['page_title'] + " " + labeling['timestamp'])
                sys.stderr.flush()
        else:
            if verbose:
                sys.stderr.write(".")
                sys.stderr.flush()

            labeling['page_id'] = rev_doc['page'].get("pageid")
            labeling['rev_id'] = rev_doc.get("revid")
            text = rev_doc['slots']["main"].get("content")
            if not_an_article(text):
                labeling['text'] = None
            else:
                labeling['text'] = text

            yield labeling

    if verbose:
        sys.stderr.write("\n")
        sys.stderr.flush()


def get_last_rev_before(session, page_title, timestamp):
    doc = session.get(action="query", prop="revisions", titles=page_title,
                      rvstart=timestamp, rvlimit=1, rvdir="older",
                      rvprop=["ids", "content"], rvslots=["main"],
                      redirects=True, formatversion=2)

    try:
        page_doc = doc['query']['pages'][0]
    except (KeyError, IndexError):
        # No pages found
        return None

    try:
        rev_doc = page_doc['revisions'][0]
        rev_doc['page'] = {k: v for k, v in page_doc.items()
                           if k != "revisions"}
    except (KeyError, IndexError):
        # No revisions matched
        return None

    return rev_doc
