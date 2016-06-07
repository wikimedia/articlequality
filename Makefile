models: \
	enwiki_models \
	frwiki_models

tuning_reports: \
	enwiki_tuning_reports \
	frwiki_tuning_reports

test_statistics = -s 'table' -s 'accuracy' -s 'roc' -s 'f1'

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
		--version 0.3.1 \
		-p 'n_estimators=501' \
		-p 'min_samples_leaf=8' \
		$(test_statistics) \
		--balance-sample \
		--center --scale > \
	models/enwiki.wp10.rf.model

datasets/enwiki.features_wp10.nettrom_30k.tsv: \
		datasets/enwiki.rev_wp10.nettrom_30k.tsv
	cat datasets/enwiki.rev_wp10.nettrom_30k.tsv | \
	revscoring extract_features \
		wikiclass.feature_lists.enwiki.wp10 \
		--host https://en.wikipedia.org \
		--include-revid \
		--verbose > \
	datasets/enwiki.features_wp10.nettrom_30k.tsv

tuning_reports/enwiki.nettrom_wp10.md: datasets/enwiki.features_wp10.nettrom_30k.tsv
	cat datasets/enwiki.features_wp10.nettrom_30k.tsv | cut -f2- | \
	revscoring tune \
		config/classifiers.params.yaml \
		wikiclass.feature_lists.enwiki.wp10 \
		--cv-timeout=60 \
		--scoring=accuracy \
		--debug \
		--label-type=str > \
	tuning_reports/enwiki.nettrom_wp10.md

models/enwiki.nettrom_wp10.rf.model: datasets/enwiki.features_wp10.nettrom_30k.tsv
	cat datasets/enwiki.features_wp10.nettrom_30k.tsv | cut -f2- | \
	revscoring train_test \
		revscoring.scorer_models.RF \
		wikiclass.feature_lists.enwiki.wp10 \
		--version 0.3.1 \
		-p 'criterion="entropy"' \
		-p 'n_estimators=320' \
		-p 'min_samples_leaf=8' \
		-p 'max_features="log2"' \
		$(test_statistics) \
		--balance-sample \
		--center --scale > \
	models/enwiki.nettrom_wp10.rf.model

enwiki_models: \
	models/enwiki.nettrom_wp10.rf.model

enwiki_tuning_reports: \
	tuning_reports/enwiki.wp10.md \
	tuning_reports/enwiki.nettrom_wp10.md

########################## French Wikipedia ###################################
#datasets/frwiki.observations.first_labelings.20150602.tsv:
#	./utility extract_labelings \
#		/mnt/data/xmldatadumps/public/frwiki/20150602/frwiki-20150602-pages-meta-history*.xml*.bz2 > \
#	datasets/frwiki.observations.first_labelings.20150602.tsv

datasets/frwiki.observations.first_labelings.20151202.tsv:
	./utility extract_labelings \
		/mnt/data/xmldatadumps/public/frwiki/20151202/frwiki-20151202-pages-meta-history*.xml*.bz2 > \
	datasets/frwiki.observations.first_labelings.20151202.tsv


datasets/frwiki.observations.first_labelings.9k.tsv: \
		datasets/frwiki.observations.first_labelings.20151202.tsv
	( \
		grep -P '"label": "e"' datasets/frwiki.observations.first_labelings.20151202.tsv | \
		shuf -n 1500; \
		grep -P '"label": "bd"' datasets/frwiki.observations.first_labelings.20151202.tsv | \
		shuf -n 1500; \
		grep -P '"label": "b"' datasets/frwiki.observations.first_labelings.20151202.tsv | \
		shuf -n 1500; \
		grep -P '"label": "a"' datasets/frwiki.observations.first_labelings.20151202.tsv | \
		shuf -n 1500; \
		grep -P '"label": "ba"' datasets/frwiki.observations.first_labelings.20151202.tsv | \
		shuf -n 1500; \
		grep -P '"label": "adq"' datasets/frwiki.observations.first_labelings.20151202.tsv | \
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
		revscoring.scorer_models.RF \
		wikiclass.feature_lists.frwiki.wp10 \
		--version 0.2.0 \
		-p 'n_estimators=501' \
		-p 'min_samples_leaf=8' \
		$(test_statistics) \
		--balance-sample \
		--center --scale > \
	models/frwiki.wp10.rf.model

frwiki_models: \
	models/frwiki.wp10.rf.model

frwiki_tuning_reports: \
	tuning_reports/frwiki.wp10.md


########################## Russian Wikipedia ###################################
datasets/ruwiki.observations.first_labelings.20160501.json:
	./utility extract_labelings \
		/mnt/data/xmldatadumps/public/ruwiki/20160501/ruwiki-20160501-pages-meta-history*.xml*.bz2 > \
	datasets/ruwiki.observations.first_labelings.20160501.json

datasets/ruwiki.observations.first_labelings.8k.json: \
	datasets/ruwiki.observations.first_labelings.20160501.json
	( \
		grep -P '"label": "I"' datasets/ruwiki.observations.first_labelings.20160501.json | \
		shuf -n 1155; \
		grep -P '"label": "II"' datasets/ruwiki.observations.first_labelings.20160501.json | \
		shuf -n 1155; \
		grep -P '"label": "III"' datasets/ruwiki.observations.first_labelings.20160501.json | \
		shuf -n 1155; \
		grep -P '"label": "IV"' datasets/ruwiki.observations.first_labelings.20160501.json | \
		shuf -n 1155; \
		grep -P '"label": "sa"' datasets/ruwiki.observations.first_labelings.20160501.json | \
		shuf -n 1155; \
		grep -P '"label": "ga"' datasets/ruwiki.observations.first_labelings.20160501.json | \
		shuf -n 1155; \
		grep -P '"label": "fa"' datasets/ruwiki.observations.first_labelings.20160501.json | \
		shuf -n 1155 \
	) | \
	shuf > \
	datasets/ruwiki.observations.first_labelings.8k.json

datasets/ruwiki.observations.text_wp10.8k.json: \
		datasets/ruwiki.observations.first_labelings.8k.json
	cat datasets/ruwiki.observations.first_labelings.8k.json | \
        ./utility fetch_text \
                --api-host=https://ru.wikipedia.org \
                --verbose > \
        datasets/ruwiki.observations.text_wp10.8k.json

datasets/ruwiki.features_wp10.8k.tsv: \
		datasets/ruwiki.observations.text_wp10.8k.json
	cat datasets/ruwiki.observations.text_wp10.8k.json | \
        ./utility extract_features \
                wikiclass.feature_lists.ruwiki.wp10 \
                --verbose > \
        datasets/ruwiki.features_wp10.8k.tsv

tuning_reports/ruwiki.wp10.md: datasets/ruwiki.features_wp10.8k.tsv
	cat datasets/ruwiki.features_wp10.8k.tsv | \
        revscoring tune \
                config/classifiers.params.yaml \
                wikiclass.feature_lists.ruwiki.wp10 \
                --cv-timeout=60 \
                --scoring=accuracy \
                --debug \
                --label-type=str > \
        tuning_reports/ruwiki.wp10.md

models/ruwiki.wp10.rf.model: datasets/ruwiki.features_wp10.8k.tsv
	cat datasets/ruwiki.features_wp10.8k.tsv | \
        revscoring train_test \
                revscoring.scorer_models.RF \
                wikiclass.feature_lists.ruwiki.wp10 \
                --version 0.0.1 \
                -p 'n_estimators=501' \
                -p 'min_samples_leaf=8' \
                $(test_statistics) \
                --balance-sample \
                --center --scale > \
        models/ruwiki.wp10.rf.model
