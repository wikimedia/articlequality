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
                                    [--extractors=<num>]
                                    [--verbose]
                                    [--debug]

    Options:
        -h --help               Print this documentation
        <features>              Classpath to a list/tuple of features
        --labelings=<path>      Path to a file containing labeling docs pairs
                                [default: <stdin>]
        --value-labels=<path>   Path to a file to write feature value-labels to
                                [default: <stdout>]
        --extractors=<num>      The number of parallel extractors to
                                start [default: <cpu count>]
        --verbose               Print dots and stuff to stderr
        --debug                 Print debug logs
"""
import json
import logging
import sys
from multiprocessing import Pool, cpu_count

import docopt
import yamlconf

from revscoring.datasources import revision
from revscoring.dependencies import solve
from revscoring.utilities.util import encode


def main(argv=None):
    args = docopt.docopt(__doc__, argv=argv)

    logging.basicConfig(
        level=logging.WARNING if not args['--debug'] else logging.DEBUG,
        format='%(asctime)s %(levelname)s:%(name)s -- %(message)s'
    )

    features = yamlconf.import_module(args['<features>'])

    if args['--labelings'] != '<stdin>':
        labelings = (json.loads(line) for line in open(args['--labelings']))
    else:
        labelings = (json.loads(line) for line in sys.stdin)

    if args['--value-labels'] != '<stdout>':
        value_labels = open(args['--value-labels'], 'w')
    else:
        value_labels = sys.stdout

    if args['--extractors'] == "<cpu count>":
        extractors = cpu_count()
    else:
        extractors = int(args['--extractors'])

    verbose = args['--verbose']

    run(labelings, features, solve, value_labels, extractors, verbose)


def run(labelings, features, solve, value_labels, extractors, verbose=False):
    extractor_pool = Pool(processes=extractors)

    extractor = LabelingFeatureExtractor(features)

    feature_labels = extractor_pool.imap(extractor.extract, labelings)
    for feature_values, label in feature_labels:
        if feature_values is not None:
            if verbose:
                sys.stderr.write(".")
                sys.stderr.flush()
            value_labels.write("\t".join([encode(v) for v in feature_values] +
                                         [label]))
            value_labels.write("\n")
        else:
            if verbose:
                sys.stderr.write("-")
                sys.stderr.flush()

    if verbose:
        sys.stderr.write("\n")


class LabelingFeatureExtractor:

    def __init__(self, features):
        self.features = features

    def extract(self, labeling):
        if labeling['text'] is None:
            return None

        feature_values = extract_features(self.features, labeling['text'])

        return list(feature_values), labeling['label']


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
