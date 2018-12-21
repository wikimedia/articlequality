Model Information:
	 - type: RandomForest
	 - version: 0.4.0
	 - params: {'random_state': None, 'min_weight_fraction_leaf': 0.0, 'min_samples_leaf': 13, 'class_weight': None, 'verbose': 0, 'labels': ['A', 'B', 'C', 'D', 'E'], 'criterion': 'gini', 'center': True, 'n_jobs': 1, 'oob_score': False, 'warm_start': False, 'n_estimators': 20, 'min_samples_split': 2, 'multilabel': False, 'scale': True, 'max_depth': None, 'label_weights': None, 'population_rates': None, 'max_leaf_nodes': None, 'min_impurity_split': None, 'max_features': 'log2', 'bootstrap': True, 'min_impurity_decrease': 0.0}
	Environment:
	 - revscoring_version: '2.3.0'
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
	counts (n=5000):
		label       n         ~A    ~B    ~C    ~D    ~E
		-------  ----  ---  ----  ----  ----  ----  ----
		'A'       322  -->   259    22    41     0     0
		'B'       438  -->    25   223   186     3     1
		'C'      1773  -->    30    48  1621    69     5
		'D'       997  -->     0     0    47   771   179
		'E'      1470  -->     0     0     4    15  1451
	rates:
		          'A'    'B'    'C'    'D'    'E'
		------  -----  -----  -----  -----  -----
		sample  0.064  0.088  0.355  0.199  0.294
	match_rate (micro=0.274, macro=0.2):
		    E      D      B      A     C
		-----  -----  -----  -----  ----
		0.327  0.172  0.059  0.063  0.38
	filter_rate (micro=0.726, macro=0.8):
		    E      D      B      A     C
		-----  -----  -----  -----  ----
		0.673  0.828  0.941  0.937  0.62
	recall (micro=0.865, macro=0.798):
		    E      D      B      A      C
		-----  -----  -----  -----  -----
		0.987  0.773  0.509  0.804  0.914
	!recall (micro=0.948, macro=0.963):
		    E      D      B      A      C
		-----  -----  -----  -----  -----
		0.948  0.978  0.985  0.988  0.914
	precision (micro=0.862, macro=0.845):
		    E      D      B      A      C
		-----  -----  -----  -----  -----
		0.887  0.899  0.761  0.825  0.854
	!precision (micro=0.965, macro=0.966):
		    E      D      B      A      C
		-----  -----  -----  -----  -----
		0.994  0.945  0.954  0.987  0.951
	f1 (micro=0.859, macro=0.815):
		    E      D     B      A      C
		-----  -----  ----  -----  -----
		0.934  0.831  0.61  0.814  0.883
	!f1 (micro=0.956, macro=0.964):
		   E      D      B      A      C
		----  -----  -----  -----  -----
		0.97  0.962  0.969  0.987  0.932
	accuracy (micro=0.939, macro=0.946):
		    E      D      B      A      C
		-----  -----  -----  -----  -----
		0.959  0.937  0.943  0.976  0.914
	fpr (micro=0.052, macro=0.037):
		    E      D      B      A      C
		-----  -----  -----  -----  -----
		0.052  0.022  0.015  0.012  0.086
	roc_auc (micro=0.971, macro=0.969):
		    E      D      B      A      C
		-----  -----  -----  -----  -----
		0.991  0.965  0.943  0.984  0.963
	pr_auc (micro=0.912, macro=0.872):
		    E      D     B     A      C
		-----  -----  ----  ----  -----
		0.978  0.911  0.69  0.86  0.923
	
	 - score_schema: {'properties': {'prediction': {'description': 'The most likely label predicted by the estimator', 'type': 'string'}, 'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'properties': {'A': {'type': 'number'}, 'D': {'type': 'number'}, 'B': {'type': 'number'}, 'E': {'type': 'number'}, 'C': {'type': 'number'}}, 'type': 'object'}}, 'type': 'object', 'title': 'Scikit learn-based classifier score with probability'}

