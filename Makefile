# Remove target files after command failure.    
.DELETE_ON_ERROR:      

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
item_quality_major_minor = 0.1

########################## English Wikipedia ###################################
datasets/enwiki.labelings.20150602.json:
	./utility extract_labelings \
	  /mnt/data/xmldatadumps/public/enwiki/20150602/enwiki-20150602-pages-meta-history*.xml*.bz2 \
	  --verbose > $@


datasets/enwiki.labelings.30k.json: \
		datasets/enwiki.labelings.20150602.json
	( \
	  grep -P '"wp10": "stub"' $< | \
	  shuf -n 5000; \
	  grep -P '"wp10": "start"' $< | \
	  shuf -n 5000; \
	  grep -P '"wp10": "c"' $< | \
	  shuf -n 5000; \
	  grep -P '"wp10": "b"' $< | \
	  shuf -n 5000; \
	  grep -P '"wp10": "ga"' $< | \
	  shuf -n 5000; \
	  grep -P '"wp10": "fa"' $< | \
	  shuf -n 5000 \
	) | \
	shuf > $@

datasets/enwiki.labeling_revisions.w_text.30k.json: \
		datasets/enwiki.labelings.30k.json
	cat $< | \
	./utility fetch_text \
	  --api-host=https://en.wikipedia.org \
	  --verbose > $@

datasets/enwiki.labeling_revisions.w_cache.30k.json: \
		datasets/enwiki.labeling_revisions.w_text.30k.json
	cat $< | \
	./utility extract_from_text \
	  wikiclass.feature_lists.enwiki.wp10 \
	  --verbose > $@

tuning_reports/enwiki.wp10.md: \
		datasets/enwiki.labeling_revisions.w_cache.30k.json
	cat $< | \
	revscoring tune \
	  config/classifiers.params.yaml \
	  wikiclass.feature_lists.enwiki.wp10 \
	  wp10 \
	  --cv-timeout=60 \
	  --scoring=accuracy \
	  --debug \
	  --label-type=str > $@

models/enwiki.wp10.rf.model: \
		datasets/enwiki.labeling_revisions.w_cache.30k.json
	cat $< | \
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
	  --center --scale > $@

datasets/enwiki.labeling_revisions.w_cache.nettrom_30k.json: \
		datasets/enwiki.labeling_revisions.nettrom_30k.json
	cat $< | \
	revscoring extract \
	  wikiclass.feature_lists.enwiki.wp10 \
	  --host https://en.wikipedia.org \
	  --verbose > $@

tuning_reports/enwiki.nettrom_wp10.md: \
		datasets/enwiki.labeling_revisions.w_cache.nettrom_30k.json
	cat $< | \
	revscoring tune \
	  config/classifiers.params.yaml \
	  wikiclass.feature_lists.enwiki.wp10 \
	  wp10 \
	  --cv-timeout=60 \
	  --scoring=accuracy \
	  --debug \
	  --label-type=str > $@

models/enwiki.nettrom_wp10.gradient_boosting.model: \
		datasets/enwiki.labeling_revisions.w_cache.nettrom_30k.json
	cat $< | \
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
	  --center --scale > $@

enwiki_models: \
	models/enwiki.nettrom_wp10.gradient_boosting.model

enwiki_tuning_reports: \
	tuning_reports/enwiki.wp10.md \
	tuning_reports/enwiki.nettrom_wp10.md

########################## French Wikipedia ###################################
#datasets/frwiki.observations.first_labelings.20150602.json:
#	./utility extract_labelings \
#		/mnt/data/xmldatadumps/public/frwiki/20150602/frwiki-20150602-pages-meta-history*.xml*.bz2 > $@

datasets/frwiki.labelings.20151202.json:
	./utility extract_labelings \
	  /mnt/data/xmldatadumps/public/frwiki/20151202/frwiki-20151202-pages-meta-history*.xml*.bz2 > $@


datasets/frwiki.labelings.9k.json: \
		datasets/frwiki.labelings.20151202.json
	( \
	  grep -P '"wp10": "e"' $< | \
	  shuf -n 1500; \
	  grep -P '"wp10": "bd"' $< | \
	  shuf -n 1500; \
	  grep -P '"wp10": "b"' $< | \
	  shuf -n 1500; \
	  grep -P '"wp10": "a"' $< | \
	  shuf -n 1500; \
	  grep -P '"wp10": "ba"' $< | \
	  shuf -n 1500; \
	  grep -P '"wp10": "adq"' $< | \
	  shuf -n 1500 \
	) | \
	shuf > $@

