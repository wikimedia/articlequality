import re

import mwparserfromhell as mwp

from ...util import autovivifying

REF_RE = re.compile(r'<ref', re.I)

def byte_length(text): return

def filter_markup(text):
	parsed_text = mwp.parse(text)
	return parsed_text.strip_code(normalize=True)


def analyze(text):
	
	stats = autovivifying.Dict(vivifier=lambda k:0)
	
	stats['byte_length'] = len(text.encode('utf-8'))
	
	# Count number of citations
	stats['references'] = len(REF_RE.findall(text))
	
	parsed_text = mwp.parse(text)
	
	# Count number of headings
	for heading in parsed_text.filter_headings():
		if u'===' in heading:
			stats['headings_lvl2'] += 1
		else:
			stats['headings_lvl3'] += 1

	# Count number of links (this also extracts link inside
	# templates, e.g. as template parameters)
	for link in parsed_text.filter_wikilinks():
		if re.match(r"(file|image):", str(link.title), re.U|re.I):
			stats['imagelinks'] += 1
		elif re.match(r"category:", str(link.title), re.U|re.I):
			stats['categorylinks'] += 1
		else:
			stats['pagelinks'] += 1
				
	# Count number of templates, split into citation templates
	# and non-citation templates, and flag if infobox
	for template in parsed_text.filter_templates():
		stats['templates'] += 1
		# Citation template?
		if re.match(r"cite", str(template.name), re.I):
			stats['citetemplates'] += 1
		# is it an infobox?
		if re.match(r"infobox", str(template.name), re.I):
			stats['infoboxes'] = 1
	
	stats['noncitetemplates'] = stats['templates'] - \
	                            stats['citetemplates']
	
	return stats
