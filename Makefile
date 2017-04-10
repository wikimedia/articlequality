models: \
	enwiki_models \
	frwiki_models \
	ruwiki_models

tuning_reports: \
	enwiki_tuning_reports \
	frwiki_tuning_reports \
	ruwiki_tuning_reports

test_statistics = -s 'table' -s 'accuracy' -s 'roc' -s 'f1'

wp10_major_minor = 0.5

########################## English Wikipedia ###################################
datasets/enwiki.labelings.20150602.json:
	./utility extract_labelings \
	  /mnt/data/xmldatadumps/public/enwiki/20150602/enwiki-20150602-pages-meta-history*.xml*.bz2 \
	  --verbose > \
	datasets/enwiki.labelings.20150602.json


datasets/enwiki.labelings.30k.json: \
		datasets/enwiki.labelings.20150602.json
	( \
	  grep -P '"wp10": "stub"' datasets/enwiki.labelings.20150602.json | \
	  shuf -n 5000; \
	  grep -P '"wp10": "start"' datasets/enwiki.labelings.20150602.json | \
	  shuf -n 5000; \
	  grep -P '"wp10": "c"' datasets/enwiki.labelings.20150602.json | \
	  shuf -n 5000; \
	  grep -P '"wp10": "b"' datasets/enwiki.labelings.20150602.json | \
	  shuf -n 5000; \
	  grep -P '"wp10": "ga"' datasets/enwiki.labelings.20150602.json | \
	  shuf -n 5000; \
	  grep -P '"wp10": "fa"' datasets/enwiki.labelings.20150602.json | \
	  shuf -n 5000 \
	) | \
	shuf > \
	datasets/enwiki.labelings.30k.json

datasets/enwiki.labeling_revisions.w_text.30k.json: \
		datasets/enwiki.labelings.30k.json
	cat datasets/enwiki.labelings.30k.json | \
	./utility fetch_text \
	  --api-host=https://en.wikipedia.org \
	  --verbose > \
	datasets/enwiki.labeling_revisions.w_text.30k.json

datasets/enwiki.labeling_revisions.w_cache.30k.json: \
		datasets/enwiki.labeling_revisions.w_text.30k.json
	cat datasets/enwiki.labeling_revisions.w_text.30k.json | \
	./utility extract_from_text \
	  wikiclass.feature_lists.enwiki.wp10 \
	  --verbose > \
	datasets/enwiki.labeling_revisions.w_cache.30k.json

tuning_reports/enwiki.wp10.md: \
		datasets/enwiki.labeling_revisions.w_cache.30k.json
	cat datasets/enwiki.labeling_revisions.w_cache.30k.json | \
	revscoring tune \
	  config/classifiers.params.yaml \
	  wikiclass.feature_lists.enwiki.wp10 \
	  wp10 \
	  --cv-timeout=60 \
	  --scoring=accuracy \
	  --debug \
	  --label-type=str > \
	tuning_reports/enwiki.wp10.md

models/enwiki.wp10.rf.model: \
		datasets/enwiki.labeling_revisions.w_cache.30k.json
	cat datasets/enwiki.labeling_revisions.w_cache.30k.json | \
	revscoring cv_train \
	  revscoring.scorer_models.GradientBoosting \
	  wikiclass.feature_lists.enwiki.wp10 \
	  wp10 \
	  --version $(wp10_major_minor).0 \
	  -p 'n_estimators=700' \
	  -p 'learning_rate=0.01' \
	  -p 'max_features="log2"' \
	  -p 'max_depth=7' \
	  $(test_statistics) \
	  --balance-sample \
	  --center --scale > \
	models/enwiki.wp10.rf.model

datasets/enwiki.labeling_revisions.w_cache.nettrom_30k.json: \
		datasets/enwiki.labeling_revisions.nettrom_30k.json
	cat datasets/enwiki.labeling_revisions.nettrom_30k.json | \
	revscoring extract \
	  wikiclass.feature_lists.enwiki.wp10 \
	  --host https://en.wikipedia.org \
	  --verbose > \
	datasets/enwiki.labeling_revisions.w_cache.nettrom_30k.json

tuning_reports/enwiki.nettrom_wp10.md: \
		datasets/enwiki.labeling_revisions.w_cache.nettrom_30k.json
	cat datasets/enwiki.labeling_revisions.w_cache.nettrom_30k.json | \
	revscoring tune \
	  config/classifiers.params.yaml \
	  wikiclass.feature_lists.enwiki.wp10 \
	  wp10 \
	  --cv-timeout=60 \
	  --scoring=accuracy \
	  --debug \
	  --label-type=str > \
	tuning_reports/enwiki.nettrom_wp10.md

