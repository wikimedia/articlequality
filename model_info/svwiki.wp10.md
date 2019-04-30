Model Information:
	 - type: GradientBoosting
	 - version: 0.8.0
	 - params: {'presort': 'auto', 'warm_start': False, 'label_weights': None, 'labels': ['u', 'b', 'r', 's'], 'min_impurity_split': None, 'loss': 'deviance', 'scale': True, 'max_features': 'log2', 'subsample': 1.0, 'n_estimators': 300, 'multilabel': False, 'init': None, 'min_samples_leaf': 1, 'learning_rate': 0.01, 'population_rates': None, 'min_impurity_decrease': 0.0, 'max_leaf_nodes': None, 'random_state': None, 'min_weight_fraction_leaf': 0.0, 'verbose': 0, 'max_depth': 7, 'criterion': 'friedman_mse', 'min_samples_split': 2, 'center': True}
	Environment:
	 - revscoring_version: '2.3.4'
	 - platform: 'Linux-4.9.0-8-amd64-x86_64-with-debian-9.5'
	 - machine: 'x86_64'
	 - version: '#1 SMP Debian 4.9.110-3+deb9u6 (2018-10-08)'
	 - system: 'Linux'
	 - processor: ''
	 - python_build: ('default', 'Sep 27 2018 17:25:39')
	 - python_compiler: 'GCC 6.3.0 20170516'
	 - python_branch: ''
	 - python_implementation: 'CPython'
	 - python_revision: ''
	 - python_version: '3.5.3'
	 - release: '4.9.0-8-amd64'
	
	Statistics:
	counts (n=1960):
		label      n         ~u    ~b    ~r    ~s
		-------  ---  ---  ----  ----  ----  ----
		'u'      498  -->   354    14   125     5
		'b'      497  -->    83   220   108    86
		'r'      499  -->   164    29   296    10
		's'      466  -->     1    54    18   393
	rates:
		              'u'    'b'    'r'    's'
		----------  -----  -----  -----  -----
		sample      0.254  0.254  0.255  0.238
		population  0.019  0.06   0.042  0.879
	match_rate (micro=0.676, macro=0.302):
		   u      b      r      s
		----  -----  -----  -----
		0.18  0.089  0.189  0.749
	filter_rate (micro=0.324, macro=0.698):
		   u      b      r      s
		----  -----  -----  -----
		0.82  0.911  0.811  0.251
	recall (micro=0.806, macro=0.648):
		    u      b      r      s
		-----  -----  -----  -----
		0.711  0.443  0.593  0.843
	!recall (micro=0.926, macro=0.881):
		   u      b      r      s
		----  -----  -----  -----
		0.83  0.934  0.828  0.932
	precision (micro=0.894, macro=0.374):
		    u      b      r      s
		-----  -----  -----  -----
		0.075  0.299  0.131  0.989
	!precision (micro=0.514, macro=0.846):
		    u      b      r     s
		-----  -----  -----  ----
		0.993  0.963  0.979  0.45
	f1 (micro=0.833, macro=0.405):
		    u      b      r     s
		-----  -----  -----  ----
		0.136  0.357  0.215  0.91
	!f1 (micro=0.646, macro=0.839):
		    u      b      r      s
		-----  -----  -----  -----
		0.905  0.948  0.897  0.607
	accuracy (micro=0.855, macro=0.851):
		    u      b      r      s
		-----  -----  -----  -----
		0.828  0.904  0.818  0.854
	fpr (micro=0.074, macro=0.119):
		   u      b      r      s
		----  -----  -----  -----
		0.17  0.066  0.172  0.068
	roc_auc (micro=0.937, macro=0.851):
		    u      b      r      s
		-----  -----  -----  -----
		0.874  0.752  0.824  0.956
	pr_auc (micro=0.905, macro=0.416):
		    u      b      r      s
		-----  -----  -----  -----
		0.087  0.394  0.189  0.992
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'prediction': {'type': 'string', 'description': 'The most likely label predicted by the estimator'}, 'probability': {'type': 'object', 'description': 'A mapping of probabilities onto each of the potential output labels', 'properties': {'u': {'type': 'number'}, 'b': {'type': 'number'}, 'r': {'type': 'number'}, 's': {'type': 'number'}}}}}

