from revscoring.dependencies.dependent import DependentSet
from revscoring.features.feature import Feature
from revscoring.features.meta import aggregators, bools


class Revision(DependentSet):

    def __init__(self, name, revision_datasources):
        super().__init__(name)

        self.datasources = revision_datasources

        self.external_sources_ratio = self.datasources.external_sources_ratio 
        "`float` : A ratio/division between number of external references and number of claims that have references in the revision"
        self.unique_sources = aggregators.len(self.datasources.unique_sources)  
        "`int` : A count of unique sources in the revision" 
        self.complete_translations = aggregators.len(self.datasources.complete_translations)
        "`int` :A count of completed translations (a pair of completed label and description) in the revision" 
        self.complete_important_translations = self.datasources.complete_important_translations 
        "`float` : A ratio of completed important translations (a pair of completed label and description) in the revision"
        self.image_quality = self.datasources.image_quality 
        "`float` : Megapixels of the image in the revision"
        self.all_sources = aggregators.len(self.datasources.all_sources)
        "`int` : A count of all sources in the revision" 
        self.all_wikimedia_sources = aggregators.len(self.datasources.all_wikimedia_sources)
        "`int` : A count of all sources which come from Wikimedia projects in the revision" 
        self.all_external_sources = self.datasources.all_external_sources
        "`int` : A count of all sources which do not come from Wikimedia projects in the revision" 


