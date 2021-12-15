"""
Extracts labels from campaign on a Wikilabels server
Assumes the general schema of the article quality campaign.

Usage:
    fetch_labels <campaign-url>
                 [--filter=<condition>...]
                 [--aggregation=<type>]
                 [--output=<path>]
                 [--debug]
                 [--verbose]

Options:
    <campaign-url>        The base URL of a campaign from which to extract
                          labels.
    --filter=<condition>  A condition for inclusion of labels in the output.
    --aggregation=<type>  Method for aggregating multiple labels (max, min,
                          median, first, last) [default: first]
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

    agg_type = args['--aggregation']
    verbose = args['--verbose']

    run(campaign_url, labels_f, filter, agg_type, verbose)


def run(campaign_url, labels_f, filter, agg_type, verbose):

    campaign_doc = requests.get(campaign_url, params={'tasks': ""}).json()

    for task_doc in campaign_doc['tasks']:
        if not filter.filter(task_doc):
            if verbose:
                sys.stderr.write("s")
                sys.stderr.flush()
            continue

        label_doc = aggregate_labels(task_doc['labels'], agg_type)
        if label_doc is None:
            if verbose:
                sys.stderr.write(".")
                sys.stderr.flush()
        else:
            revision = task_doc['data']
            revision.update(label_doc)
            labels_f.write(json.dumps(util.normalize_revision(revision)))
            labels_f.write("\n")


def aggregate_labels(label_docs, agg_type):

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
            field = "item_quality"
        elif 'wp10' in label_docs[0]['data']:
            field = "wp10"
        else:
            raise RuntimeError("Couldn't find a valid field in {0}"
                               .format(label_docs))

        label_vals = [l['data'][field] for l in label_docs]
        label = aggregate_label_vals(label_vals, agg_type)
        if label is None:
            return None
        else:
            data[field] = label
            data['raw_labels'] = label_vals
            return data


def aggregate_label_vals(labels, agg_type):
    if agg_type == "first":
        return labels[0]
    elif agg_type == "last":
        return labels[-1]
    else:
        _labels = [l for l in labels if l is not None]
        if len(_labels) == 0:
            return None
        elif agg_type == "min":
            return min(_labels)
        elif agg_type == "max":
            return max(_labels)
        elif agg_type == "median":
            return sorted(_labels)[len(_labels)//2]


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
