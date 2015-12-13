"""
``$ wikclass score -h``
::

    Applies a scoring model to a chunch of text.

    Usage:
        score <model-file> [<text>]
        score -h | --help

    Options:
        -h --help     Prints this documentation
        <model-file>  The path to a scorer_model file to use
        <text>        The path to a file containing text to score
                      [default: <stdin>]
"""
import sys

import docopt

from revscoring.scorer_models import MLScorerModel

from .extract_features import extract_features


def main(argv=None):
    args = docopt.docopt(__doc__, argv=argv)

    scorer_model = MLScorerModel.load(open(args['<model-file>'], 'rb'))
    if args['<text>'] == "<stdin>":
        text = sys.stdin.read()
    else:
        text = open(args['<text>']).read()

    print(score(scorer_model, text))


def score(scorer_model, text, cache=None, context=None):
    """
    Scores a chunck of Wikitext markup

    :Parameters:
        scorer_model : :class:`revscoring.ScorerModel`
            A scorer model to apply
        text : `str`
            A chunk of Wikitext markup to score
        cache : `dict`
            Cache to use during feature extraction
        context : `dict`
            Context injected during feature extraction

    :Returns:
        A `dict` of score information.
    """

    feature_values = extract_features(scorer_model.features, text, cache=cache,
                                      context=context)

    score = scorer_model.score(feature_values)

    return score
