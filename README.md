# Wikipedia article quality classification

This library provides a set of utilities for performing automatic detection of
assessment classes of Wikipedia articles.  For more information, see the full
documentation at https://articlequality.readthedocs.io .

**Compatible with Python 3.x only.**  Sorry.

* **Install:** ``pip install articlequality``
* **Models:** https://github.com/wikimedia/articlequality/tree/master/models
* **Documentation:** https://articlequality.readthedocs.io

## Basic usage

    >>> import articlequality
    >>> from revscoring import Model
    >>>
    >>> scorer_model = Model.load(open("models/enwiki.nettrom_wp10.gradient_boosting.model", "rb"))
    >>>
    >>> text = "I am the text of a page.  I have a <ref>word</ref>"
    >>> articlequality.score(scorer_model, text)
    {'prediction': 'stub',
     'probability': {'stub': 0.27156163795807853,
                     'b': 0.14707452309674252,
                     'fa': 0.16844898943510833,
                     'c': 0.057668704007171959,
                     'ga': 0.21617801281707663,
                     'start': 0.13906813268582238}}

## Install

### Requirements

* Python 3.5, 3.6 or 3.7
* All the system requirements of [revscoring](https://github.com/wikimedia/revscoring)

### Installation steps

1. clone this repository
2. install the package itself and its dependencies `python setup.py install`
3. You can verify that your installation worked by running `make enwiki_models` to build the English Wikipedia article quality model or `make wikidatawiki_models` to build the item quality model for Wikidata

### Retraining the models

To retrain a model, run `make -B MODEL` e.g. `make -B wikidatawiki_models`. This will redownload the labels, re-extract the features from the revisions, and then retrain and rescore the model.

To skip re-downloading the training labels and re-extracting the features, it is enough `touch` the files in the `datasets/` directory and run the `make` command without the `-B` flag.

### Running tests

Example:

```
pytest -vv tests/feature_lists/test_wikidatawiki.py
```

## Authors
* Aaron Halfaker -- https://github.com/halfak
* Morten Warncke-Wang -- https://github.com/nettrom
