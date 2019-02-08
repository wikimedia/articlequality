Model Information:
	 - type: GradientBoosting
	 - version: 0.8.0
	 - params: {'min_impurity_split': None, 'max_leaf_nodes': None, 'warm_start': False, 'subsample': 1.0, 'random_state': None, 'scale': True, 'learning_rate': 0.01, 'presort': 'auto', 'criterion': 'friedman_mse', 'multilabel': False, 'label_weights': None, 'min_weight_fraction_leaf': 0.0, 'max_features': 'log2', 'verbose': 0, 'labels': ['Stub', 'Start', 'C', 'B', 'GA', 'FA'], 'n_estimators': 300, 'loss': 'deviance', 'population_rates': None, 'min_samples_leaf': 1, 'min_samples_split': 2, 'init': None, 'max_depth': 1, 'min_impurity_decrease': 0.0, 'center': True}
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
	counts (n=282):
		label      n         ~Stub    ~Start    ~C    ~B    ~GA    ~FA
		-------  ---  ---  -------  --------  ----  ----  -----  -----
		'Stub'    50  -->       27        21     2     0      0      0
		'Start'   49  -->        8        26     9     4      2      0
		'C'       50  -->        2         3    33     7      4      1
		'B'       44  -->        0         2    11    16     13      2
		'GA'      50  -->        0         0     9    13     15     13
		'FA'      39  -->        0         0     1     0     10     28
	rates:
		          'Stub'    'Start'    'C'    'B'    'GA'    'FA'
		------  --------  ---------  -----  -----  ------  ------
		sample     0.177      0.174  0.177  0.156   0.177   0.138
	match_rate (micro=0.168, macro=0.167):
		  Stub      B     C    Start     GA     FA
		------  -----  ----  -------  -----  -----
		 0.131  0.142  0.23    0.184  0.156  0.156
	filter_rate (micro=0.832, macro=0.833):
		  Stub      B     C    Start     GA     FA
		------  -----  ----  -------  -----  -----
		 0.869  0.858  0.77    0.816  0.844  0.844
	recall (micro=0.514, macro=0.519):
		  Stub      B     C    Start    GA     FA
		------  -----  ----  -------  ----  -----
		  0.54  0.364  0.66    0.531   0.3  0.718
	!recall (micro=0.902, macro=0.903):
		  Stub      B      C    Start     GA     FA
		------  -----  -----  -------  -----  -----
		 0.957  0.899  0.862    0.888  0.875  0.934
	precision (micro=0.517, macro=0.519):
		  Stub    B      C    Start     GA     FA
		------  ---  -----  -------  -----  -----
		  0.73  0.4  0.508      0.5  0.341  0.636
	!precision (micro=0.902, macro=0.903):
		  Stub      B      C    Start     GA     FA
		------  -----  -----  -------  -----  -----
		 0.906  0.884  0.922      0.9  0.853  0.954
	f1 (micro=0.511, macro=0.514):
		  Stub      B      C    Start     GA     FA
		------  -----  -----  -------  -----  -----
		 0.621  0.381  0.574    0.515  0.319  0.675
	!f1 (micro=0.901, macro=0.903):
		  Stub      B      C    Start     GA     FA
		------  -----  -----  -------  -----  -----
		 0.931  0.892  0.891    0.894  0.864  0.944
	accuracy (micro=0.836, macro=0.838):
		  Stub      B      C    Start     GA     FA
		------  -----  -----  -------  -----  -----
		 0.883  0.816  0.826    0.826  0.773  0.904
	fpr (micro=0.098, macro=0.097):
		  Stub      B      C    Start     GA     FA
		------  -----  -----  -------  -----  -----
		 0.043  0.101  0.138    0.112  0.125  0.066
	roc_auc (micro=0.85, macro=0.851):
		  Stub     B      C    Start     GA     FA
		------  ----  -----  -------  -----  -----
		 0.935  0.78  0.848     0.85  0.781  0.913
	pr_auc (micro=0.529, macro=0.53):
		  Stub      B      C    Start     GA     FA
		------  -----  -----  -------  -----  -----
		 0.725  0.324  0.707    0.411  0.321  0.694
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'properties': {'probability': {'properties': {'Stub': {'type': 'number'}, 'B': {'type': 'number'}, 'C': {'type': 'number'}, 'Start': {'type': 'number'}, 'GA': {'type': 'number'}, 'FA': {'type': 'number'}}, 'type': 'object', 'description': 'A mapping of probabilities onto each of the potential output labels'}, 'prediction': {'type': 'string', 'description': 'The most likely label predicted by the estimator'}}, 'type': 'object'}

