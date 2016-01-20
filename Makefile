all_models:
	enwiki_models \
	frwiki_models

########################## English Wikipedia ###################################
datasets/enwiki.observations.first_labelings.20150602.tsv:
	./utility extract_labelings \
		/mnt/data/xmldatadumps/public/enwiki/20150602/enwiki-20150602-pages-meta-history*.xml*.bz2 \
		--verbose > \
	datasets/enwiki.observations.first_labelings.20150602.tsv


datasets/enwiki.observations.first_labelings.30k.tsv: \
		datasets/enwiki.observations.first_labelings.20150602.tsv
	( \
		grep -P '"label": "stub"' datasets/enwiki.observations.first_labelings.20150602.tsv | \
		shuf -n 5000; \
		grep -P '"label": "start"' datasets/enwiki.observations.first_labelings.20150602.tsv | \
		shuf -n 5000; \
		grep -P '"label": "c"' datasets/enwiki.observations.first_labelings.20150602.tsv | \
		shuf -n 5000; \
		grep -P '"label": "b"' datasets/enwiki.observations.first_labelings.20150602.tsv | \
		shuf -n 5000; \
		grep -P '"label": "ga"' datasets/enwiki.observations.first_labelings.20150602.tsv | \
		shuf -n 5000; \
		grep -P '"label": "fa"' datasets/enwiki.observations.first_labelings.20150602.tsv | \
		shuf -n 5000 \
	) | \
	shuf > \
	datasets/enwiki.observations.first_labelings.30k.tsv

datasets/enwiki.observations.text_wp10.30k.tsv: \
		datasets/enwiki.observations.first_labelings.30k.tsv
	cat datasets/enwiki.observations.first_labelings.30k.tsv | \
	./utility fetch_text \
		--api-host=https://en.wikipedia.org \
		--verbose > \
	datasets/enwiki.observations.text_wp10.30k.tsv

datasets/enwiki.features_wp10.30k.tsv: \
		datasets/enwiki.observations.text_wp10.30k.tsv
	cat datasets/enwiki.observations.text_wp10.30k.tsv | \
	./utility extract_features \
		wikiclass.feature_lists.enwiki.wp10 \
		--verbose > \
	datasets/enwiki.features_wp10.30k.tsv

tuning_reports/enwiki.wp10.md: datasets/enwiki.features_wp10.30k.tsv
	cat datasets/enwiki.features_wp10.30k.tsv | \
	revscoring tune \
		config/classifiers.params.yaml \
		wikiclass.feature_lists.enwiki.wp10 \
		--cv-timeout=60 \
		--scoring=accuracy \
		--debug \
		--label-type=str > \
	tuning_reports/enwiki.wp10.md

models/enwiki.wp10.rf.model: datasets/enwiki.features_wp10.30k.tsv
	cat datasets/enwiki.features_wp10.30k.tsv | \
	revscoring train_test \
		revscoring.scorer_models.RF \
		wikiclass.feature_lists.enwiki.wp10 \
		-p 'n_estimators=501' \
		-p 'min_samples_leaf=8' \
		--version=0.2.1 > \
	models/enwiki.wp10.rf.model

enwiki_models:
	models/enwiki.wp10.rf.model

########################## French Wikipedia ###################################
datasets/frwiki.observations.first_labelings.20150602.tsv:
	./utility extract_labelings \
		/mnt/data/xmldatadumps/public/frwiki/20150602/frwiki-20150602-pages-meta-history*.xml*.bz2 > \
	datasets/frwiki.observations.first_labelings.20150602.tsv

datasets/frwiki.observations.first_labelings.9k.tsv: \
		datasets/frwiki.observations.first_labelings.20150602.tsv
	( \
		grep -P '"label": "e"' datasets/frwiki.observations.first_labelings.20150602.tsv | \
		shuf -n 1500; \
		grep -P '"label": "bd"' datasets/frwiki.observations.first_labelings.20150602.tsv | \
		shuf -n 1500; \
		grep -P '"label": "b"' datasets/frwiki.observations.first_labelings.20150602.tsv | \
		shuf -n 1500; \
		grep -P '"label": "a"' datasets/frwiki.observations.first_labelings.20150602.tsv | \
		shuf -n 1500; \
		grep -P '"label": "ba"' datasets/frwiki.observations.first_labelings.20150602.tsv | \
		shuf -n 1500; \
		grep -P '"label": "adq"' datasets/frwiki.observations.first_labelings.20150602.tsv | \
		shuf -n 1500 \
	) | \
	shuf > \
	datasets/frwiki.observations.first_labelings.9k.tsv

datasets/frwiki.observations.text_wp10.9k.tsv: \
		datasets/frwiki.observations.first_labelings.9k.tsv
	cat datasets/frwiki.observations.first_labelings.9k.tsv | \
	./utility fetch_text \
                --api-host=https://fr.wikipedia.org \
                --verbose > \
	datasets/frwiki.observations.text_wp10.9k.tsv

datasets/frwiki.features_wp10.9k.tsv: \
		datasets/frwiki.observations.text_wp10.9k.tsv
	cat datasets/frwiki.observations.text_wp10.9k.tsv | \
	./utility extract_features \
		wikiclass.feature_lists.frwiki.wp10 \
		--verbose > \
	datasets/frwiki.features_wp10.9k.tsv

tuning_reports/frwiki.wp10.md: datasets/frwiki.features_wp10.9k.tsv
	cat datasets/frwiki.features_wp10.9k.tsv | \
	revscoring tune \
		config/classifiers.params.yaml \
		wikiclass.feature_lists.frwiki.wp10 \
		--cv-timeout=60 \
		--scoring=accuracy \
		--debug \
		--label-type=str > \
	tuning_reports/frwiki.wp10.md

models/frwiki.wp10.rf.model: datasets/frwiki.features_wp10.9k.tsv
	cat datasets/frwiki.features_wp10.9k.tsv | \
	revscoring train_test \
		revscoring.scorer_models.RFModel \
		wikiclass.feature_lists.frwiki.wp10 \
		-p 'n_estimators=501' \
		-p 'min_samples_leaf=8' \
		--version=0.1.0 > \
	models/frwiki.wp10.rf.model

frwiki_models:
	models/enwiki.wp10.rf.model
