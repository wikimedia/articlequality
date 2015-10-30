import revscoring.datasources.revision
from nose.tools import eq_
from revscoring.dependencies import solve

from .. import meta


def test_templates_that_match():
    templates_ds = revscoring.datasources.revision.templates
    text = """
    {{Foo|bar=1}}
    {{Bar}}
    {{Bar foo}}
    {{Derp bar foo}}
    """

    barfoos = meta.templates_that_match(templates_ds, "bar foo")
    eq_(solve(barfoos, cache={revscoring.datasources.revision.text: text}), 1)