datasets/frwiki.labeling_revisions.w_text.9k.json: \
		datasets/frwiki.labelings.9k.json
	cat $< | \
	./utility fetch_text \
	  --api-host=https://fr.wikipedia.org \
	  --verbose > $@

datasets/frwiki.labeling_revisions.w_cache.9k.json: \
		datasets/frwiki.labeling_revisions.w_text.9k.json
	cat $< | \
	./utility extract_from_text \
	  wikiclass.feature_lists.frwiki.wp10 \
	  --verbose > $@


tuning_reports/frwiki.wp10.md: \
		datasets/frwiki.labeling_revisions.w_cache.9k.json
	cat $< | \
	revscoring tune \
	  config/classifiers.params.yaml \
	  wikiclass.feature_lists.frwiki.wp10 \
	  wp10 \
	  --cv-timeout=60 \
	  --scoring=accuracy \
	  --debug \
	  --label-type=str > $@

models/frwiki.wp10.gradient_boosting.model: \
		datasets/frwiki.labeling_revisions.w_cache.9k.json
	cat $< | \
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
	  --center --scale > $@

frwiki_models: \
	models/frwiki.wp10.gradient_boosting.model

frwiki_tuning_reports: \
	tuning_reports/frwiki.wp10.md

############################# French Wikisource ###############################

# TODO: Use: https://fr.wikisource.org/w/api.php?action=query&prop=revisions&revids=6515962&rvprop=content&rvcontentformat=application/json&formatversion=2

# https://quarry.wmflabs.org/query/18839
datasets/frwikisource.sampled_revisions.200k_2017.json:
	wget https://quarry.wmflabs.org/run/178341/output/0/json-lines?download=true -qO- > $@

datasets/frwikisource.sampled_revisions.with_text.200k_2017.json: \
		datasets/frwikisource.sampled_revisions.200k_2017.json
	cat $< | \
	revscoring fetch_text \
		--host=https://fr.wikisource.org \
		--verbose > $@

datasets/frwikisource.labeled_revisions.with_text.20k_balanced_2017.json: \
		datasets/frwikisource.sampled_revisions.with_text.200k_2017.json
	( \
	  cat $< | \
	  grep 'level=\\"4\\"' | shuf -n 5000 | sed -r 's/"rev_id"/"page_level": "4", "rev_id"/'; \
          cat $< | \
          grep 'level=\\"3\\"' | shuf -n 5000 | sed -r 's/"rev_id"/"page_level": "3", "rev_id"/'; \
          cat $< | \
          grep 'level=\\"1\\"' | shuf -n 5000 | sed -r 's/"rev_id"/"page_level": "1", "rev_id"/'; \
          cat $< | \
          grep 'level=\\"0\\"' | shuf -n 5000 | sed -r 's/"rev_id"/"page_level": "0", "rev_id"/' \
	) > $@

datasets/frwikisource.labeled_revisions.w_cache.20k_balanced_2017.json: \
		datasets/frwikisource.labeled_revisions.with_text.20k_balanced_2017.json
	cat $< | \
	./utility extract_from_text \
	  wikiclass.feature_lists.frwikisource.pagelevel \
	  --verbose > $@

tuning_reports/frwikisource.page_level.md: \
		datasets/frwikisource.labeled_revisions.w_cache.20k_balanced_2017.json
	cat $< | \
	revscoring tune \
	  config/classifiers.params.yaml \
	  wikiclass.feature_lists.frwikisource.pagelevel \
	  page_level \
	  --cv-timeout=60 \
	  --scoring=accuracy \
	  --debug \
	  --label-type=str > $@

models/frwikisource.page_level.gradient_boosting.model: \
		datasets/frwikisource.labeled_revisions.w_cache.20k_balanced_2017.json
	cat $< | \
	revscoring cv_train \
	  revscoring.scorer_models.GradientBoosting \
	  wikiclass.feature_lists.frwikisource.pagelevel \
	  page_level \
	  --version 0.0.1 \
	  -p 'n_estimators=700' \
	  -p 'learning_rate=0.01' \
	  -p 'max_features="log2"' \
	  -p 'max_depth=7' \
	  $(test_statistics) \
	  --balance-sample \
	  --center --scale > $@


