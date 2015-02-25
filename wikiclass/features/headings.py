from revscoring.features import Feature

from ..datasources import headings


def level_2_headings_process(headings):
    return sum(1 for h in headings if h.level==2)

level_2_headings = Feature("level_2_headings", level_2_headings_process,
                           returns=int, depends_on=[headings])

def level_3_headings_process(headings):
    return sum(1 for h in headings if h.level==3)

level_3_headings = Feature("level_3_headings", level_3_headings_process,
                           returns=int, depends_on=[headings])
