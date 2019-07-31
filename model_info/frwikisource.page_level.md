Model Information:
	 - type: GradientBoosting
	 - version: 0.3.0
	 - params: {'population_rates': None, 'min_impurity_decrease': 0.0, 'n_iter_no_change': None, 'scale': True, 'max_features': 'log2', 'tol': 0.0001, 'labels': ['validated', 'not_proofread', 'proofread', 'without_text'], 'multilabel': False, 'init': None, 'validation_fraction': 0.1, 'n_estimators': 700, 'center': True, 'random_state': None, 'subsample': 1.0, 'max_depth': 7, 'criterion': 'friedman_mse', 'learning_rate': 0.01, 'min_weight_fraction_leaf': 0.0, 'warm_start': False, 'min_samples_split': 2, 'loss': 'deviance', 'presort': 'auto', 'label_weights': None, 'verbose': 0, 'min_samples_leaf': 1, 'min_impurity_split': None, 'max_leaf_nodes': None}
	Environment:
	 - revscoring_version: '2.5.1'
	 - platform: 'Linux-4.9.0-9-amd64-x86_64-with-debian-9.9'
	 - machine: 'x86_64'
	 - version: '#1 SMP Debian 4.9.168-1+deb9u2 (2019-05-13)'
	 - system: 'Linux'
	 - processor: ''
	 - python_build: ('default', 'Sep 27 2018 17:25:39')
	 - python_compiler: 'GCC 6.3.0 20170516'
	 - python_branch: ''
	 - python_implementation: 'CPython'
	 - python_revision: ''
	 - python_version: '3.5.3'
	 - release: '4.9.0-9-amd64'
	
	Statistics:
	counts (n=20000):
		label               n         ~validated    ~not_proofread    ~proofread    ~without_text
		---------------  ----  ---  ------------  ----------------  ------------  ---------------
		'validated'      5000  -->          3299               547          1136               18
		'not_proofread'  5000  -->           825              3510           600               65
		'proofread'      5000  -->          1613               611          2763               13
		'without_text'   5000  -->            59               127            17             4797
	rates:
		              'validated'    'not_proofread'    'proofread'    'without_text'
		----------  -------------  -----------------  -------------  ----------------
		sample              0.25               0.25           0.25              0.25
		population          0.173              0.499          0.296             0.032
	match_rate (micro=0.314, macro=0.232):
		  not_proofread    without_text    validated    proofread
		---------------  --------------  -----------  -----------
		          0.393           0.037        0.252        0.246
	filter_rate (micro=0.686, macro=0.768):
		  not_proofread    without_text    validated    proofread
		---------------  --------------  -----------  -----------
		          0.607           0.963        0.748        0.754
	recall (micro=0.659, macro=0.718):
		  not_proofread    without_text    validated    proofread
		---------------  --------------  -----------  -----------
		          0.702           0.959         0.66        0.553
	!recall (micro=0.894, macro=0.906):
		  not_proofread    without_text    validated    proofread
		---------------  --------------  -----------  -----------
		          0.914           0.994        0.834        0.883
	precision (micro=0.747, macro=0.71):
		  not_proofread    without_text    validated    proofread
		---------------  --------------  -----------  -----------
		          0.891           0.831        0.453        0.666
	!precision (micro=0.812, macro=0.875):
		  not_proofread    without_text    validated    proofread
		---------------  --------------  -----------  -----------
		          0.755           0.999        0.921        0.824
	f1 (micro=0.692, macro=0.704):
		  not_proofread    without_text    validated    proofread
		---------------  --------------  -----------  -----------
		          0.785            0.89        0.537        0.604
	!f1 (micro=0.848, macro=0.888):
		  not_proofread    without_text    validated    proofread
		---------------  --------------  -----------  -----------
		          0.827           0.996        0.875        0.853
	accuracy (micro=0.806, macro=0.847):
		  not_proofread    without_text    validated    proofread
		---------------  --------------  -----------  -----------
		          0.808           0.993        0.804        0.785
	fpr (micro=0.106, macro=0.094):
		  not_proofread    without_text    validated    proofread
		---------------  --------------  -----------  -----------
		          0.086           0.006        0.166        0.117
	roc_auc (micro=0.889, macro=0.904):
		  not_proofread    without_text    validated    proofread
		---------------  --------------  -----------  -----------
		          0.914           0.989        0.862        0.852
	pr_auc (micro=0.79, macro=0.777):
		  not_proofread    without_text    validated    proofread
		---------------  --------------  -----------  -----------
		          0.916           0.954        0.517        0.722
	
	 - score_schema: {'type': 'object', 'properties': {'prediction': {'description': 'The most likely label predicted by the estimator', 'type': 'string'}, 'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object', 'properties': {'not_proofread': {'type': 'number'}, 'without_text': {'type': 'number'}, 'validated': {'type': 'number'}, 'proofread': {'type': 'number'}}}}, 'title': 'Scikit learn-based classifier score with probability'}

