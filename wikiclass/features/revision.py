import revscoring.datasources.revision

from . import meta


def templates_that_match(regex, name=None):
    return meta.TemplatesThatMatch(regex,
                                   revscoring.datasources.revision.templates,
                                   name=name)
