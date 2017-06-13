import json
import csv
import os
from urllib.parse import urlencode
import urllib.request
import pywikibase

from revscoring.datasources.datasource import Datasource 
from revscoring.dependencies.dependent import DependentSet
from revscoring.features.wikibase.datasources.revision_oriented import _process_sources
from revscoring.features.wikibase.datasources.revision_oriented import _claim_to_str


class Revision(DependentSet):

    def __init__(self, name, revision_datasources):
        super().__init__(name)

        self.item_doc = Datasource(
            name + ".item_doc", _process_item_doc,
            depends_on=[revision_datasources.text]
        )
        """
        A JSONable `dict` of content for a Wikibase content.
        """

        self.item = Datasource(
            name + ".item", _process_item,
            depends_on=[self.item_doc]
        )
        """
        A `~pywikibase.Item` for the Wikibase content
        """
		
        self.unique_sources = Datasource(
	        name + ".unique_sources", _process_unique_sources, depends_on=[self.item]
        )

        """
        A `set` of unique sources in the revision
        """
		
        self.complete_translations = Datasource(
	        name + ".complete_translations", _process_complete_translations, depends_on=[self.item]
        )

        """
        A `list` of completed translations (a pair of completed label and description) in the revision
        """
	
        self.all_sources = Datasource(
			name + ".all_sources", _process_all_sources, depends_on=[self.item]
		)

        """
        A `list` of all sources in the revision
        """
		
        self.all_wikimedia_sources = Datasource(
	        name + ".all_wikimedia_sources", _process_wikimedia_sources, depends_on=[self.item]
        )

        """
        A `list` of all sources which come from Wikimedia projects in the revision
        """

def _process_item_doc(text):
    if text is not None:
        return json.loads(text)
    else:
        return None


def _process_item(item_doc):
    item = pywikibase.ItemPage()
    item.get(content=item_doc or {'aliases': {}})
    return item

def _process_all_sources(item):

	list_sources_in_JSON = []
	
	try:
		for property in item.claims:
			list_of_properties = property
			for claim in item.claims[list_of_properties]:
				list_of_claims = claim
				for i, source in enumerate(list_of_claims.sources):
					for index_list_1, index_list_2 in source.items(): 
						sources_in_JSON = index_list_2[0].toJSON()
						list_sources_in_JSON.append(sources_in_JSON['datavalue']['value'])
		
		return list_sources_in_JSON
	except:
		return 0 #if the revision does not contain any sources, return 0

def _process_wikimedia_sources(item):

	list_sources_in_JSON = []
	list_wikimedia_sources = []
	
	try:
		for property in item.claims:
			list_of_properties = property
			for claim in item.claims[list_of_properties]:
				list_of_claims = claim
				for i, source in enumerate(list_of_claims.sources):
					for index_list_1, index_list_2 in source.items(): 
						sources_in_JSON = index_list_2[0].toJSON()
						list_sources_in_JSON.append(sources_in_JSON['datavalue']['value'])
		
		wdir_path = os.path.dirname(os.path.realpath(__file__)) #get the current working directory path
		csv_path = os.path.join(wdir_path, 'excluded_qids.csv')
		
		for list_sources_in_JSON_content in list_sources_in_JSON: 
			with open(csv_path) as csvfile:
				readCSV = csv.reader(csvfile, delimiter=',')
				for line in readCSV:				
					try:
						if(list_sources_in_JSON_content['numeric-id'] == int(line[0])): #if a source comes from Wikimedia projects and DBpedia (i.e. DBpedia collects data from Wikipedia), append that source to the list
							list_wikimedia_sources.append(list_sources_in_JSON_content)
							break
					except:
						continue
		return list_wikimedia_sources
	except:
		return 0 #if the revision does not contain any wikimedia projects sources, return 0

def _process_external_sources(item):
    
    count_all_sources = len(_process_all_sources(item))
    count_wiki_sources = len(_process_wikimedia_sources(item))
    return count_all_sources - count_wiki_sources


def _process_external_sources_ratio(item):
	
	try: 
		count_external_sources = _process_external_sources(item)
		count_claims_with_sources = len(_process_sources(item))
		return count_external_sources/count_claims_with_sources
	except: 
		return 0.0 #if the revision does not contain any sources, return 0 
	
def _process_unique_sources(item):
	
	list_sources_in_JSON = []
	result_set = set()
	
	for property in item.claims:
		list_of_properties = property
		for claim in item.claims[list_of_properties]:
			list_of_claims = claim
			for i, source in enumerate(list_of_claims.sources):
				for index_list_1, index_list_2 in source.items(): 
					sources_in_JSON = index_list_2[0].toJSON()
					list_sources_in_JSON.append("property : " + str(sources_in_JSON['property']) + " & value : " + str(sources_in_JSON['datavalue']['value']))
	
	#eliminate duplicates
	for value in list_sources_in_JSON:
		result_set.add(value)
	
	return result_set
	

def _process_complete_translations(item):
	item_labels_dict = item.labels
	item_desc_dict = item.descriptions
	combined_dict = {}
	result_set = []
	
	#merging item label dictionary and item description dictionary
	for key in (item_labels_dict.keys() | item_desc_dict.keys()):
		if key in item_labels_dict: combined_dict.setdefault(key, []).append(item_labels_dict[key])
		if key in item_desc_dict: combined_dict.setdefault(key, []).append(item_desc_dict[key])
	
	#if a language consists of both item label and item description exist, add the language into result_set
	for value in combined_dict.items():
		if(len(value[1]) == 2): 
			result_set.append(value[0])
			
	return result_set

def _process_important_translations(item):
	item_labels_dict = item.labels
	item_desc_dict = item.descriptions
	combined_dict = {}
	result_set = []
	
	#merging item label dictionary and item description dictionary
	for key in (item_labels_dict.keys() | item_desc_dict.keys()):
		if key in item_labels_dict: combined_dict.setdefault(key, []).append(item_labels_dict[key])
		if key in item_desc_dict: combined_dict.setdefault(key, []).append(item_desc_dict[key])
	
	#if an important language consists of both item label and item description exist, add the language into result_set
	for value in combined_dict.items():
		if((len(value[1]) == 2) and (value[0] in ('en', 'de', 'ar', 'zh', 'es', 'pt', 'ru', 'fr'))):
			result_set.append(value[0])

	return len(result_set)/8
