Model Information:
	 - type: GradientBoosting
	 - version: 0.8.0
	 - params: {'loss': 'deviance', 'init': None, 'ccp_alpha': 0.0, 'verbose': 0, 'min_impurity_split': None, 'center': True, 'multilabel': False, 'n_iter_no_change': None, 'min_samples_split': 2, 'validation_fraction': 0.1, 'subsample': 1.0, 'min_samples_leaf': 1, 'random_state': None, 'max_features': 'log2', 'label_weights': None, 'warm_start': False, 'min_weight_fraction_leaf': 0.0, 'labels': ['u', 'b', 'r', 's'], 'population_rates': None, 'tol': 0.0001, 'criterion': 'friedman_mse', 'min_impurity_decrease': 0.0, 'presort': 'deprecated', 'n_estimators': 500, 'learning_rate': 0.01, 'max_depth': 3, 'max_leaf_nodes': None, 'scale': True}
	Environment:
	 - revscoring_version: '2.8.2'
	 - platform: 'Linux-4.9.0-11-amd64-x86_64-with-debian-9.12'
	 - machine: 'x86_64'
	 - version: '#1 SMP Debian 4.9.189-3+deb9u1 (2019-09-20)'
	 - system: 'Linux'
	 - processor: ''
	 - python_build: ('default', 'Sep 27 2018 17:25:39')
	 - python_compiler: 'GCC 6.3.0 20170516'
	 - python_branch: ''
	 - python_implementation: 'CPython'
	 - python_revision: ''
	 - python_version: '3.5.3'
	 - release: '4.9.0-11-amd64'
	
	Statistics:
	counts (n=1960):
		label      n         ~u    ~b    ~r    ~s
		-------  ---  ---  ----  ----  ----  ----
		'u'      498  -->   371    15   106     6
		'b'      497  -->    87   222   106    82
		'r'      499  -->   176    23   289    11
		's'      466  -->     1    54    15   396
	rates:
		              'u'    'b'    'r'    's'
		----------  -----  -----  -----  -----
		sample      0.254  0.254  0.255  0.238
		population  0.019  0.06   0.042  0.879
	match_rate (micro=0.68, macro=0.301):
		    u      b      r      s
		-----  -----  -----  -----
		0.191  0.086  0.173  0.755
	filter_rate (micro=0.32, macro=0.699):
		    u      b      r      s
		-----  -----  -----  -----
		0.809  0.914  0.827  0.245
	recall (micro=0.812, macro=0.655):
		    u      b      r     s
		-----  -----  -----  ----
		0.745  0.447  0.579  0.85
	!recall (micro=0.928, macro=0.884):
		    u      b      r      s
		-----  -----  -----  -----
		0.819  0.937  0.845  0.934
	precision (micro=0.896, macro=0.379):
		    u      b     r      s
		-----  -----  ----  -----
		0.074  0.312  0.14  0.989
	!precision (micro=0.523, macro=0.849):
		    u      b      r      s
		-----  -----  -----  -----
		0.994  0.964  0.979  0.461
	f1 (micro=0.838, macro=0.411):
		    u      b      r      s
		-----  -----  -----  -----
		0.135  0.367  0.226  0.914
	!f1 (micro=0.655, macro=0.843):
		    u     b      r      s
		-----  ----  -----  -----
		0.898  0.95  0.907  0.617
	accuracy (micro=0.861, macro=0.855):
		    u      b      r     s
		-----  -----  -----  ----
		0.818  0.908  0.833  0.86
	fpr (micro=0.072, macro=0.116):
		    u      b      r      s
		-----  -----  -----  -----
		0.181  0.063  0.155  0.066
	roc_auc (micro=0.94, macro=0.855):
		    u      b      r      s
		-----  -----  -----  -----
		0.874  0.761  0.826  0.959
	pr_auc (micro=0.906, macro=0.419):
		    u      b      r      s
		-----  -----  -----  -----
		0.105  0.404  0.174  0.992
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'properties': {'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'properties': {'u': {'type': 'number'}, 's': {'type': 'number'}, 'b': {'type': 'number'}, 'r': {'type': 'number'}}, 'type': 'object'}, 'prediction': {'description': 'The most likely label predicted by the estimator', 'type': 'string'}}, 'type': 'object'}

