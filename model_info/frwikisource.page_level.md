Model Information:
	 - type: GradientBoosting
	 - version: 0.3.0
	 - params: {'random_state': None, 'warm_start': False, 'subsample': 1.0, 'labels': ['validated', 'not_proofread', 'proofread', 'without_text'], 'multilabel': False, 'init': None, 'presort': 'auto', 'max_leaf_nodes': None, 'scale': True, 'min_impurity_decrease': 0.0, 'verbose': 0, 'min_weight_fraction_leaf': 0.0, 'center': True, 'criterion': 'friedman_mse', 'min_impurity_split': None, 'n_estimators': 700, 'label_weights': None, 'min_samples_leaf': 1, 'learning_rate': 0.01, 'population_rates': None, 'min_samples_split': 2, 'loss': 'deviance', 'max_depth': 7, 'max_features': 'log2'}
	Environment:
	 - revscoring_version: '2.3.3'
	 - platform: 'Linux-4.9.0-8-amd64-x86_64-with-debian-9.5'
	 - machine: 'x86_64'
	 - version: '#1 SMP Debian 4.9.110-3+deb9u6 (2018-10-08)'
	 - system: 'Linux'
	 - processor: ''
	 - python_build: ('default', 'Jan 19 2017 14:11:04')
	 - python_compiler: 'GCC 6.3.0 20170118'
	 - python_branch: ''
	 - python_implementation: 'CPython'
	 - python_revision: ''
	 - python_version: '3.5.3'
	 - release: '4.9.0-8-amd64'
	
	Statistics:
	counts (n=20000):
		label               n         ~validated    ~not_proofread    ~proofread    ~without_text
		---------------  ----  ---  ------------  ----------------  ------------  ---------------
		'validated'      5000  -->          3372               546          1068               14
		'not_proofread'  5000  -->           868              3384           680               68
		'proofread'      5000  -->          1669               608          2708               15
		'without_text'   5000  -->            50               123            13             4814
	rates:
		              'validated'    'not_proofread'    'proofread'    'without_text'
		----------  -------------  -----------------  -------------  ----------------
		sample              0.25               0.25           0.25              0.25
		population          0.173              0.499          0.296             0.032
	match_rate (micro=0.308, macro=0.23):
		  validated    proofread    without_text    not_proofread
		-----------  -----------  --------------  ---------------
		      0.259        0.243           0.037            0.381
	filter_rate (micro=0.692, macro=0.77):
		  validated    proofread    without_text    not_proofread
		-----------  -----------  --------------  ---------------
		      0.741        0.757           0.963            0.619
	recall (micro=0.645, macro=0.714):
		  validated    proofread    without_text    not_proofread
		-----------  -----------  --------------  ---------------
		      0.674        0.542           0.963            0.677
	!recall (micro=0.893, macro=0.905):
		  validated    proofread    without_text    not_proofread
		-----------  -----------  --------------  ---------------
		      0.828        0.883           0.994            0.915
	precision (micro=0.743, macro=0.707):
		  validated    proofread    without_text    not_proofread
		-----------  -----------  --------------  ---------------
		      0.449         0.66            0.83            0.888
	!precision (micro=0.804, macro=0.871):
		  validated    proofread    without_text    not_proofread
		-----------  -----------  --------------  ---------------
		      0.924        0.821           0.999            0.739
	f1 (micro=0.681, macro=0.698):
		  validated    proofread    without_text    not_proofread
		-----------  -----------  --------------  ---------------
		      0.539        0.595           0.891            0.768
	!f1 (micro=0.843, macro=0.884):
		  validated    proofread    without_text    not_proofread
		-----------  -----------  --------------  ---------------
		      0.873         0.85           0.996            0.818
	accuracy (micro=0.799, macro=0.843):
		  validated    proofread    without_text    not_proofread
		-----------  -----------  --------------  ---------------
		      0.801        0.782           0.993            0.796
	fpr (micro=0.107, macro=0.095):
		  validated    proofread    without_text    not_proofread
		-----------  -----------  --------------  ---------------
		      0.172        0.117           0.006            0.085
	roc_auc (micro=0.887, macro=0.904):
		  validated    proofread    without_text    not_proofread
		-----------  -----------  --------------  ---------------
		      0.866        0.853           0.989            0.907
	pr_auc (micro=0.793, macro=0.778):
		  validated    proofread    without_text    not_proofread
		-----------  -----------  --------------  ---------------
		      0.545        0.725           0.934            0.909
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'probability': {'type': 'object', 'properties': {'validated': {'type': 'number'}, 'proofread': {'type': 'number'}, 'without_text': {'type': 'number'}, 'not_proofread': {'type': 'number'}}, 'description': 'A mapping of probabilities onto each of the potential output labels'}, 'prediction': {'type': 'string', 'description': 'The most likely label predicted by the estimator'}}}

