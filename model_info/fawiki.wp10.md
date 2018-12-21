Model Information:
	 - type: GradientBoosting
	 - version: 0.8.0
	 - params: {'labels': ['Stub', 'Start', 'C', 'B', 'GA', 'FA'], 'n_estimators': 100, 'random_state': None, 'label_weights': None, 'min_samples_leaf': 1, 'min_samples_split': 2, 'verbose': 0, 'center': True, 'max_depth': 7, 'loss': 'deviance', 'min_impurity_decrease': 0.0, 'presort': 'auto', 'max_leaf_nodes': None, 'learning_rate': 0.5, 'multilabel': False, 'criterion': 'friedman_mse', 'scale': True, 'subsample': 1.0, 'population_rates': None, 'init': None, 'warm_start': False, 'min_impurity_split': None, 'min_weight_fraction_leaf': 0.0, 'max_features': 'log2'}
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
	counts (n=1235):
		label      n         ~Stub    ~Start    ~C    ~B    ~GA    ~FA
		-------  ---  ---  -------  --------  ----  ----  -----  -----
		'Stub'   226  -->      167        16    22    17      2      2
		'Start'   94  -->       26        23    35    10      0      0
		'C'      152  -->       22        20    53    42     12      3
		'B'      200  -->       13        18    26    58     64     21
		'GA'     300  -->        0         0    15    33    168     84
		'FA'     263  -->        2         0     3    18     84    156
	rates:
		              'Stub'    'Start'    'C'    'B'    'GA'    'FA'
		----------  --------  ---------  -----  -----  ------  ------
		sample         0.183      0.076  0.123  0.162   0.243   0.213
		population     0.182      0.076  0.123  0.162   0.242   0.212
	match_rate (micro=0.188, macro=0.166):
		  Stub     FA    Start     GA      C      B
		------  -----  -------  -----  -----  -----
		 0.185  0.215    0.062  0.267  0.125  0.144
	filter_rate (micro=0.812, macro=0.834):
		  Stub     FA    Start     GA      C      B
		------  -----  -------  -----  -----  -----
		 0.815  0.785    0.938  0.733  0.875  0.856
	recall (micro=0.506, macro=0.463):
		  Stub     FA    Start    GA      C     B
		------  -----  -------  ----  -----  ----
		 0.739  0.593    0.245  0.56  0.349  0.29
	!recall (micro=0.888, macro=0.899):
		  Stub     FA    Start     GA      C      B
		------  -----  -------  -----  -----  -----
		 0.938  0.887    0.953  0.827  0.907  0.884
	precision (micro=0.498, macro=0.464):
		  Stub     FA    Start     GA      C      B
		------  -----  -------  -----  -----  -----
		 0.724  0.586    0.298  0.508  0.344  0.325
	!precision (micro=0.893, macro=0.9):
		  Stub    FA    Start     GA      C      B
		------  ----  -------  -----  -----  -----
		 0.942  0.89    0.939  0.855  0.909  0.866
	f1 (micro=0.501, macro=0.463):
		  Stub     FA    Start     GA      C      B
		------  -----  -------  -----  -----  -----
		 0.732  0.589    0.269  0.533  0.346  0.307
	!f1 (micro=0.891, macro=0.899):
		  Stub     FA    Start    GA      C      B
		------  -----  -------  ----  -----  -----
		  0.94  0.888    0.946  0.84  0.908  0.875
	accuracy (micro=0.825, macro=0.836):
		  Stub     FA    Start     GA      C      B
		------  -----  -------  -----  -----  -----
		 0.901  0.824    0.899  0.762  0.838  0.788
	fpr (micro=0.112, macro=0.101):
		  Stub     FA    Start     GA      C      B
		------  -----  -------  -----  -----  -----
		 0.062  0.113    0.047  0.173  0.093  0.116
	roc_auc (micro=0.805, macro=0.8):
		  Stub     FA    Start     GA     C      B
		------  -----  -------  -----  ----  -----
		 0.934  0.837    0.773  0.775  0.79  0.693
	pr_auc (micro=0.494, macro=0.454):
		  Stub     FA    Start     GA      C      B
		------  -----  -------  -----  -----  -----
		 0.793  0.569    0.233  0.499  0.336  0.291
	
	 - score_schema: {'type': 'object', 'title': 'Scikit learn-based classifier score with probability', 'properties': {'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object', 'properties': {'Stub': {'type': 'number'}, 'FA': {'type': 'number'}, 'Start': {'type': 'number'}, 'GA': {'type': 'number'}, 'C': {'type': 'number'}, 'B': {'type': 'number'}}}, 'prediction': {'description': 'The most likely label predicted by the estimator', 'type': 'string'}}}

