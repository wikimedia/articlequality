# Wikipedia article quality classification

This library provides a set of utilities for performing automatic detection of assessment classes of Wikipedia articles.  For more information, see the full documentation at http://pythonhosted.org/wikiclass.

**Compatible with Python 3.x only.**  Sorry.

* **Install:** ``pip install wikiclass``
* **Models:** https://github.com/halfak/wikiclass/tree/master/models
* **Documentation:** http://pythonhosted.org/wikiclass

## Basic usage

    >>> import wikiclass
    >>> from revscoring.scorer_models import MLScorerModel
    >>>
    >>> scorer_model = MLScorerModel.load(open("models/enwiki.wp10.rf.model", "rb"))
    >>>
    >>> text = "I am the text of a page.  I have a <ref>word</ref>"
    >>> wikiclass.score(scorer_model, text)
    {'prediction': 'stub',
     'probability': {'stub': 0.27156163795807853,
                     'b': 0.14707452309674252,
                     'fa': 0.16844898943510833,
                     'c': 0.057668704007171959,
                     'ga': 0.21617801281707663,
                     'start': 0.13906813268582238}}


## Authors
* Aaron Halfaker -- https://github.com/halfak
* Morten Warncke-Wang -- http://www-users.cs.umn.edu/~morten