########################## Russian Wikipedia ###################################
datasets/ruwiki.labelings.20160501.json:
	./utility extract_labelings \
		/mnt/data/xmldatadumps/public/ruwiki/20160501/ruwiki-20160501-pages-meta-history*.xml*.bz2 > $@

datasets/ruwiki.labelings.8k.json: \
	datasets/ruwiki.labelings.20160501.json
	( \
	  grep -P '"wp10": "I"' $< | \
	  shuf -n 1155; \
	  grep -P '"wp10": "II"' $< | \
	  shuf -n 1155; \
	  grep -P '"wp10": "III"' $< | \
	  shuf -n 1155; \
	  grep -P '"wp10": "IV"' $< | \
	  shuf -n 1155; \
	  grep -P '"wp10": "ДС"' $< | \
	  shuf -n 1155; \
	  grep -P '"wp10": "ХС"' $< | \
	  shuf -n 1155; \
	  grep -P '"wp10": "ИС"' $< | \
	  shuf -n 1155 \
	) | \
	shuf > $@

datasets/ruwiki.labeling_revisions.w_text.8k.json: \
		datasets/ruwiki.labelings.8k.json
	cat $< | \
	./utility fetch_text \
	  --api-host=https://ru.wikipedia.org \
	  --verbose > $@

datasets/ruwiki.labeling_revisions.w_cache.8k.json: \
		datasets/ruwiki.labeling_revisions.w_text.8k.json
	cat $< | \
	./utility extract_from_text \
	  wikiclass.feature_lists.ruwiki.wp10 \
	  --verbose > $@

tuning_reports/ruwiki.wp10.md: \
		datasets/ruwiki.labeling_revisions.w_cache.8k.json
	cat $< | \
	revscoring tune \
	  config/classifiers.params.yaml \
	  wikiclass.feature_lists.ruwiki.wp10 \
	  wp10 \
	  --cv-timeout=60 \
	  --scoring=accuracy \
	  --debug \
	  --label-type=str > $@

models/ruwiki.wp10.gradient_boosting.model: \
		datasets/ruwiki.labeling_revisions.w_cache.8k.json
	cat $< | \
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
	  --center --scale > $@

ruwiki_models: \
	models/ruwiki.wp10.gradient_boosting.model

riwiki_tuning_reports: \
	tuning_reports/ruwiki.wp10.md


############################ Turkish Wikipedia #############################
datasets/trwiki.labelings.20170501.json:
	./utility extract_labelings \
		/mnt/data/xmldatadumps/public/trwiki/20170501/trwiki-20170501-pages-meta-history.xml.bz2 > \
	datasets/trwiki.labelings.20170501.json

datasets/trwiki.labelings.2k.json: \
		datasets/trwiki.labelings.20170501.json
	(cat $< | grep '"wp10": "taslak"' | shuf -n 272; \
	 cat $< | grep '"wp10": "baslag\\u0131\\u00e7"' | shuf -n 272; \
	 cat $< | grep '"wp10": "c"' | shuf -n 272; \
	 cat $< | grep '"wp10": "b"' | shuf -n 272; \
	 cat $< | grep '"wp10": "km"' | shuf -n 272; \
	 cat $< | grep '"wp10": "sm"' | shuf -n 272) > $@

datasets/trwiki.labeling_revisions.w_text.2k.json: \
		datasets/trwiki.labelings.2k.json
	cat $< | \
	./utility fetch_text \
	  --api-host=https://tr.wikipedia.org \
	  --verbose > $@

datasets/trwiki.labeling_revisions.w_cache.2k.json: \
		datasets/trwiki.labeling_revisions.w_text.2k.json
	cat $< | \
	./utility extract_from_text \
	  wikiclass.feature_lists.trwiki.wp10 \
	  --verbose > $@

