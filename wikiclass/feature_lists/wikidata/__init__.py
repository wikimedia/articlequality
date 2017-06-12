"""
This features module provides access to features of the bytes of content in
revisions.

.. autodata:: revscoring.features.wikibase.revision

Supporting classes
++++++++++++++++++

.. autoclass:: revscoring.features.wikibase.Revision
    :members:
    :member-order: bysource

"""
from .revision_oriented import revision
from .features import Revision

__all__ = [revision, Revision]
