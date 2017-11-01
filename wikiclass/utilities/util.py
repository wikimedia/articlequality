

def normalize_revision(rev_doc):
    autolabel = rev_doc.get('autolabel', {})
    if "needs_review" in rev_doc:
        autolabel['needs_review'] = ensure_bool(rev_doc['needs_review'])
        del rev_doc['needs_review']
    if "reason" in rev_doc:
        autolabel['reason'] = rev_doc['reason'] \
            if rev_doc['reason'] != "NULL" else None
        del rev_doc['reason']

    rev_doc['rev_id'] = int(rev_doc['rev_id'])
    rev_doc['autolabel'] = autolabel

    return rev_doc


def ensure_bool(val):
    if isinstance(val, bool):
        return val
    elif isinstance(val, str):
        return val.lower() in ("true", "1", "t", "y")
    else:
        return bool(val)