models/enwiki.nettrom_wp10.gradient_boosting.model: \
		datasets/enwiki.labeling_revisions.w_cache.nettrom_30k.json
	cat datasets/enwiki.labeling_revisions.w_cache.nettrom_30k.json | \
	revscoring cv_train \
	  revscoring.scorer_models.GradientBoosting \
	  wikiclass.feature_lists.enwiki.wp10 \
	  wp10 \
	  --version $(wp10_major_minor).0 \
	  -p 'n_estimators=700' \
	  -p 'learning_rate=0.01' \
	  -p 'max_features="log2"' \
	  -p 'max_depth=7' \
	  $(test_statistics) \
	  --balance-sample \
	  --center --scale > \
	models/enwiki.nettrom_wp10.gradient_boosting.model

enwiki_models: \
	models/enwiki.nettrom_wp10.gradient_boosting.model

enwiki_tuning_reports: \
	tuning_reports/enwiki.wp10.md \
	tuning_reports/enwiki.nettrom_wp10.md

########################## French Wikipedia ###################################
#datasets/frwiki.observations.first_labelings.20150602.json:
#	./utility extract_labelings \
#		/mnt/data/xmldatadumps/public/frwiki/20150602/frwiki-20150602-pages-meta-history*.xml*.bz2 > \
#	datasets/frwiki.observations.first_labelings.20150602.json

datasets/frwiki.labelings.20151202.json:
	./utility extract_labelings \
	  /mnt/data/xmldatadumps/public/frwiki/20151202/frwiki-20151202-pages-meta-history*.xml*.bz2 > \
	datasets/frwiki.labelings.20151202.json


datasets/frwiki.labelings.9k.json: \
		datasets/frwiki.labelings.20151202.json
	( \
	  grep -P '"wp10": "e"' datasets/frwiki.labelings.20151202.json | \
	  shuf -n 1500; \
	  grep -P '"wp10": "bd"' datasets/frwiki.labelings.20151202.json | \
	  shuf -n 1500; \
	  grep -P '"wp10": "b"' datasets/frwiki.labelings.20151202.json | \
	  shuf -n 1500; \
	  grep -P '"wp10": "a"' datasets/frwiki.labelings.20151202.json | \
	  shuf -n 1500; \
	  grep -P '"wp10": "ba"' datasets/frwiki.labelings.20151202.json | \
	  shuf -n 1500; \
	  grep -P '"wp10": "adq"' datasets/frwiki.labelings.20151202.json | \
	  shuf -n 1500 \
	) | \
	shuf > \
	datasets/frwiki.labelings.9k.json

datasets/frwiki.labeling_revisions.w_text.9k.json: \
		datasets/frwiki.labelings.9k.json
	cat datasets/frwiki.labelings.9k.json | \
	./utility fetch_text \
	  --api-host=https://fr.wikipedia.org \
	  --verbose > \
	datasets/frwiki.labeling_revisions.w_text.9k.json

datasets/frwiki.labeling_revisions.w_cache.9k.json: \
		datasets/frwiki.labeling_revisions.w_text.9k.json
	cat datasets/frwiki.labeling_revisions.w_text.9k.json | \
	./utility extract_from_text \
	  wikiclass.feature_lists.frwiki.wp10 \
	  --verbose > \
	datasets/frwiki.labeling_revisions.w_cache.9k.json

tuning_reports/frwiki.wp10.md: \
		datasets/frwiki.labeling_revisions.w_cache.9k.json
	cat datasets/frwiki.labeling_revisions.w_cache.9k.json | \
	revscoring tune \
	  config/classifiers.params.yaml \
	  wikiclass.feature_lists.frwiki.wp10 \
	  wp10 \
	  --cv-timeout=60 \
	  --scoring=accuracy \
	  --debug \
	  --label-type=str > \
	tuning_reports/frwiki.wp10.md

models/frwiki.wp10.gradient_boosting.model: \
		datasets/frwiki.labeling_revisions.w_cache.9k.json
	cat datasets/frwiki.labeling_revisions.w_cache.9k.json | \
	revscoring cv_train \
	  revscoring.scorer_models.GradientBoosting \
	  wikiclass.feature_lists.frwiki.wp10 \
	  wp10 \
	  --version $(wp10_major_minor).0 \
	  -p 'learning_rate=0.01' \
	  -p 'max_features="log2"' \
	  -p 'n_estimators=100' \
	  -p 'max_depth=7' \
	  $(test_statistics) \
	  --balance-sample \
	  --center --scale > \
	models/frwiki.wp10.gradient_boosting.model

frwiki_models: \
	models/frwiki.wp10.gradient_boosting.model

frwiki_tuning_reports: \
	tuning_reports/frwiki.wp10.md


########################## Russian Wikipedia ###################################
datasets/ruwiki.labelings.20160501.json:
	./utility extract_labelings \
		/mnt/data/xmldatadumps/public/ruwiki/20160501/ruwiki-20160501-pages-meta-history*.xml*.bz2 > \
	datasets/ruwiki.labelings.20160501.json

