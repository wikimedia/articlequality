Model Information:
	 - type: GradientBoosting
	 - version: 0.8.0
	 - params: {'criterion': 'friedman_mse', 'tol': 0.0001, 'subsample': 1.0, 'min_impurity_split': None, 'population_rates': None, 'labels': ['u', 'b', 'r', 's'], 'multilabel': False, 'min_impurity_decrease': 0.0, 'n_iter_no_change': None, 'learning_rate': 0.01, 'center': True, 'min_samples_leaf': 1, 'presort': 'auto', 'random_state': None, 'max_features': 'log2', 'max_leaf_nodes': None, 'min_weight_fraction_leaf': 0.0, 'verbose': 0, 'scale': True, 'init': None, 'loss': 'deviance', 'min_samples_split': 2, 'n_estimators': 500, 'label_weights': None, 'warm_start': False, 'validation_fraction': 0.1, 'max_depth': 3}
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
	counts (n=1960):
		label      n         ~u    ~b    ~r    ~s
		-------  ---  ---  ----  ----  ----  ----
		'u'      498  -->   369    15   108     6
		'b'      497  -->    83   222   111    81
		'r'      499  -->   178    24   286    11
		's'      466  -->     1    56    16   393
	rates:
		              'u'    'b'    'r'    's'
		----------  -----  -----  -----  -----
		sample      0.254  0.254  0.255  0.238
		population  0.019  0.06   0.042  0.879
	match_rate (micro=0.675, macro=0.301):
		    b      r      s     u
		-----  -----  -----  ----
		0.088  0.178  0.749  0.19
	filter_rate (micro=0.325, macro=0.699):
		    b      r      s     u
		-----  -----  -----  ----
		0.912  0.822  0.251  0.81
	recall (micro=0.806, macro=0.651):
		    b      r      s      u
		-----  -----  -----  -----
		0.447  0.573  0.843  0.741
	!recall (micro=0.928, macro=0.882):
		    b      r      s      u
		-----  -----  -----  -----
		0.935  0.839  0.934  0.821
	precision (micro=0.895, macro=0.376):
		    b      r      s      u
		-----  -----  -----  -----
		0.305  0.135  0.989  0.074
	!precision (micro=0.514, macro=0.847):
		    b      r      s      u
		-----  -----  -----  -----
		0.964  0.978  0.451  0.994
	f1 (micro=0.834, macro=0.407):
		    b      r      s      u
		-----  -----  -----  -----
		0.363  0.219  0.911  0.135
	!f1 (micro=0.647, macro=0.84):
		    b      r      s      u
		-----  -----  -----  -----
		0.949  0.903  0.608  0.899
	accuracy (micro=0.856, macro=0.852):
		    b      r      s      u
		-----  -----  -----  -----
		0.906  0.828  0.854  0.819
	fpr (micro=0.072, macro=0.118):
		    b      r      s      u
		-----  -----  -----  -----
		0.065  0.161  0.066  0.179
	roc_auc (micro=0.939, macro=0.855):
		    b      r      s      u
		-----  -----  -----  -----
		0.761  0.826  0.958  0.874
	pr_auc (micro=0.906, macro=0.419):
		    b      r      s      u
		-----  -----  -----  -----
		0.405  0.176  0.992  0.104
	
	 - score_schema: {'type': 'object', 'title': 'Scikit learn-based classifier score with probability', 'properties': {'prediction': {'type': 'string', 'description': 'The most likely label predicted by the estimator'}, 'probability': {'type': 'object', 'description': 'A mapping of probabilities onto each of the potential output labels', 'properties': {'b': {'type': 'number'}, 'r': {'type': 'number'}, 's': {'type': 'number'}, 'u': {'type': 'number'}}}}}

