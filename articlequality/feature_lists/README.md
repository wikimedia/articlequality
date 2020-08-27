## Wikidata feature lists

To add/delete new properties from the `wikidatawiki.py` feature list we need to manually update the file `property_datatypes.py`. 

Currently the file contains a list of `NON_EXTERNAL_IDENTIFIERS` that we want to extract as features. `NON_EXTERNAL_IDENTIFIERS` is used instead of `EXTERNAL_IDENTIFIERS` because external identifiers comprise about 5000+ of the total 8000+ that we have currently on the database. Using NON_EXTERNAL_IDENTIFIERS (~2500) reduces the processing time. 