Model Information:
	 - type: GradientBoosting
	 - version: 0.8.0
	 - params: {'n_estimators': 300, 'random_state': None, 'labels': ['Stub', 'Start', 'C', 'B', 'GA', 'FA'], 'min_samples_split': 2, 'warm_start': False, 'scale': True, 'subsample': 1.0, 'population_rates': None, 'label_weights': None, 'criterion': 'friedman_mse', 'min_impurity_split': None, 'max_features': 'log2', 'verbose': 0, 'presort': 'auto', 'center': True, 'min_samples_leaf': 1, 'validation_fraction': 0.1, 'min_weight_fraction_leaf': 0.0, 'tol': 0.0001, 'loss': 'deviance', 'min_impurity_decrease': 0.0, 'multilabel': False, 'max_leaf_nodes': None, 'max_depth': 1, 'init': None, 'n_iter_no_change': None, 'learning_rate': 0.01}
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
	counts (n=282):
		label      n         ~Stub    ~Start    ~C    ~B    ~GA    ~FA
		-------  ---  ---  -------  --------  ----  ----  -----  -----
		'Stub'    50  -->       26        18     6     0      0      0
		'Start'   49  -->       11        25     9     4      0      0
		'C'       50  -->        3         6    30    10      1      0
		'B'       44  -->        1         1     7    17     15      3
		'GA'      50  -->        0         1     6    15     14     14
		'FA'      39  -->        0         0     0     1     12     26
	rates:
		          'Stub'    'Start'    'C'    'B'    'GA'    'FA'
		------  --------  ---------  -----  -----  ------  ------
		sample     0.177      0.174  0.177  0.156   0.177   0.138
	match_rate (micro=0.167, macro=0.167):
		    B     FA    Start      C     GA    Stub
		-----  -----  -------  -----  -----  ------
		0.167  0.152    0.181  0.206  0.149   0.145
	filter_rate (micro=0.833, macro=0.833):
		    B     FA    Start      C     GA    Stub
		-----  -----  -------  -----  -----  ------
		0.833  0.848    0.819  0.794  0.851   0.855
	recall (micro=0.489, macro=0.494):
		    B     FA    Start    C    GA    Stub
		-----  -----  -------  ---  ----  ------
		0.386  0.667     0.51  0.6  0.28    0.52
	!recall (micro=0.897, macro=0.898):
		    B    FA    Start      C     GA    Stub
		-----  ----  -------  -----  -----  ------
		0.874  0.93    0.888  0.879  0.879   0.935
	precision (micro=0.488, macro=0.49):
		    B     FA    Start      C     GA    Stub
		-----  -----  -------  -----  -----  ------
		0.362  0.605     0.49  0.517  0.333   0.634
	!precision (micro=0.896, macro=0.898):
		    B     FA    Start      C    GA    Stub
		-----  -----  -------  -----  ----  ------
		0.885  0.946    0.896  0.911  0.85     0.9
	f1 (micro=0.487, macro=0.49):
		    B     FA    Start      C     GA    Stub
		-----  -----  -------  -----  -----  ------
		0.374  0.634      0.5  0.556  0.304   0.571
	!f1 (micro=0.897, macro=0.898):
		    B     FA    Start      C     GA    Stub
		-----  -----  -------  -----  -----  ------
		0.879  0.938    0.892  0.895  0.864   0.918
	accuracy (micro=0.828, macro=0.83):
		    B     FA    Start     C     GA    Stub
		-----  -----  -------  ----  -----  ------
		0.798  0.894    0.823  0.83  0.773   0.862
	fpr (micro=0.103, macro=0.102):
		    B    FA    Start      C     GA    Stub
		-----  ----  -------  -----  -----  ------
		0.126  0.07    0.112  0.121  0.121   0.065
	roc_auc (micro=0.852, macro=0.854):
		    B     FA    Start      C     GA    Stub
		-----  -----  -------  -----  -----  ------
		0.791  0.939    0.847  0.843  0.783   0.919
	pr_auc (micro=0.53, macro=0.532):
		    B     FA    Start      C     GA    Stub
		-----  -----  -------  -----  -----  ------
		0.344  0.671    0.466  0.631  0.324   0.754
	
	 - score_schema: {'type': 'object', 'title': 'Scikit learn-based classifier score with probability', 'properties': {'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object', 'properties': {'B': {'type': 'number'}, 'FA': {'type': 'number'}, 'Start': {'type': 'number'}, 'Stub': {'type': 'number'}, 'GA': {'type': 'number'}, 'C': {'type': 'number'}}}, 'prediction': {'description': 'The most likely label predicted by the estimator', 'type': 'string'}}}

