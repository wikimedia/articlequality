import pickle
import sys; sys.path.insert(0, ".")
import csv; csv.field_size_limit(sys.maxsize)

import codecs
import logging
import os.path

from collections import namedtuple

from wikiclass import assessments, languages
from wikiclass.models import RFContentModel
from wikiclass.features import WikitextAndInfonoise

## NOTE: This script requires storage of revision content in a separate
## directory. A tarball with our training/test dataset is available in
## "datasets" directory and can be extracted to be used for this purpose.

def test_model(model_file, testset_file, revision_dir):
    """                                                                     
    Test a trained content length-based Random Forest model based on
    revision IDs and class labels, fetching content from revisions
    stored in the defined directory.
    
    :Parameters:                                                            
    model_file: `str`
        Path to the model file
    testset_file : `str`
        Path to the test set file with revision/class information.
    revision-dir : `str`
        Path to the directory where revision content is stored.
    """
    revdata = []
    for row in csv.DictReader(open(testset_file), delimiter='\t'):
        if row['ordered_class'] == 'A': continue # skip A-class articles
        revdata.append((row['revid'], row['ordered_class']))
        
    logging.info('read {0} revisions from test set'.format(len(revdata)))
    logging.info('reading revision content...')

    # Turn revision IDs into text to train the classifier
    test_set = []
    for revtuple in revdata:
        rev_filename = os.path.join(revision_dir, revtuple[0])
        rev_content = ''
        with codecs.open(rev_filename, 'r', 'utf-8') as infile:
            rev_content = infile.read()

        test_set.append((rev_content, revtuple[1]))

    logging.info('read revision data, testing model')

    model = RFContentModel.from_file(open(model_file, "rb"))
    results = model.test(test_set)

    print(results)

def main():
    import argparse
    
    cli_parser = argparse.ArgumentParser(
        description="Program to test a RFContentModel"
        )

    cli_parser.add_argument("-v", "--verbose", action="store_true",
                            help="write informational output")
    cli_parser.add_argument('model_file', type=str,
                            help='path to stored model file')
    cli_parser.add_argument('testset_file', type=str,
                            help='path to test set TSV file')
    cli_parser.add_argument('revision_dir', type=str,
                            help='path to directory where revision content is stored')

    args = cli_parser.parse_args()
    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)

    test_model(args.model_file, args.testset_file, args.revision_dir)

    # ok, done
    return

if __name__ == '__main__':
    main()

