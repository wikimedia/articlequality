Wikipedia article quality classification
====================================================

A library for performing automatic detection of assessment classes of Wikipedia
articles.

* **Install:** ``pip install articlequality``
* **Models:** `<https://github.com/wikimedia/articlequality/tree/master/models>`_
* **Repo:** `<https://github.com/wikimedia/articlequality>`_
* **License:** MIT License

Contents
--------
.. toctree::
    :maxdepth: 2

    functions
    utilities
    extractors

Basic usage
-----------

    >>> import articlequality
    >>> from revscoring import Model
    >>>
    >>> scorer_model = Model.load(open("models/enwiki.wp10.rf.model", "rb"))
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



Authors
-------
* Aaron Halfaker -- https://github.com/halfak
* Morten Warncke-Wang -- http://www-users.cs.umn.edu/~morten

.. code::

  MIT LICENSE

  Copyright (c) 2015 Aaron Halfaker <ahalfaker@wikimedia.org>

  Permission is hereby granted, free of charge, to any person
  obtaining a copy of this software and associated documentation
  files (the "Software"), to deal in the Software without
  restriction, including without limitation the rights to use,
  copy, modify, merge, publish, distribute, sublicense, and/or
  sell copies of the Software, and to permit persons to whom
  the Software is furnished to do so, subject to the following
  conditions:

  The above copyright notice and this permission notice shall
  be included in all copies or substantial portions of the
  Software.

  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY
  KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
  WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
  PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS
  OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR
  OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
  OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
  SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
