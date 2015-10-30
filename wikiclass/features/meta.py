import re

from revscoring import Feature


class templates_that_match(Feature):

    def __init__(self, templates_ds, regex, name=None):
        if not hasattr(regex, "pattern"):
            regex = re.compile(regex)

        self.regex = regex

        if name is None:
            name = "{0}({1})".format(self.__class__.__name__, regex.pattern)

        super().__init__(name, self._process, depends_on=[templates_ds],
                         returns=int)

    def _process(self, templates):
        for template in templates:
            print(template.name)
        return sum(bool(self.regex.match(str(template.name)))
                   for template in templates)
