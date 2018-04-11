"""
Extracts labels from campaign on a Wikilabels server
Assumes the general schema of the article quality campaign.

Usage:
    fetch_labels <campaign-url>
                 [--filter=<condition>...]
                 [--output=<path>]
                 [--debug]
                 [--verbose]

Options:
    <campaign-url>        The base URL of a campaign from which to extract
                          labels.
    --filter=<condition>  A condition for inclusion of labels in the output.
    --output=<path>       Path to an file to write output to
                          [default: <stdout>]
    --debug               Print debug logging
    --verbose             Print dots and stuff representing progress
"""
import json
import logging
import re
import sys

import docopt
import requests

from . import util


def main(argv=None):
    args = docopt.docopt(__doc__, argv=argv)

    logging.basicConfig(
        level=logging.DEBUG if args['--debug'] else logging.WARNING,
        format='%(asctime)s %(levelname)s:%(name)s -- %(message)s'
    )

    campaign_url = args['<campaign-url>']

    filter = Filter.from_strings(args['--filter'])

    if args['--output'] == "<stdout>":
        labels_f = sys.stdout
    else:
        labels_f = open(args['--output'], "w")

    verbose = args['--verbose']

    run(campaign_url, labels_f, filter, verbose)


def run(campaign_url, labels_f, filter, verbose):

    campaign_doc = requests.get(campaign_url, params={'tasks': ""}).json()

    for task_doc in campaign_doc['tasks']:
        if not filter.filter(task_doc):
            if verbose:
                sys.stderr.write("s")
                sys.stderr.flush()
            continue

        label_doc = aggregate_labels(task_doc['labels'])
        if label_doc is None:
            if verbose:
                sys.stderr.write(".")
                sys.stderr.flush()
        else:
            revision = task_doc['data']
            revision.update(label_doc)
            labels_f.write(json.dumps(util.normalize_revision(revision)))
            labels_f.write("\n")


def aggregate_labels(label_docs):

    if len(label_docs) == 0:
        return None
    else:
        if sum('automated' not in l['data'] for l in label_docs) > 0:
            auto_labeled = False
        else:
            auto_labeled = True
        data = {'auto_labeled': auto_labeled,
                'timestamp': str(label_docs[0]['timestamp'])}

        if 'item_quality' in label_docs[0]['data']:
            data['item_quality'] = label_docs[0]['data']['item_quality']
        elif 'wp10' in label_docs[0]['data']:
            data['wp10'] = label_docs[0]['data']['wp10']
        return data


OPERATORS = {"=": lambda field, value: field == value,
             "!=": lambda field, value: field != value,
             ">": lambda field, value: field > value,
             ">=": lambda field, value: field >= value,
             "<": lambda field, value: field < value,
             "<=": lambda field, value: field <= value}
FILTER_RE = re.compile(r"([^.<>!=]+(\.[^.<>!=]+)*)" +
                       r"\s*(=|!=|>|>=|<|<=)\s*" +
                       r"(.+)", re.I)


class Filter:

    def __init__(self, conditions):
        self.conditions = conditions

    def filter(self, doc):
        return sum(condition(doc) for condition in self.conditions) == \
            len(self.conditions)

    @classmethod
    def from_strings(cls, condition_strings):
        conditions = []
        for condition_string in condition_strings:
            fields_string, _, operator, value_string = \
                FILTER_RE.match(condition_string).groups()

            conditions.append(
                lambda doc: OPERATORS[operator](query_json(fields_string, doc),
                                                json.loads(value_string)))

        return cls(conditions)


def query_json(field_string, doc):
    fields = field_string.split(".")
    return _query_json_fields(fields, doc)


def _query_json_fields(fields, doc):
    field = fields.pop(0)
    if len(fields) > 0:
        return _query_json_fields(fields, doc[field])
    else:
        return doc[field]
