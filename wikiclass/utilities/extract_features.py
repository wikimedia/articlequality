"""
``$ wikclass extract_features -h``
::

    Extracts features from a labeling doc containing text and a label and writes a
    TSV of <feature>[TAB]<feature>[TAB]...<label> that is compatible with
    `revscoring`'s train_test utility.

    Input: { ... "label": ..., "text": ..., ... }

    Output: <feature>[TAB]<feature>[TAB]...<label>


    Usage:
        extract_features -h | --help
        extract_features <features> [--labelings=<path>]
                                    [--value-labels=<path>]
                                    [--verbose]

    Options:
        -h --help                Print this documentation
        <features>               Classpath to a list/tuple of features
        --labelings=<path>       Path to a file containing labeling docs pairs
                                 [default: <stdin>]
        --value-labels=<path>    Path to a file to write feature value-labels to
                                 [default: <stdout>]
        --verbose                Print logging information
"""
import json
import sys

import docopt
from revscoring.datasources import revision
from revscoring.dependencies import solve
from revscoring.utilities.util import encode, import_from_path


def main(argv=None):
    args = docopt.docopt(__doc__, argv=argv)

    features = import_from_path(args['<features>'])

    if args['--labelings'] != '<stdin>':
        labelings = (json.loads(line) for line in open(args['--labelings']))
    else:
        labelings = (json.loads(line) for line in sys.stdin)

    if args['--value-labels'] != '<stdout>':
        value_labels = open(args['--value-labels'], 'w')
    else:
        value_labels = sys.stdout

    run(labelings, features, solve, value_labels)


def run(labelings, features, solve, value_labels):

    for labeling in labelings:
        feature_values = extract_features(features, labeling['text'])

        value_labels.write("\t".join([encode(v) for v in feature_values] +
                                     [labeling['label']]))
        value_labels.write("\n")


def extract_features(features, text, cache=None, context=None):
    """
    Extracts a set of feature values from a text.

    :Parameters:
        features : `list`( :class:`revscoring.features.Feature` )
            A list of features to extract values for
        text : `str`
            A text from which to extract features

    :Returns:
        A list of extracted feature values
    """
    local_cache = {revision.text: text}
    local_cache.update(cache or {})

    return list(solve(features, cache=local_cache, context=context))
