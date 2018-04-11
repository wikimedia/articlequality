"""
``$ articlequality fetch_item_info -h``
::

    Annotates wikibase items with additional information

    Usage:
        fetch_item_info --api-host=<url>
                        [--claim=<property>]...
                        [--input=<path>] [--output=<path>]
                        [--debug] [--verbose]

    Options:
        -h --help           Show this documentation.
        --host=<url>        The hostname of a Wikibase (MediaWiki) e.g.
                            "https://wikidata.org"
        --claim=<property>  Get the value for a claim based on it's property
        --input=<path>      Path to a file contining observations
                            labels. [default: <stdin>]
        --output=<path>     Path to a file to write new observations
                            (with text) out to. [default: <stdout>]
        --verbose           Prints dots and stuff to stderr
"""
import json
import logging
import sys
import traceback
from concurrent.futures import ThreadPoolExecutor
from itertools import islice

import mwapi
import mwbase
from docopt import docopt
from revscoring.utilities.util import dump_observation, read_observations

logger = logging.getLogger(__name__)


def main(argv=None):
    args = docopt(__doc__, argv=argv)

    logging.basicConfig(
        level=logging.INFO if not args['--debug'] else logging.DEBUG,
        format='%(asctime)s %(levelname)s:%(name)s -- %(message)s'
    )

    if args['--input'] == '<stdin>':
        observations = read_observations(sys.stdin)
    else:
        observations = read_observations(open(args['--input']))

    if args['--output'] == '<stdout>':
        output = sys.stdout
    else:
        output = open(args['--output'])

    claims = args['--claim']

    session = mwapi.Session(args['--api-host'],
                            user_agent="ArticleQuality fetch_text utility.")

    verbose = args['--verbose']

    run(session, observations, claims, output, verbose)


def run(session, observations, claims, output, verbose):

    for ob in fetch_item_info(session, observations, claims, verbose=verbose):
        dump_observation(ob, output)


def fetch_item_info(session, observations, claims, verbose=False):
    """
    Fetches information about wikidata items.

    :Parameters:
        session : :class:`mwapi.Session`
            An API session to use for querying
        observations : `iterable`(`dict`)
            A collection of observations to annotate
        claims : `list` ( `str` )
            A set of property names to look up claims for
        verbose : `bool`
            Print dots and stuff

    :Returns:
        An `iterator` of observations augmented with an `autolabel` field
        containing the requested information.  Note that observations that
        can't be found will be excluded.
    """
    batches = chunkify(observations, 25)

    executor = ThreadPoolExecutor(max_workers=4)
    _fetch_item_info = build_fetch_item_info(session, claims)

    for annotated_batch in executor.map(_fetch_item_info, batches):
        for annotated_item in annotated_batch:
            yield annotated_item
            if verbose:
                sys.stderr.write(".")
                sys.stderr.flush()

    if verbose:
        sys.stderr.write("\n")


def build_fetch_item_info(session, claims):

    def _fetch_item_info(observations):
        doc = session.get(
            action='query', prop='revisions', rvprop=['ids', 'content'],
            formatversion=2, revids=[ob['rev_id'] for ob in observations])

        rev_doc_map = {}
        for page_doc in doc['query']['pages']:
            for rev_doc in page_doc.get('revisions', []):
                rev_doc_map[rev_doc['revid']] = rev_doc

        annotated_observations = []
        for ob in observations:
            if ob['rev_id'] not in rev_doc_map:
                logger.warn("Could not find information for {0}".format(ob))
            else:
                rev_doc = rev_doc_map[ob['rev_id']]
                try:
                    item = mwbase.Entity.from_json(
                        json.loads(rev_doc['content']))
                    ob['claims'] = {}
                    for pid in claims:
                        if pid in item.claims:
                            datavalue = \
                                item.claims[pid][0]['statement']['datavalue']
                            if isinstance(datavalue, mwbase.Time):
                                value = datavalue['calendarmodel']
                            elif isinstance(datavalue, mwbase.EntityId):
                                value = datavalue['id']
                            elif isinstance(datavalue, mwbase.Coordinate):
                                value = datavalue['globe']
                            elif isinstance(datavalue, mwbase.Quantity):
                                value = datavalue['unit']
                            elif isinstance(datavalue, mwbase.String):
                                value = datavalue['value']
                            else:
                                logger.warning(
                                    "Can't handle datavalue of type {0}"
                                    .format(type(datavalue)))
                        else:
                            value = None

                    ob['claims'][pid] = value
                    annotated_observations.append(ob)
                except Exception as e:
                    logger.error("Could not process {0}".format(ob))
                    logger.error(traceback.format_exc())
        return annotated_observations
    return _fetch_item_info


def chunkify(iterable, size):
    while True:
        output = tuple(islice(iterable, size))
        if output:
            yield output
        else:
            break
