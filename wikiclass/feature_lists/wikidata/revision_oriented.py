from . import datasources, features
from revscoring.datasources import revision_oriented


name = "wikidata.revision"

revision = features.Revision(
    name,
    datasources.Revision(name, revision_oriented.revision)
)
"""
Represents the base revision of interest.  Implements this basic structure:

* revision: :class:`~revscoring.features.wikidata.Revision`
    * parent: :class:`~revscoring.features.wikidata.Revision`
"""
