"""
This script provides access to a set of utilities for extracting features and
building article quality classifiers.

* extract_labelings -- Gathers quality labeling events from XML dumps
* extract_text -- Gathers text for each labeling observation from XML dumps
* extract_features -- Extracts feature_lists for observations
* fetch_text -- Gathers text for each labeling observation from a MediaWiki API

Usage:
    wikiclass (-h | --help)
    wikiclass <utility> [-h | --help]

Options:
    -h | --help  Prints this documentation
    <utility>    The name of the utility to run
"""
import sys
import traceback
from importlib import import_module

import docopt


USAGE = """Usage:
    wikiclass (-h | --help)
    wikiclass <utility> [-h | --help]\n"""


def main():

    if len(sys.argv) < 2:
        sys.stderr.write(USAGE)
        sys.exit(1)
    elif sys.argv[1] in ("-h", "--help"):
        sys.stderr.write(__doc__ + "\n")
        sys.exit(1)
    elif sys.argv[1][:1] == "-":
        sys.stderr.write(USAGE)
        sys.exit(1)

    module_name = sys.argv[1]
    try:
        module = import_module(".utilities." + module_name, package="wikiclass")
    except ImportError:
        sys.stderr.write(traceback.format_exc())
        sys.stderr.write("Could not find utility {0}.\n".format(module_name))
        sys.exit(1)

    module.main(sys.argv[2:])
