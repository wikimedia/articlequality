# Changelog
All notable changes to this project will be documented in this file.

## [Unreleased]

## [0.4.3] - 2022-05-26

### Added
- Adds nlwiki models with sample of probable D, C, and B-class articles for review
- Allow setting custom classes and weights when extracting scores
- Added `non-external-id` statement count as a signal
- Add tests to ensure item parts are being counted correctly
- Add check for image and commons media
- Add retraining model documentation
- Add `is_astronomical_object` feature for wikidatawiki
- Add `is_scholarlyarticle` feature to wikidatawiki
- Add test instructions
- Add some basic installation instructions
- Add new ukwiki model
- Added `words_to_watch` to ptwiki `feature_lists`
- Add `weighted_sum` utility

### Changed
- Rebuilds enwiki model with revscoring 2.11.1
- Builds new model for nlwiki using new features and manual labels
- Remove impactless property suggester feature
- Builds new wikidata model
- Remove number of sitelinks signal from wikibase item quality model
- Reduce the size of wikidata model and simplify its logic
- Move tests to outside of the production code
- Rebuilds ptwiki models with revscoring-2.8.2
- Rebuilds all models with revscoring-2.8.2
- Increase revscoring version requirement
- Update Makefile to remove revisions older than 2014
- Rebuild enwiki model with new image counts
- Rebuilds ptwiki models with more observations

### Fixed
- Fix `extract_scores` utility
- Fix fatal error when creating the model info
- Fix module names import type
- Convert page id to string explicitly
- Fix extraction when there are multiple reverts
- Match articles to talk pages using the API
- Detect labels in old ptwiki templates
- Fix typo in `user_agent`
- Fix misleading dataset filenames
- Update `extract_labelings` doc
- Fix doc for ptwiki extractor

## [0.4.2] - 2020-04-17

### Added
- Feature list for ptwiki

### Changed
- Bumped revscoring to v2.5.1

### Removed
- Old code examples (`examples/test_model.py` and `examples/train_model.py`)

## [0.4.1] - 2019-07-25

### Changed
- Bumped revscoring to v2.4.x
- Added `content_type` param to setup.py
- Minor formatting edits in README

## [0.4.0] - 2019-07-25

### Added
- Added features for English Wikipedia's short-format notes.
- Release Criteria document
- svwiki feature lists
- Added ability to do a fast filtering pass before parsing wikitext.
- Added svwiki extractor.
- Added Wikibase item features.
- Added `util` utility helpers.
- Added `fetch_labels` utilities.
- Added trwiki extractor.
- Added `words_to_watch` count to enwiki feature lists.
- Added new features to wikidatawiki - (@glorianY)
- Added basic extraction pattern for item quality model.
- Added Persian Wikipedia features.
- Added glwiki feature lists.
- Adds `item_completes` to wikidatawiki.

### Changed
- Rename wikiclass to articlequality.
- Bumped revscoring to v2.3.4
- Updated `fetch_text` for new `rvslots` API param.
- Remove target files when commands error out.
- Replaced filenames with automatic Make variables.
- Update classification examples to revscoring 2.x
- Started using TravisCI for automated builds.
- Use PyTest for testing now.
- Rename pagelevel prediction classes in frwikisource.
- Rename `wp10` -> `articlequality`.
- Change wikidatawiki models to use GradientBoosting.

### Fixed
- Fixed bug in `fetch_item_info`.
- Update about.py in wikiclass folder to the right github link.
- Resolved mwxml/mwtypes version conflict.
- Fixed "who" templates in enwiki features.
- Fixed trwiki extractor so that it works for 'baslagıç'.

## [0.3.2] - 2017-01-07

### Added
- Added feature lists for ruwiki.
- Added `extract_scores` utility.

### Changed
- Implemented modular `about.py` pattern for pkg info.
- Bumped revscoring to v1.3.0
- Add HTML comment filtering to Russian extractor
- Added testcase to ruwiki extractor.
- Switched RF for GradientBoosting models in Makefile.
- Cleaned up `extract_from_text` utility.

### Fixed
- Wrong variable name in frwiki extractor.
- Fixed division with modifiers in `wikipedia.article`.

## [0.3.1] - 2015-04-27

### Added
- Added Russian assessment extractor. - @nettrom

### Changed
- Flexibility for revscoring version requirement.

### Fixed
- Typo in French extractor. - @nettrom

## [0.3.0] - 2015-03-17

### Added
- Added basic counts for cn templates and dict_words/word to frwiki feature list.
- Added tuning reports to Makefile.

### Changed
- Bumped revscoring requirement to v1.1.0.
- Updated feature extractor for revscoring 1.x
- Updates enwiki and frwiki `feature_lists` for revscoring 1.x

## [0.2.3] - 2015-03-10

### Changed
- Using `mwreverts`, `mwxml`, `mwapi` libraries instead of `mw` lib.

## [0.2.2] - 2015-12-13

### Changed
- Bumped revscoring requirement to 0.7.10 and fixed issues this causes.

## [0.2.1] - 2015-11-12

### Changed
- Updated requirement for mwtypes >= 0.2.0

## [0.2.0] - 2015-11-12

### Added
- Adds new `templates_that_match` meta feature.
- Added `not_an_article` filter.
- Added `who`, `citation_needed` and `main_article` templates to enwiki.

### Changed
- Bumped revscoring requirement to 0.7.2
- Switched text extraction to be API-based.
- Added verbose option to `extract_features`.
- Parallelization for `extract_features`.

### Fixed
- Minor divide-by-zero errors in enwiki and frwiki features.
- Template list error for frwiki. - @gpaumier

### Removed
- Remove empty sections from CHANGELOG, they occupy too much space and
create too much noise in the file. People will have to assume that the
missing sections were intentionally left out because they contained no
notable changes.

## [0.1.3] - 2015-10-07

### Changed
- Cleanup to feature sets for enwiki and frwiki.
- Spaces to tabs in Makefile
- Pass `page_labeling` to `extract_text` as arg.

## [0.1.2] - 2015-09-25

### Fixed
- Fixed issue with generator requirements in setup.

## [0.1.1] - 2015-09-24

### Changed
- README format changed from `.rst` to `.md`.
- Update functions documentation.
- Minor updates to Makefile and `extract_text` for running on stat3


## [0.1.0] - 2015-09-03

### Added
- Basic API.
- Added tests for all features and datasources.
- Added frwiki extractor
- Added `extract_text` utility.

### Changed
- Restructured wikiclass to make use of the revscoring package.
- Completed enwiki extractor.
- Added error handling in case mwparserfromhell fails.
- Switches `extract_labelings` to use mwxml library
- Remove post '/' stuff from titles during normalization.
- Additional documentation.

### Fixed
- Minor issues in `extract_features.py` script.

### Removed
- Removed duplicated feature definitions(now part of revscoring).
-

## [0.0.2] - 2014-07-21

### Added
- Added minimal docs setup.
- Added a LICENSE.

### Changed
- Moved `add_text` util to `scripts/` dir.
- Completed basic docs.

### Fixed
- README errors.
- Handle division-by-zero case for articles with no words.

## [0.0.1] - 2014-06-11
- First release on PyPI.

### Added
- Working RFTextModel
- Added `add_text` util.
- Basic README.

