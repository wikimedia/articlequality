datasets/enwiki.observations.first_labelings.20150602.tsv:
	./utility extract_labelings \
		/mnt/data/xmldatadumps/public/enwiki/20150602/enwiki-20150602-pages-meta-history*.xml*.bz2 \
		--verbose > \
	datasets/enwiki.observations.first_labelings.20150602.tsv

datasets/frwiki.observations.first_labelings.20150602.tsv:
	./utility extract_labelings \
		/mnt/data/xmldatadumps/public/frwiki/20150602/frwiki-20150602-pages-meta-history*.xml*.bz2 > \
	datasets/frwiki.observations.first_labelings.20150602.tsv


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
		--api=https://en.wikipedia.org/w/api.php --verbose > \
	datasets/enwiki.observations.text_wp10.30k.tsv

datasets/enwiki.features_wp10.30k.tsv: \
		datasets/enwiki.observations.text_wp10.30k.tsv
	cat datasets/enwiki.observations.text_wp10.30k.tsv | \
	./utility extract_features \
		wikiclass.feature_lists.enwiki.wp10 \
		--language=revscoring.languages.english > \
	datasets/enwiki.features_wp10.30k.tsv

models/enwiki.wp10.rf.model: datasets/enwiki.features_wp10.30k.tsv
	cat datasets/enwiki.features_wp10.30k.tsv | \
	revscoring train_test \
		revscoring.scorer_models.RFModel \
		wikiclass.feature_lists.enwiki.wp10 \
		-p 'n_estimators=501' \
		-p 'min_samples_leaf=8' \
		--version=0.2.0 > \
	models/enwiki.wp10.rf.model
#Based on work by Nettrom[1] and with a few improvements and extensions.
#
#1. Warncke-Wang, M., Cosley, D., & Riedl, J. (2013, August). Tell me more: An
#   actionable quality model for wikipedia. In Proceedings of the 9th
#   International Symposium on Open Collaboration (p. 8). ACM.
#   http://opensym.org/wsos2013/proceedings/p0202-warncke.pdf
