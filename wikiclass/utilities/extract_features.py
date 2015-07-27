"""
Extracts features from an observation containing text and a label and writes a
TSV of <feature>[TAB]<feature>[TAB]...<label>

Input: { ... "label": ..., "text": ..., ... }

Output: <feature>[TAB]<feature>[TAB]...<label>


Usage:
    extract_features -h | --help
    extract_features <features> [--language=<classpath>]
                                [--observations=<path>]
                                [--value-labels=<path>]
                                [--verbose]

Options:
    -h --help                Print this documentation
    <features>               Classpath to a list/tuple of features
    --language=<classpath>   Classpath to a Language
    --observations=<path>    Path to a file containing rev_id-label pairs
                             [default: <stdin>]
    --value-labels=<path>    Path to a file to write feature value-labels to
                             [default: <stdout>]
    --verbose                Print logging information
"""
import sys

import docopt
from revscoring.datasources import revision
from revscoring.dependencies import solve
from revscoring.utilities.util import encode, import_from_path


def main(argv=None):
    args = docopt.docopt(__doc__, argv=argv)

    if args['--observations'] is not None:
        obs = (json.loads(line) for line in open(args['--observations']))
    else:
        obs = (json.loads(line) for line in sys.stdin)

    if args['--value-labels'] is not None:
        value_labels = open(args['--value-labels'], 'w')
    else:
        value_labels = sys.stdout

    if args['--language'] is not None:
        language = import_from_path(args['--language'])
        solve = language.solve
    else:
        language = none

    run(obs, features, solve, value_lables)

def run(obs, features, solve, value_labels):

    for ob in obs:
        cache = {revision.text: obs['text']}

        feature_values = solve(features, cache=cache)

        value_labels.write("\t".join([encode(v) for v in feature_values] +
                                     [obs['label']]))
