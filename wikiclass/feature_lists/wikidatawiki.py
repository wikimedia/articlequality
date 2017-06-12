from revscoring.features import wikibase as wikibase_features
from revscoring.features.modifiers import not_
from revscoring.features.feature import Feature
from revscoring.features.meta import aggregators, bools
from . import wikibase 
import json
import csv
import os
from urllib.parse import urlencode
import urllib.request
import pywikibase
from revscoring.datasources.datasource import Datasource 
from revscoring.features.wikibase.datasources.revision_oriented import _process_item_doc
from revscoring.features.wikibase.datasources.revision_oriented import _process_item
from revscoring.features.wikibase.datasources.revision_oriented import _process_labels
from revscoring.features.wikibase.datasources.revision_oriented import _process_descriptions
from revscoring.datasources import revision_oriented
from revscoring.features import modifiers


name = "wikidatawiki"

revision = wikibase_features.revision

IMPORTANT_LANG_CODES = {'en', 'de', 'ar', 'zh', 'es', 'pt', 'ru', 'fr'}
"""
Language codes for important languages which are described in https://www.wikidata.org/wiki/Wikidata:Item_quality#Translations
"""

wdir_path = os.path.dirname(os.path.realpath(__file__)) #get the current working directory path
csv_path = os.path.join(wdir_path, 'excluded_qids.csv')
WIKIMEDIA_SOURCES = set()
"""
A set which contains the QID of Wikimedia wikis 
"""	
#add content from the CSV to set
with open(csv_path) as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')
	for line in readCSV:
		WIKIMEDIA_SOURCES.add(int(line[0]))

class properties:
    """
    Mapping of english descriptions to property identifiers
    """
    INSTANCE_OF = 'P31'
    DATE_OF_BIRTH = 'P569'
    DATE_OF_DEATH = 'P570'

class items:
    """
    Mapping of english descriptions to item idenifiers
    """
    HUMAN = 'Q5'

def _process_all_sources(item):

	list_sources_in_JSON = []
	
	try:
		for property in item.claims:
			for claim in item.claims[property]:
				for i, source in enumerate(claim.sources):
					for index_list_1, index_list_2 in source.items(): 
						sources_in_JSON = index_list_2[0].toJSON()
						if('numeric-id' in sources_in_JSON['datavalue']['value']):
							list_sources_in_JSON.append("property:" + str(sources_in_JSON['property']) + "&value:" + str(sources_in_JSON['datavalue']['value']['numeric-id']))
						else:
							list_sources_in_JSON.append("property:" + str(sources_in_JSON['property']) + "&value:" + str(sources_in_JSON['datavalue']['value']))

		return list_sources_in_JSON
	except: 
		return 0 #if the revision does not contain any sources, return 0

def _process_wikimedia_sources(list_all_sources):

	result_list = []
    
	#check revision sources for any Wikimedia project sources
	for list_all_sources_content in list_all_sources:
		for wikimedia_sources_content in WIKIMEDIA_SOURCES:
			try:
				split_source = list_all_sources_content.split("&value:")
				if(int(split_source[1]) == wikimedia_sources_content): #if a source comes from Wikimedia projects and DBpedia (i.e. DBpedia collects data from Wikipedia), append that source to the list
					result_list.append(list_all_sources_content)
					break
			except:
				continue

	return result_list
	
def _process_unique_sources(list_all_sources):
	
	result_set = set()
	
	for value in list_all_sources:
		result_set.add(value)
	
	return len(result_set)
	
def _process_complete_translations(item_labels, item_descriptions):
	return len(item_labels.keys() & item_descriptions.keys())

def _process_important_translations(item_labels, item_descriptions):
	result_set = set()
	
	for label in (item_labels.keys() & item_descriptions.keys() & IMPORTANT_LANG_CODES):
		result_set.add(label)
	
	return len(result_set)/8

def _process_important_translations_labels(item_labels):
	result_set = set()
	
	for label in (item_labels.keys() & IMPORTANT_LANG_CODES):
		result_set.add(label)
	
	return len(result_set)/8

def _process_important_translations_descriptions(item_descriptions):
	result_set = set()
	
	for description in (item_descriptions.keys() & IMPORTANT_LANG_CODES):
		result_set.add(description)
	
	return len(result_set)/8


item_doc = Datasource(name + ".item_doc", _process_item_doc,depends_on=[revision_oriented.revision.text])
"""A JSONable `dict` of content for a Wikibase content."""

item = Datasource(name + ".item", _process_item, depends_on=[item_doc])
"""A `~pywikibase.Item` for the Wikibase content"""

item_labels_datasource = Datasource(name + ".labels", _process_labels, depends_on=[item])
item_descriptions_datasource = Datasource(name + ".descriptions", _process_descriptions,depends_on=[item])
complete_translations = Feature(name + ".complete_translations", _process_complete_translations, depends_on=[item_labels_datasource, item_descriptions_datasource], returns=int)
"`int` :A count of completed translations (a pair of completed label and description) in the revision" 

complete_important_translations = Feature(name + ".complete_important_translations", _process_important_translations, depends_on=[item_labels_datasource, item_descriptions_datasource], returns=float)
"`float` : A ratio of completed important translations (a pair of completed label and description) in the revision"

important_translations_labels = Feature(name + ".important_translations_labels", _process_important_translations_labels, depends_on=[item_labels_datasource], returns=float)
"`float` : A ratio of important translations labels in the revision"

important_translations_descriptions = Feature(name + ".important_translations_descriptions", _process_important_translations_descriptions, depends_on=[item_descriptions_datasource], returns=float)
"`float` : A ratio of important translations descriptions in the revision"

all_sources_datasource = Datasource(name + ".all_sources", _process_all_sources, depends_on=[item])
all_sources = aggregators.len(all_sources_datasource)
"`int` : A count of all sources in the revision" 

all_wikimedia_sources_datasource = Datasource(name + ".all_wikimedia_sources", _process_wikimedia_sources, depends_on=[all_sources_datasource])
all_wikimedia_sources = aggregators.len(all_wikimedia_sources_datasource)
"`int` : A count of all sources which come from Wikimedia projects in the revision" 

all_external_sources = modifiers.sub(all_sources, all_wikimedia_sources)
"A count of all sources which do not come from Wikimedia projects in the revision" 

external_sources_ratio = all_external_sources / modifiers.max (wikibase_features.revision.sources, 1)
"A ratio/division between number of external references and number of claims that have references in the revision"

unique_sources = Feature(name + ".unique_sources", _process_unique_sources, depends_on=[all_sources_datasource], returns=int)
"`int` : A count of unique sources in the revision" 

# Status
is_human = revision.has_property_value(properties.INSTANCE_OF, items.HUMAN,
                                       name=name + '.is_human')
has_birthday = revision.has_property(properties.DATE_OF_BIRTH,
                                     name='revision.has_birthday')
dead = revision.has_property(properties.DATE_OF_DEATH,
                             name='revision.dead')
is_blp = has_birthday.and_(not_(dead))

local_wiki = [
    is_human,
    is_blp,
    external_sources_ratio,
    unique_sources,
    complete_translations,
    complete_important_translations,
	important_translations_labels,
	important_translations_descriptions,
    all_sources,
    all_wikimedia_sources,
    all_external_sources
]

item_quality = wikibase.item + local_wiki
