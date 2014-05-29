#!/usr/env/python
# -*- coding: utf-8 -*-
'''
Library to predict assessments classes for English Wikipedia
based on a given wikitext.

Copyright (C) 2014 SuggestBot Dev Group

This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Library General Public
License as published by the Free Software Foundation; either
version 2 of the License, or (at your option) any later version.

This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Library General Public License for more details.

You should have received a copy of the GNU Library General Public
License along with this library; if not, write to the
Free Software Foundation, Inc., 51 Franklin St, Fifth Floor,
Boston, MA  02110-1301, USA.
'''

import logging

import qualmetrics

import pandas as pd
from sklearn.externals import joblib
from sklearn.ensemble import RandomForestClassifier

from numpy import log2

# Errors the prediction library might throw
class ParseError(Exception):
    '''
    Failed to parse the wikitext.
    '''
    pass

class PredictionError(Exception):
    '''
    Our classifier threw an exception trying to predict
    the assessment class based on a given set of quality metrics.
    '''
    pass

class ModelNotLoadedError(Exception):
    '''
    Called predict() without loading the classifier model first.
    '''
    pass

class Prediction():
    '''
    Results of a quality prediction.  Contains properties for
    the assessed class, probabilities for each class, as well
    as the associated quality metrics (unless asked to not
    store them).

    @param predicted_class: predicted most probably assessment class
    @type predicted_class: str

    @param class_probs: per-class probability from the random forest
    @type class_probs: dict

    @param quality_features: quality features that were used as input
    @type quality_features: qualmetrics.QualityFeatures
    '''
    def __init__(self, predicted_class, class_probs,
                 quality_features):
        self.predclass = predicted_class
        self.classprobs = class_probs
        self.qualfeatures = quality_features



# Random Forest classifier model we use for predictions, must be loaded
# before attempting to predict
predmodel = None

# Do we store the quality features (and associated wikitext) with the
# prediction object.
store_features = True

def load_model(model_path):
    global predmodel # FIXME: better approach than using global?
    try:
        predmodel = joblib.load(model_path)
    except:
        logging.error('Unable to load classifier model from {0}'.format(model_path))
        raise IOError

def predict(wikitext):
    '''
    Predict assessment class based on the given wikitext.

    @param wikitext: the wikitext you want predictions for
    @type wikitext: unicode
    '''
    if not predmodel:
        raise ModelNotLoadedError

    # Calculate the quality metrics
    try:
        qualfeatures = qualmetrics.get_qualfeatures(wikitext)
    except qualmetrics.ParseError:
        # mwparserfromhell.parse() failed
        logging.error(u'unable to parse wikitext')
        raise ParseError
    except:
        # any other type of error
        logging.error(u'unable to extract quality features')
        raise ParseError

    # To assess the quality of the wikitext we need a data frame
    # built out of a dictionary with the calculated metrics
    trans_features = {}
    for (attribute, transfunc) in translations.iteritems():
        trans_features[attribute] = [transfunc(qualfeatures)]
    df = pd.DataFrame(trans_features)
        
    try:
        # feat_cols used to ensure proper column order
        pred_class = predmodel.predict(df.loc[:,feat_cols])[0]
        pred_probs_list = predmodel.predict_proba(df.loc[:,feat_cols])[0]
    except:
        logging.errors(u'unable to predict assessment class')
        raise PredictionError

    logging.info(u'predicted class: {0}'.format(pred_class))

    # Classes are in alphabetical sorted order, so
    # B-class has index 0, FA index 2, and so on
    pred_probs_dict = {
        u'FA': pred_probs_list[2],
        u'GA': pred_probs_list[3],
        u'B': pred_probs_list[0],
        u'C': pred_probs_list[1],
        u'Start': pred_probs_list[4],
        u'Stub': pred_probs_list[5]
        }

    pred_obj = Prediction(pred_class, pred_probs_dict, None)
    if store_features:
        pred_obj.qualfeatures = qualfeatures

    return pred_obj
