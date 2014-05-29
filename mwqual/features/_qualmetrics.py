#!/usr/env/python
# -*- coding: utf-8 -*-
'''
Library to calculate quality metrics for Wikipedia articles.

Copyright (C) 2014 SuggestBot Dev Group

This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Library General Public
License as published by the Free Software Foundation; either
version 2 of the License, or (at your option) any later version.

This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Library General Public License for more details.

You should have received a copy of the GNU Library General Public
License along with this library; if not, write to the
Free Software Foundation, Inc., 51 Franklin St, Fifth Floor,
Boston, MA  02110-1301, USA.
'''

import re
import logging

import mwparserfromhell as mwp
import nltk

class QualityFeatures(object):
    """
    Quality features for a given revision.
    """
    def __init__(self, revisionid,
                 pageid=None, pagetitle=None, talkpageid=None):
        self.revid = revisionid
        self.timestamp = None
        self.content = u""
        self.api_length = 0
        self.length = 0
        self.num_headings_lvl2 = 0
        self.num_headings_lvl3 = 0
        self.num_references = 0
        self.num_categorylinks = 0
        self.num_pagelinks = 0
        self.num_imagelinks = 0
        self.num_templates = 0
        self.num_noncitetemplates = 0
        self.num_citetemplates = 0
        self.infonoise = 0
        self.has_infobox = 0
        # Meta-info about the page
        self.pageid = pageid
        self.pagetitle = pagetitle
        self.talkpage = talkpageid
        self.assessments = []

class_regex = re.compile(ur"^Category[:](FA|GA|A|B|C|Start|Stub)-Class")
ref_regex = re.compile(ur'<ref', re.I)

# Default is English language stemmer and stopwords
stemmer = nltk.stem.SnowballStemmer('english')
stopwords = nltk.corpus.stopwords.words('english')

class ParseError(Exception):
    '''
    Failed to correctly parse the wikitext.
    '''
    pass

def calc_infonoise(page_code, page_len):
    """
    Calculate the InfoNoiseScore for the given parsed code
    with an associated raw wikitext length.  The definition of
    InfoNoiseScore is found in Table 1 of the appendix of
    Assessing Information Quality of a Community-Based Encyclopedia
    by Stvilia, Twidale, Smith, and Gasser (2005).
    
    @param page_code: parsed wikitext for a given page
    @type page_code: mwparserfromhell.WikiCode
    
    @param page_len: raw length of the wikitext
    @type page_len: int

    @return: the calculate InfoNoiseScore
    """
        
    # Strip away MediaWiki code (templates and such)
    # (we can't use filter_text() because it keeps template params)
    parsed_text = page_code.strip_code(normalize=True)

    # Extract words from the wikitext
    words = nltk.tokenize.wordpunct_tokenize(parsed_text)

    # We now stem the words, remove stop-words (using NLTK's corpus of
    # stopwords) and then calculate the InfoNoise value.
    stemmed_words = []
    for word in words:
        # if stemming fails, skip
        try:
            stemmed_words.append(stemmer.stem(word))
        except:
            continue
        
    nonstops = [w for w in stemmed_words
                if w.lower() not in stopwords]

    logging.info("length={l}, words={w}, stemmed words={sw}, non-stopwords={nsw}".format(l=page_len, w=len(words), sw=len(stemmed_words), nsw=len(nonstops)))
    
    # Calculate info noise
    # 1.0 - Number of tokens/size of article
    return 1.0 - (1.0*len(u" ".join(nonstops))/page_len)
    
def get_qualfeatures(wikitext,
                     revisionid=None, pageid=None, pagetitle=None):
    '''
    For the given raw wikitext, extract quality features
    (number of links, categorylinks, image links, etc).
    
    @param wikitext: raw wikitext
    @type wikitext: unicode

    @return: QualityFeatures object with the calculated metrics.
    '''

    features = QualityFeatures(revisionid)
    features.pageid = pageid
    features.pagetitle = pagetitle
   
    features.length = len(wikitext.encode('utf-8'))

    try:
        parsed_text = mwp.parse(wikitext)
    except:
        logging.error(u'Failed to parse revision {revid}'.format(revid=revisionid))
        raise ParseError

    features.infonoise = calc_infonoise(parsed_text,
                                        features.length)

    # Count number of citations
    features.num_references = len(ref_regex.findall(wikitext))

    # Count number of headings
    for heading in parsed_text.filter_headings():
        if u'===' in heading:
            features.num_headings_lvl2 += 1
        else:
            features.num_headings_lvl3 += 1

    # Count number of links (this also extracts link inside
    # templates, e.g. as template parameters)
    for link in parsed_text.filter_wikilinks():
        if re.match(ur"(file|image):", unicode(link.title), re.U|re.I):
            features.num_imagelinks += 1
        elif re.match(ur"category:", unicode(link.title), re.U|re.I):
            features.num_categorylinks += 1
        else:
            features.num_pagelinks += 1
                
    # Count number of templates, split into citation templates
    # and non-citation templates, and flag if infobox
    for template in parsed_text.filter_templates():
        features.num_templates += 1
        # Citation template?
        if re.match(ur"cite", unicode(template.name), re.I):
            features.num_citetemplates += 1
        # is it an infobox?
        if re.match(ur"infobox", unicode(template.name), re.I):
            features.has_infobox = 1

    features.num_noncitetemplates = features.num_templates \
        - features.num_citetemplates

    return features

def main():
    # FIXME: do some unit tests
    pass

if __name__ == "__main__":
    main()
