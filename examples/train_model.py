import pickle
import sys; sys.path.insert(0, ".")
import csv; csv.field_size_limit(sys.maxsize)

import codecs
import logging
import os.path

from collections import namedtuple

from wikiclass import assessments, languages
from wikiclass.models import RFContentModel

## NOTE: This script requires storage of revision content in a separate
## directory. A tarball with our training/test dataset is available in
## "datasets" directory and can be extracted to be used for this purpose.

def train_model(trainset_file, revision_dir, output_file):
    """                                                                     
    Train a content length-based Random Forest model based on
    revision IDs and class labels, fetching content from revisions
    stored in the defined directory.
    
    :Parameters:                                                            
    trainset_file : `str`
        Path to the training set file with revision/class information.
    revision-dir : `str`
        Path to the directory where revision content is stored.
    output_file : `str`
        Path to write the trained model to.
    """
    revdata = []
    for row in csv.DictReader(open(trainset_file), delimiter='\t'):
        if row['ordered_class'] == 'A': continue # skip A-class articles
        revdata.append((row['revid'], row['ordered_class']))
        
    logging.info('read {0} revisions from training set'.format(len(revdata)))
    logging.info('reading revision content...')

    # Turn revision IDs into text to train the classifier
    training_set = []
    for revtuple in revdata:
        rev_filename = os.path.join(revision_dir, revtuple[0])
        rev_content = ''
        with codecs.open(rev_filename, 'r', 'utf-8') as infile:
            rev_content = infile.read()

        training_set.append((rev_content, revtuple[1]))

    logging.info('read revision data, training model')

    model = RFContentModel.train(
        training_set,
        oob_score=True,
        n_estimators=501,
        min_samples_leaf=8,
        random_state=42
    )
    model.to_file(open(output_file, "wb"))
    

def main():
    import argparse
    
    cli_parser = argparse.ArgumentParser(
        description="Program to train a RFContentModel"
        )

    cli_parser.add_argument("-v", "--verbose", action="store_true",
                            help="write informational output");

    cli_parser.add_argument('trainset_file', type=str,
                            help='path to training set TSV file')
    cli_parser.add_argument('revision_dir', type=str,
                            help='path to directory where revision content is stored')
    cli_parser.add_argument('output_file', type=str,
                            help='path to output model file')

    args = cli_parser.parse_args()
    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)

    train_model(args.trainset_file, args.revision_dir, args.output_file)

    # ok, done
    return

if __name__ == '__main__':
    main()

