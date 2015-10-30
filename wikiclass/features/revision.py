import revscoring.datasources.revision

from . import meta


def templates_that_match(regex, name=None):
    return meta.templates_that_match(regex,
                                     revscoring.datasources.revision.templates,
                                     name=name)
