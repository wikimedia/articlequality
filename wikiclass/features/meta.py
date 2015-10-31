import re

from revscoring import Feature


class TemplatesThatMatch(Feature):

    def __init__(self, regex, templates_ds, name=None):
        if not hasattr(regex, "pattern"):
            regex = re.compile(regex, re.I)

        self.regex = regex

        if name is None:
            name = "{0}({1})".format(self.__class__.__name__, regex.pattern)

        super().__init__(name, self._process, depends_on=[templates_ds],
                         returns=int)

    def _process(self, templates):
        return sum(bool(self.regex.match(str(template.name).replace("_", " ")))
                   for template in templates)
