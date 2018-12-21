Model Information:
	 - type: GradientBoosting
	 - version: 0.8.0
	 - params: {'random_state': None, 'init': None, 'loss': 'deviance', 'max_features': 'log2', 'learning_rate': 0.01, 'max_leaf_nodes': None, 'min_impurity_split': None, 'subsample': 1.0, 'criterion': 'friedman_mse', 'center': True, 'min_samples_split': 2, 'population_rates': None, 'min_weight_fraction_leaf': 0.0, 'label_weights': None, 'warm_start': False, 'min_samples_leaf': 1, 'n_estimators': 300, 'scale': True, 'presort': 'auto', 'labels': ['Stub', 'Start', 'C', 'B', 'GA', 'FA'], 'multilabel': False, 'min_impurity_decrease': 0.0, 'max_depth': 1, 'verbose': 0}
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
	counts (n=282):
		label      n         ~Stub    ~Start    ~C    ~B    ~GA    ~FA
		-------  ---  ---  -------  --------  ----  ----  -----  -----
		'Stub'    50  -->       25        17     8     0      0      0
		'Start'   49  -->       14        23     9     3      0      0
		'C'       50  -->        3         6    30    10      1      0
		'B'       44  -->        1         1     8    16     15      3
		'GA'      50  -->        0         1     4    15     15     15
		'FA'      39  -->        0         0     0     1     12     26
	rates:
		          'Stub'    'Start'    'C'    'B'    'GA'    'FA'
		------  --------  ---------  -----  -----  ------  ------
		sample     0.177      0.174  0.177  0.156   0.177   0.138
	match_rate (micro=0.167, macro=0.167):
		   GA    Start     FA     B    Stub      C
		-----  -------  -----  ----  ------  -----
		0.152     0.17  0.156  0.16   0.152  0.209
	filter_rate (micro=0.833, macro=0.833):
		   GA    Start     FA     B    Stub      C
		-----  -------  -----  ----  ------  -----
		0.848     0.83  0.844  0.84   0.848  0.791
	recall (micro=0.479, macro=0.483):
		  GA    Start     FA      B    Stub    C
		----  -------  -----  -----  ------  ---
		 0.3    0.469  0.667  0.364     0.5  0.6
	!recall (micro=0.895, macro=0.896):
		   GA    Start     FA      B    Stub      C
		-----  -------  -----  -----  ------  -----
		0.879    0.893  0.926  0.878   0.922  0.875
	precision (micro=0.476, macro=0.477):
		   GA    Start     FA      B    Stub      C
		-----  -------  -----  -----  ------  -----
		0.349    0.479  0.591  0.356   0.581  0.508
	!precision (micro=0.894, macro=0.896):
		   GA    Start     FA      B    Stub     C
		-----  -------  -----  -----  ------  ----
		0.854    0.889  0.945  0.882   0.895  0.91
	f1 (micro=0.475, macro=0.478):
		   GA    Start     FA     B    Stub     C
		-----  -------  -----  ----  ------  ----
		0.323    0.474  0.627  0.36   0.538  0.55
	!f1 (micro=0.894, macro=0.896):
		   GA    Start     FA     B    Stub      C
		-----  -------  -----  ----  ------  -----
		0.866    0.891  0.936  0.88   0.909  0.892
	accuracy (micro=0.824, macro=0.826):
		   GA    Start    FA      B    Stub      C
		-----  -------  ----  -----  ------  -----
		0.777    0.819  0.89  0.798   0.848  0.826
	fpr (micro=0.105, macro=0.104):
		   GA    Start     FA      B    Stub      C
		-----  -------  -----  -----  ------  -----
		0.121    0.107  0.074  0.122   0.078  0.125
	roc_auc (micro=0.849, macro=0.851):
		  GA    Start     FA      B    Stub     C
		----  -------  -----  -----  ------  ----
		0.79    0.845  0.937  0.791   0.913  0.83
	pr_auc (micro=0.526, macro=0.527):
		   GA    Start     FA      B    Stub      C
		-----  -------  -----  -----  ------  -----
		0.335     0.47  0.681  0.326   0.737  0.614
	
	 - score_schema: {'type': 'object', 'properties': {'prediction': {'type': 'string', 'description': 'The most likely label predicted by the estimator'}, 'probability': {'properties': {'GA': {'type': 'number'}, 'Start': {'type': 'number'}, 'FA': {'type': 'number'}, 'B': {'type': 'number'}, 'Stub': {'type': 'number'}, 'C': {'type': 'number'}}, 'type': 'object', 'description': 'A mapping of probabilities onto each of the potential output labels'}}, 'title': 'Scikit learn-based classifier score with probability'}

