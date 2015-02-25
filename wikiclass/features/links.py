import re

from revscoring.features import Feature

from ..datasources import internal_links as internal_links_ds

IMAGE_RE = re.compile(r"(file|image):", re.U|re.I)
CATEGORY_RE = re.compile(r"category:", re.U|re.I)

def process_image_links(internal_links_ds):
    return sum(1 for l in internal_links_ds if IMAGE_RE.match(str(l.title)))

image_links = Feature("image_links_process", process_image_links,
                      returns=int, depends_on=[internal_links_ds])
                      
def process_category_links(internal_links_ds):
    return sum(1 for l in internal_links_ds if CATEGORY_RE.match(str(l.title)))

category_links = Feature("category_links", process_category_links,
                         returns=int, depends_on=[internal_links_ds])
                         
def process_internal_links(internal_links_ds):
    return len(internal_links_ds)

internal_links = Feature("internal_links", process_internal_links,
                         returns=int, depends_on=[internal_links_ds])
