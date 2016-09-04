
r"""
Gathers the scores for a set of revisions and
prints a TSV to stdout of the format:
<page_id>\t<title>\n<rev_id>\t<prediction>\t<weighted_sum>

See https://phabricator.wikimedia.org/T135684 for more information.

Usage:
    extract_scores -h | --help
    extract_scores --dump=<dump-file>... --model=<model-file>
                                    [--verbose]
                                    [--rev-scores=<path>]

Options:
    -h --help                   Prints out this documentation.
    --dump=<dump-file>          Path to dump file.
    --model=<model-file>        Path to the model file.
    --verbose                   Prints dots and stuff to stderr
    --rev-scores=<path>         The location to write output to.
                                [default: <stdout>]
"""
from revscoring import ScorerModel
from revscoring.datasources import revision_oriented
from revscoring.dependencies import solve
import logging
import sys

import docopt
import mwxml

import mysqltsv

logger = logging.getLogger(__name__)
r_text = revision_oriented.revision.text

CLASS_WEIGHTS = {
    'Stub': 0,
    'Start': 1,
    'C': 2,
    'B': 3,
    'GA': 4,
    'FA': 5
}

def main(argv=None):
    args = docopt.docopt(__doc__, argv=argv)

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(levelname)s:%(name)s -- %(message)s'
    )

    dumps = args['--dump']
    with open(args['--model']) as f:
        model = ScorerModel.load(f)

    headers=["page_id", "title", "rev_id", "prediction", "weighted_sum"]
    if args['--rev-scores'] == "<stdout>":
        rev_scores = mysqltsv.Writer(sys.stdout, headers=headers)
    else:
        rev_scores = mysqltsv.Writer(open(args['--rev-scores'], "w"),
                                     headers=headers)

    verbose = args['--verbose']
    run(dumps, model, rev_scores, verbose=verbose)


def run(paths, model, rev_scores, verbose=False):

    def process_dump(dump, path):
        for page in dump:
            if int(page.namespace) != 0 or page.redirect:
                continue
            for revision in page:
                feature_values = list(solve(model.features,
                                       cache={r_text: revision.text}))
                yield (revision.id, model.score(feature_values), page.title, page.id)

    for rev_id, score, title, page_id in mwxml.map(process_dump, paths):
        weighted_sum = sum(CLASS_WEIGHTS[cls] * score['probability'][cls]
                           for cls in score['probability'])
        rev_scores.write(
            [page_id,
            title,
            rev_id,
            CLASS_WEIGHTS[score['prediction']],
            weighted_sum]
        )
        if verbose:
            sys.stderr.write(str(CLASS_WEIGHTS[score['prediction']]))
            sys.stderr.flush()

    if verbose:
        sys.stderr.write("\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.stderr.write("\n^C Caught.  Exiting...")

