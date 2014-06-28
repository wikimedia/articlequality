.. Wiki-Class documentation master file, created by
   sphinx-quickstart on Wed Jun 11 22:44:18 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Wiki-Class: Wikipedia article quality classification
====================================================

A library for performing automatic detection of assessment classes of Wikipedia
articles.

**Compatible with Python 3.x only.**  Sorry.

* **Install:** ``pip install wikiclass``
* **Models:** `<https://github.com/halfak/Wiki-Class/tree/master/models>`_
* **Repo:** `<https://github.com/halfak/Wiki-Class>`_

Basic usage
===========
If you want to detect some assessment classes, you're going to need a model.
You can `download a prebuilt model
<https://github.com/halfak/Wiki-Class/tree/master/models>`_ or build one
yourself.

Model from file
---------------
.. code-block:: python
    
    from wikiclass.models import RFTextModel
    
    model = RFTextModel.from_file(open("enwiki.rf_text.model", "rb"))
    
    assessment, probabilities = model.classify("Some article text")
    
    print("I'm about {0}% ".format(probabilities[assessment]*100) + \
          "sure that this should be classified {0}".format(assessment))
    

Model building
--------------
.. code-block:: python
    
    from wikiclass.models import RFTextModel
    from wikiclass import assessments
    
    # Gather a training and test set
    #Both train_set and test_set are a list of tuples who are ("article text", "classification")
    train_set = [
        ("Some article text", "Stub"),
        ("Some more article text<ref>news</ref>.", "Start")
        # ...
    ]
    test_set = [
        ("The Lorem Ipsum dolored the sit amet.", "C"),
        ("'''Lorem Ipsum''', sit amet the dolor amer. {{InfoBox|...}}", "FA")
        # ...
    ]
    
    # Train a model
    model = RFTextModel.train(
        train_set,
        assessments=assessments.WP10
    )
    
    # Run the test set & print the results
    results = model.test(test_set)
    print(results)
    
    # Write the model to disk for reuse.
    model.to_file(open("enwiki.rf_text.model", "wb"))

Modules
=======
:ref:`wikiclass.models <wikiclass.models>`
    A set of classification models that can be trained and used to classify
    articles.
    
    * :class:`~wikiclass.models.RFTextModel` -- A random forrest classifier that extracts features from article text.

:ref:`wikiclass.features <wikiclass.features>`
    A set of feature extractors used to organize a set of features for use in
    model training and classification.
    
    * :class:`~wikiclass.features.WikitextAndInfonoise` -- A text feature extractor that gathers wiki markup features and an information-based measure.

:ref:`wikiclass.languages <wikiclass.languages>`
    Some :class:`~wikiclass.features.FeatureExtractor` s require information
    about the language being processed.  This module contains basic language
    info for common languages.
    
    * :func:`~wikiclass.languages.get`, gets a :class:`~wikiclass.languages.Language` based on a name.  Currently supported languages include:
        * ``"English"``
    * :func:`~wikiclass.languages.register`, registers a new :class:`~wikiclass.languages.Language` for access from :func:`~wikiclass.languages.get`.


Authors
=======
    Aaron Halfaker
        * ahalfaker@wikimedia.org
        * `<http://halfaker.info>`_
    Morten Warncke-Wang
        * `<http://www-users.cs.umn.edu/~morten>`_



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
