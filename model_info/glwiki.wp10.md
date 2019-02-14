Model Information:
	 - type: GradientBoosting
	 - version: 0.8.0
	 - params: {'init': None, 'min_samples_leaf': 1, 'presort': 'auto', 'learning_rate': 0.01, 'label_weights': None, 'random_state': None, 'min_impurity_split': None, 'criterion': 'friedman_mse', 'warm_start': False, 'min_samples_split': 2, 'population_rates': None, 'loss': 'deviance', 'max_features': 'log2', 'subsample': 1.0, 'scale': True, 'min_impurity_decrease': 0.0, 'n_estimators': 500, 'verbose': 0, 'center': True, 'multilabel': False, 'labels': ['Stub', 'Start', 'C', 'B', 'GA', 'FA'], 'max_leaf_nodes': None, 'max_depth': 3, 'min_weight_fraction_leaf': 0.0}
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
	counts (n=401):
		label      n         ~Stub    ~Start    ~C    ~B    ~GA    ~FA
		-------  ---  ---  -------  --------  ----  ----  -----  -----
		'Stub'    67  -->       50        16     1     0      0      0
		'Start'   67  -->       18        21    20     6      1      1
		'C'       67  -->        1        18    24    13      6      5
		'B'       67  -->        3         2    15    24      7     16
		'GA'      66  -->        0         2     6    12     28     18
		'FA'      67  -->        0         0     1    21      9     36
	rates:
		          'Stub'    'Start'    'C'    'B'    'GA'    'FA'
		------  --------  ---------  -----  -----  ------  ------
		sample     0.167      0.167  0.167  0.167   0.165   0.167
	match_rate (micro=0.167, macro=0.167):
		   GA    Stub    Start      C    FA     B
		-----  ------  -------  -----  ----  ----
		0.127    0.18    0.147  0.167  0.19  0.19
	filter_rate (micro=0.833, macro=0.833):
		   GA    Stub    Start      C    FA     B
		-----  ------  -------  -----  ----  ----
		0.873    0.82    0.853  0.833  0.81  0.81
	recall (micro=0.456, macro=0.456):
		   GA    Stub    Start      C     FA      B
		-----  ------  -------  -----  -----  -----
		0.424   0.746    0.313  0.358  0.537  0.358
	!recall (micro=0.891, macro=0.891):
		   GA    Stub    Start      C    FA      B
		-----  ------  -------  -----  ----  -----
		0.931   0.934    0.886  0.871  0.88  0.844
	precision (micro=0.458, macro=0.458):
		   GA    Stub    Start      C     FA      B
		-----  ------  -------  -----  -----  -----
		0.549   0.694    0.356  0.358  0.474  0.316
	!precision (micro=0.891, macro=0.891):
		   GA    Stub    Start      C     FA      B
		-----  ------  -------  -----  -----  -----
		0.891   0.948    0.865  0.871  0.905  0.868
	f1 (micro=0.455, macro=0.455):
		   GA    Stub    Start      C     FA      B
		-----  ------  -------  -----  -----  -----
		0.479   0.719    0.333  0.358  0.503  0.336
	!f1 (micro=0.891, macro=0.891):
		   GA    Stub    Start      C     FA      B
		-----  ------  -------  -----  -----  -----
		0.911   0.941    0.876  0.871  0.892  0.856
	accuracy (micro=0.819, macro=0.819):
		   GA    Stub    Start      C     FA      B
		-----  ------  -------  -----  -----  -----
		0.848   0.903    0.791  0.786  0.823  0.763
	fpr (micro=0.109, macro=0.109):
		   GA    Stub    Start      C    FA      B
		-----  ------  -------  -----  ----  -----
		0.069   0.066    0.114  0.129  0.12  0.156
	roc_auc (micro=0.798, macro=0.798):
		   GA    Stub    Start      C    FA      B
		-----  ------  -------  -----  ----  -----
		0.814   0.918    0.742  0.734  0.88  0.701
	pr_auc (micro=0.447, macro=0.447):
		   GA    Stub    Start      C    FA      B
		-----  ------  -------  -----  ----  -----
		0.543   0.699    0.355  0.309  0.49  0.288
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'probability': {'type': 'object', 'properties': {'GA': {'type': 'number'}, 'Stub': {'type': 'number'}, 'Start': {'type': 'number'}, 'C': {'type': 'number'}, 'FA': {'type': 'number'}, 'B': {'type': 'number'}}, 'description': 'A mapping of probabilities onto each of the potential output labels'}, 'prediction': {'type': 'string', 'description': 'The most likely label predicted by the estimator'}}}