datasets/ruwiki.labelings.8k.json: \
	datasets/ruwiki.labelings.20160501.json
	( \
	  grep -P '"wp10": "I"' datasets/ruwiki.labelings.20160501.json | \
	  shuf -n 1155; \
	  grep -P '"wp10": "II"' datasets/ruwiki.labelings.20160501.json | \
	  shuf -n 1155; \
	  grep -P '"wp10": "III"' datasets/ruwiki.labelings.20160501.json | \
	  shuf -n 1155; \
	  grep -P '"wp10": "IV"' datasets/ruwiki.labelings.20160501.json | \
	  shuf -n 1155; \
	  grep -P '"wp10": "ДС"' datasets/ruwiki.labelings.20160501.json | \
	  shuf -n 1155; \
	  grep -P '"wp10": "ХС"' datasets/ruwiki.labelings.20160501.json | \
	  shuf -n 1155; \
	  grep -P '"wp10": "ИС"' datasets/ruwiki.labelings.20160501.json | \
	  shuf -n 1155 \
	) | \
	shuf > \
	datasets/ruwiki.labelings.8k.json

datasets/ruwiki.labeling_revisions.w_text.8k.json: \
		datasets/ruwiki.labelings.8k.json
	cat datasets/ruwiki.labelings.8k.json | \
	./utility fetch_text \
	  --api-host=https://ru.wikipedia.org \
	  --verbose > \
	datasets/ruwiki.labeling_revisions.w_text.8k.json

datasets/ruwiki.labeling_revisions.w_cache.8k.json: \
		datasets/ruwiki.labeling_revisions.w_text.8k.json
	cat datasets/ruwiki.labeling_revisions.w_text.8k.json | \
	./utility extract_from_text \
	  wikiclass.feature_lists.ruwiki.wp10 \
	  --verbose > \
	datasets/ruwiki.labeling_revisions.w_cache.8k.json

tuning_reports/ruwiki.wp10.md: \
		datasets/ruwiki.labeling_revisions.w_cache.8k.json
	cat datasets/ruwiki.labeling_revisions.w_cache.8k.json | \
	revscoring tune \
	  config/classifiers.params.yaml \
	  wikiclass.feature_lists.ruwiki.wp10 \
	  wp10 \
	  --cv-timeout=60 \
	  --scoring=accuracy \
	  --debug \
	  --label-type=str > \
	tuning_reports/ruwiki.wp10.md

models/ruwiki.wp10.gradient_boosting.model: \
		datasets/ruwiki.labeling_revisions.w_cache.8k.json
	cat datasets/ruwiki.labeling_revisions.w_cache.8k.json | \
	revscoring cv_train \
	  revscoring.scorer_models.GradientBoosting \
	  wikiclass.feature_lists.ruwiki.wp10 \
	  wp10 \
	  --version $(wp10_major_minor).0 \
	  -p 'max_depth=5' \
	  -p 'learning_rate=0.01' \
	  -p 'max_features="log2"' \
	  -p 'n_estimators=300' \
	  $(test_statistics) \
	  --balance-sample \
	  --center --scale > \
	models/ruwiki.wp10.gradient_boosting.model

ruwiki_models: \
	models/ruwiki.wp10.gradient_boosting.model

riwiki_tuning_reports: \
	tuning_reports/ruwiki.wp10.md


##############################################################################
################### Wikidata

# From https://quarry.wmflabs.org/query/17904
datasets/wikidatawiki.stratified_revisions.filtered_sample.json:
	wget https://quarry.wmflabs.org/run/167696/output/0/json-lines?download=true -qO- | \
	./utility fetch_item_info --api-host https://wikidata.org --claim P31 --verbose | \
	grep -v '"P31": "Q4167410"' | \
	grep -v '"P31": "Q4167836"' | \
	grep -v '"P31": "Q17633526"' | \
	grep -v '"P31": "Q11266439"' | \
	grep -v '"P31": "Q13406463"' > \
	datasets/wikidatawiki.stratified_revisions.filtered_sample.json


datasets/wikidatawiki.stratified_revisions.5k_sample.json: \
		datasets/wikidatawiki.stratified_revisions.filtered_sample.json
	( \
	  cat datasets/wikidatawiki.stratified_revisions.filtered_sample.json | \
	  grep '"strata": "1024"' | shuf -n 1000; \
	  cat datasets/wikidatawiki.stratified_revisions.filtered_sample.json | \
	  grep '"strata": "8192"' | shuf -n 1000; \
	  cat datasets/wikidatawiki.stratified_revisions.filtered_sample.json | \
	  grep '"strata": "131072"' | shuf -n 1000; \
	  cat datasets/wikidatawiki.stratified_revisions.filtered_sample.json | \
	  grep '"strata": "262144"' | shuf -n 250; \
	  cat datasets/wikidatawiki.stratified_revisions.filtered_sample.json | \
	  grep '"strata": "inf"' | shuf -n 250; \
	  cat datasets/wikidatawiki.stratified_revisions.filtered_sample.json | \
	  grep '"strata": "low-qid"' | shuf -n 1500 \
	) > datasets/wikidatawiki.stratified_revisions.5k_sample.json