tuning_reports/trwiki.wp10.md: \
		datasets/trwiki.labeling_revisions.w_cache.2k.json
	cat $< | \
	revscoring tune \
	  config/classifiers.params.yaml \
	  wikiclass.feature_lists.trwiki.wp10 \
	  wp10 \
	  --cv-timeout=60 \
	  --scoring=accuracy \
	  --debug \
	  --folds 20 \
	  --label-type=str > $@

max_depth=7, max_features="log2", n_estimators=300, learning_rate=0.1

models/trwiki.wp10.gradient_boosting.model: \
		datasets/trwiki.labeling_revisions.w_cache.2k.json
	cat $< | \
	revscoring cv_train \
	  revscoring.scorer_models.GradientBoosting \
	  wikiclass.feature_lists.trwiki.wp10 \
	  wp10 \
	  --version $(wp10_major_minor).0 \
	  -p 'max_depth=5' \
	  -p 'learning_rate=0.01' \
	  -p 'max_features="log2"' \
	  -p 'n_estimators=300' \
	  $(test_statistics) \
	  --balance-sample \
	  --center --scale > $@

############################# Wikidata ######################################

# From https://quarry.wmflabs.org/query/17904
datasets/wikidatawiki.stratified_revisions.filtered_sample.json:
	wget https://quarry.wmflabs.org/run/167696/output/0/json-lines?download=true -qO- | \
	./utility fetch_item_info --api-host https://wikidata.org --claim P31 --verbose | \
	grep -v '"P31": "Q4167410"' | \
	grep -v '"P31": "Q4167836"' | \
	grep -v '"P31": "Q17633526"' | \
	grep -v '"P31": "Q11266439"' | \
	grep -v '"P31": "Q13406463"' > $@


datasets/wikidatawiki.stratified_revisions.5k_sample.json: \
		datasets/wikidatawiki.stratified_revisions.filtered_sample.json
	( \
	  cat $< | \
	  grep '"strata": "1024"' | shuf -n 1000; \
	  cat $< | \
	  grep '"strata": "8192"' | shuf -n 1000; \
	  cat $< | \
	  grep '"strata": "131072"' | shuf -n 1000; \
	  cat $< | \
	  grep '"strata": "262144"' | shuf -n 250; \
	  cat $< | \
	  grep '"strata": "inf"' | shuf -n 250; \
	  cat $< | \
	  grep '"strata": "low-qid"' | shuf -n 1500 \
	) > $@

datasets/wikidatawiki.labelings.5k.json:
	./utility fetch_labels \
		https://labels.wmflabs.org/campaigns/wikidatawiki/53/ > $@

datasets/wikidatawiki.labeling_revisions.w_text.5k.json: \
		datasets/wikidatawiki.labelings.5k.json
	cat $< | \
	./utility fetch_text \
	  --api-host=https://www.wikidata.org \
	  --verbose > $@

datasets/wikidatawiki.labeling_revisions.w_cache.5k.json: \
		datasets/wikidatawiki.labeling_revisions.w_text.5k.json
	cat $< | \
	./utility extract_from_text \
	  wikiclass.feature_lists.wikidatawiki.item_quality \
	  --verbose > $@

tuning_reports/wikidatawiki.item_quality.md: \
		datasets/wikidatawiki.labeling_revisions.w_cache.5k.json
	cat $< | \
	revscoring tune \
	  config/classifiers.params.yaml \
	  wikiclass.feature_lists.wikidatawiki.item_quality \
	  item_quality \
	  --cv-timeout=60 \
	  --scoring=accuracy \
	  --debug \
	  --label-type=str > $@

models/wikidatawiki.item_quality.rf.model: \
		datasets/wikidatawiki.labeling_revisions.w_cache.5k.json
	cat $< | \
	revscoring cv_train \
	  revscoring.scorer_models.RF \
	  wikiclass.feature_lists.wikidatawiki.item_quality \
	  item_quality \
	  --version $(item_quality_major_minor).0 \
	  -p 'n_estimators=20' \
	  -p 'criterion="gini"' \
	  -p 'min_samples_leaf=13' \
	  -p 'max_features="log2"' \
	  $(test_statistics) \
	  --balance-sample \
	  --center --scale > $@

wikidatawiki_models: \
	models/wikidatawiki.item_quality.rf.model

wikidatawiki_tuning_reports: \
	tuning_reports/wikidatawiki.item_quality.md
