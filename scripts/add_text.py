"""
Reads a TSV, looks for a 'rev_id' field and queries the MediaWiki API of your
choosing to get the associated text.  If a text is found, a new line will be
printed that contains all of the input column and an additional column for text.

Usage:
    add_text <api_url>
    add_text -h | --help
    add_text --version

Options:
    -h --help  Show this screen.
    --version  Show version.
    <api_url>  The url of a MediaWiki API e.g.
               "https://en.wikipedia.org/w/api.php"
"""
import sys, csv
from docopt import docopt
from mw import api
from mw.api.errors import APIError


def main():
    args = docopt(__doc__, version="0.0.0")
    
    api_session = api.Session(args['<api_url>'])
    
    writer = None
    for row in csv.DictReader(sys.stdin, delimiter="\t"):
        if writer == None:
            writer = csv.DictWriter(sys.stdout, list(row.keys()) + ['text'],
                                    delimiter="\t")
            writer.writeheader()
        
        try:
            docs = list(api_session.revisions.query(revids={row['rev_id']},
                                                    properties={"content"}))
            
            row['text'] = docs[0]['*']
            
            writer.writerow(row)
            
            sys.stderr.write(".")
        except APIError:
            raise
            sys.stderr.write("a")
        except KeyError:
            sys.stderr.write("e")
        finally:
            sys.stderr.flush()
        
    

if __name__ == "__main__": main()
