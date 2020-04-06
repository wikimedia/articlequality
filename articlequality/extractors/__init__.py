"""
This module provides a set of :class:`articlequality.Extractor` s that
implement a strategy for identifying article quality labeling events
historically.  These labelings are used as training data to build prediction
models.

Supported wikis
---------------
.. automodule:: articlequality.extractors.enwiki

.. automodule:: articlequality.extractors.frwiki

.. automodule:: articlequality.extractors.ptwiki

.. automodule:: articlequality.extractors.ruwiki

.. automodule:: articlequality.extractors.svwiki

.. automodule:: articlequality.extractors.trwiki

Base classes
------------
.. automodule:: articlequality.extractors.extractor
"""
from .enwiki import enwiki
from .frwiki import frwiki
from .ptwiki import ptwiki
from .ruwiki import ruwiki
from .svwiki import svwiki
from .trwiki import trwiki

__all__ = [enwiki, frwiki, ptwiki, ruwiki, svwiki, trwiki]
