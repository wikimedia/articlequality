Model Information:
	 - type: GradientBoosting
	 - version: 0.8.0
	 - params: {'criterion': 'friedman_mse', 'init': None, 'min_samples_leaf': 1, 'presort': 'auto', 'population_rates': None, 'verbose': 0, 'center': True, 'loss': 'deviance', 'learning_rate': 0.01, 'multilabel': False, 'scale': True, 'min_impurity_split': None, 'max_features': 'log2', 'labels': ['u', 'b', 'r', 's'], 'min_weight_fraction_leaf': 0.0, 'max_depth': 3, 'n_estimators': 500, 'min_samples_split': 2, 'min_impurity_decrease': 0.0, 'subsample': 1.0, 'max_leaf_nodes': None, 'warm_start': False, 'label_weights': None, 'random_state': None}
	Environment:
	 - revscoring_version: '2.3.4'
	 - platform: 'Linux-4.9.0-8-amd64-x86_64-with-debian-9.9'
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
		'u'      498  -->   368    15   110     5
		'b'      497  -->    86   221   108    82
		'r'      499  -->   179    26   283    11
		's'      466  -->     1    53    16   396
	rates:
		              'u'    'b'    'r'    's'
		----------  -----  -----  -----  -----
		sample      0.254  0.254  0.255  0.238
		population  0.019  0.06   0.042  0.879
	match_rate (micro=0.68, macro=0.303):
		    b      u      r      s
		-----  -----  -----  -----
		0.087  0.193  0.177  0.755
	filter_rate (micro=0.32, macro=0.697):
		    b      u      r      s
		-----  -----  -----  -----
		0.913  0.807  0.823  0.245
	recall (micro=0.812, macro=0.65):
		    b      u      r     s
		-----  -----  -----  ----
		0.445  0.739  0.567  0.85
	!recall (micro=0.928, macro=0.882):
		    b      u     r      s
		-----  -----  ----  -----
		0.936  0.818  0.84  0.934
	precision (micro=0.895, macro=0.376):
		    b      u      r      s
		-----  -----  -----  -----
		0.306  0.073  0.134  0.989
	!precision (micro=0.523, macro=0.849):
		    b      u      r      s
		-----  -----  -----  -----
		0.964  0.994  0.978  0.461
	f1 (micro=0.837, macro=0.407):
		    b      u      r      s
		-----  -----  -----  -----
		0.363  0.133  0.217  0.914
	!f1 (micro=0.655, macro=0.842):
		    b      u      r      s
		-----  -----  -----  -----
		0.949  0.897  0.904  0.618
	accuracy (micro=0.861, macro=0.853):
		    b      u      r     s
		-----  -----  -----  ----
		0.906  0.817  0.828  0.86
	fpr (micro=0.072, macro=0.118):
		    b      u     r      s
		-----  -----  ----  -----
		0.064  0.182  0.16  0.066
	roc_auc (micro=0.941, macro=0.855):
		    b      u      r     s
		-----  -----  -----  ----
		0.762  0.874  0.826  0.96
	pr_auc (micro=0.906, macro=0.419):
		    b      u      r      s
		-----  -----  -----  -----
		0.404  0.106  0.174  0.992
	
	 - score_schema: {'type': 'object', 'title': 'Scikit learn-based classifier score with probability', 'properties': {'prediction': {'type': 'string', 'description': 'The most likely label predicted by the estimator'}, 'probability': {'type': 'object', 'description': 'A mapping of probabilities onto each of the potential output labels', 'properties': {'b': {'type': 'number'}, 'u': {'type': 'number'}, 'r': {'type': 'number'}, 's': {'type': 'number'}}}}}

