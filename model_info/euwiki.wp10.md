Model Information:
	 - type: GradientBoosting
	 - version: 0.8.0
	 - params: {'presort': 'auto', 'population_rates': None, 'multilabel': False, 'n_iter_no_change': None, 'label_weights': None, 'min_samples_split': 2, 'max_features': 'log2', 'min_impurity_decrease': 0.0, 'labels': ['Stub', 'Start', 'C', 'B', 'GA', 'FA'], 'criterion': 'friedman_mse', 'center': True, 'loss': 'deviance', 'validation_fraction': 0.1, 'verbose': 0, 'min_impurity_split': None, 'init': None, 'max_depth': 1, 'learning_rate': 0.01, 'subsample': 1.0, 'n_estimators': 300, 'min_weight_fraction_leaf': 0.0, 'random_state': None, 'warm_start': False, 'scale': True, 'min_samples_leaf': 1, 'tol': 0.0001, 'max_leaf_nodes': None}
	Environment:
	 - revscoring_version: '2.6.1'
	 - platform: 'Linux-4.9.0-9-amd64-x86_64-with-debian-9.11'
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
	counts (n=282):
		label      n         ~Stub    ~Start    ~C    ~B    ~GA    ~FA
		-------  ---  ---  -------  --------  ----  ----  -----  -----
		'Stub'    50  -->       29        15     6     0      0      0
		'Start'   49  -->       11        23    12     2      1      0
		'C'       50  -->        1         5    33     7      4      0
		'B'       44  -->        0         2     4    14     22      2
		'GA'      50  -->        1         1     3    10     20     15
		'FA'      39  -->        0         0     0     0     13     26
	rates:
		          'Stub'    'Start'    'C'    'B'    'GA'    'FA'
		------  --------  ---------  -----  -----  ------  ------
		sample     0.177      0.174  0.177  0.156   0.177   0.138
	match_rate (micro=0.168, macro=0.167):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.149    0.163  0.206  0.117  0.213  0.152
	filter_rate (micro=0.832, macro=0.833):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.851    0.837  0.794  0.883  0.787  0.848
	recall (micro=0.514, macro=0.516):
		  Stub    Start     C      B    GA     FA
		------  -------  ----  -----  ----  -----
		  0.58    0.469  0.66  0.318   0.4  0.667
	!recall (micro=0.901, macro=0.903):
		  Stub    Start      C     B     GA    FA
		------  -------  -----  ----  -----  ----
		 0.944    0.901  0.892  0.92  0.828  0.93
	precision (micro=0.519, macro=0.52):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		  0.69      0.5  0.569  0.424  0.333  0.605
	!precision (micro=0.902, macro=0.903):
		  Stub    Start      C     B     GA     FA
		------  -------  -----  ----  -----  -----
		 0.912     0.89  0.924  0.88  0.865  0.946
	f1 (micro=0.513, macro=0.515):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		  0.63    0.484  0.611  0.364  0.364  0.634
	!f1 (micro=0.901, macro=0.902):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.928    0.896  0.908  0.899  0.846  0.938
	accuracy (micro=0.836, macro=0.838):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.879    0.826  0.851  0.826  0.752  0.894
	fpr (micro=0.099, macro=0.097):
		  Stub    Start      C     B     GA    FA
		------  -------  -----  ----  -----  ----
		 0.056    0.099  0.108  0.08  0.172  0.07
	roc_auc (micro=0.871, macro=0.873):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.931    0.851  0.884  0.821  0.802  0.946
	pr_auc (micro=0.544, macro=0.543):
		  Stub    Start     C      B     GA     FA
		------  -------  ----  -----  -----  -----
		 0.714    0.451  0.72  0.377  0.383  0.615
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'properties': {'probability': {'properties': {'Start': {'type': 'number'}, 'GA': {'type': 'number'}, 'C': {'type': 'number'}, 'B': {'type': 'number'}, 'Stub': {'type': 'number'}, 'FA': {'type': 'number'}}, 'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object'}, 'prediction': {'description': 'The most likely label predicted by the estimator', 'type': 'string'}}, 'type': 'object'}

