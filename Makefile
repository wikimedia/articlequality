datasets/enwiki.observations.first_labelings.20150602.tsv:
	wikilabels extract_labelings \
		/mnt/xmldumps/public/enwiki/20150602/enwiki-20150602-pages-meta-history*.xml*.bz2 \
		--extractor=enwiki > \
	datasets/enwiki.observations.first_labelings.20150602.tsv

datasets/enwiki.observations.first_labelings.30k.tsv: \
		datasets/enwiki.first_labelings.20150602.tsv
	( \
		grep -P '"label": "Stub"' datasets/enwiki.first_labelings.20150602.tsv | \
		shuf -n 5000; \
		grep -P '"label": "Start"' datasets/enwiki.first_labelings.20150602.tsv | \
		shuf -n 5000; \
		grep -P '"label": "C"' datasets/enwiki.first_labelings.20150602.tsv | \
		shuf -n 5000; \
		grep -P '"label": "B"' datasets/enwiki.first_labelings.20150602.tsv | \
		shuf -n 5000; \
		grep -P '"label": "GA"' datasets/enwiki.first_labelings.20150602.tsv | \
		shuf -n 5000; \
		grep -P '"label": "FA"' datasets/enwiki.first_labelings.20150602.tsv | \
		shuf -n 5000 \
	) | \
	shuf >
	datasets/enwiki.observations.first_labelings.30k.tsv

datasets/enwiki.observations.text_wp10.30k.tsv: \
		datasets/enwiki.observations.first_labelings.30k.tsv
	cat datasets/enwiki.first_labelings.30k.tsv | \
	wikilabels fetch_text \
		--api=https://en.wikipedia.org/w/api.php > \
	datasets/enwiki.observations.text_wp10.30k.tsv

datasets/enwiki.features_wp10.30k.tsv: \
		datasets/enwiki.observations.text_wp10.30k.tsv
	cat datasets/enwiki.observations.text_wp10.30k.tsv | \
	wikilabels extract_features \
		feature_lists.enwiki.wp10 \
		--language=revscoring.languages.english > \
	datasets/enwiki.features_wp10.30k.tsv

models/enwiki.wp10.rf.model: datasets/enwiki.features_wp10.30k.tsv
	cat datasets/enwiki.features_wp10.30k.tsv | \
	revscoring train_test \
		revscoring.scorer_models.RFModel \
		feature_lists.enwiki.wp10 \
		revscoring.languages.english \
		-p 'n_estimators=501' \
		-p 'min_samples_leaf=8' \
		--version=0.1.0 > \
	models/enwiki.wp10.rf.model
#Based on work by Nettrom[1] and with a few improvements and extensions.
#
#1. Warncke-Wang, M., Cosley, D., & Riedl, J. (2013, August). Tell me more: An
#   actionable quality model for wikipedia. In Proceedings of the 9th
#   International Symposium on Open Collaboration (p. 8). ACM.
#   http://opensym.org/wsos2013/proceedings/p0202-warncke.pdf
