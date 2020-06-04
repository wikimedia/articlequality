Model Information:
	 - type: GradientBoosting
	 - version: 0.4.0
	 - params: {'init': None, 'labels': ['A', 'B', 'C', 'D', 'E'], 'n_estimators': 500, 'min_samples_split': 2, 'n_iter_no_change': None, 'validation_fraction': 0.1, 'min_impurity_decrease': 0.0, 'population_rates': None, 'learning_rate': 0.01, 'warm_start': False, 'verbose': 0, 'min_weight_fraction_leaf': 0.0, 'tol': 0.0001, 'subsample': 1.0, 'criterion': 'friedman_mse', 'min_samples_leaf': 1, 'min_impurity_split': None, 'presort': 'deprecated', 'label_weights': None, 'random_state': None, 'multilabel': False, 'max_leaf_nodes': None, 'center': True, 'max_features': 'log2', 'scale': True, 'loss': 'deviance', 'ccp_alpha': 0.0, 'max_depth': 5}
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
	counts (n=4952):
		label       n         ~A    ~B    ~C    ~D    ~E
		-------  ----  ---  ----  ----  ----  ----  ----
		'A'       322  -->   258    28    36     0     0
		'B'       438  -->    27   235   172     4     0
		'C'      1756  -->    28    50  1648    27     3
		'D'       995  -->     0     0   242   716    37
		'E'      1441  -->     0     0     9   114  1318
	rates:
		          'A'    'B'    'C'    'D'    'E'
		------  -----  -----  -----  -----  -----
		sample  0.065  0.088  0.355  0.201  0.291
	match_rate (micro=0.275, macro=0.2):
		    A      B      C      D      E
		-----  -----  -----  -----  -----
		0.063  0.063  0.425  0.174  0.274
	filter_rate (micro=0.725, macro=0.8):
		    A      B      C      D      E
		-----  -----  -----  -----  -----
		0.937  0.937  0.575  0.826  0.726
	recall (micro=0.843, macro=0.782):
		    A      B      C     D      E
		-----  -----  -----  ----  -----
		0.801  0.537  0.938  0.72  0.915
	!recall (micro=0.936, macro=0.956):
		    A      B      C      D      E
		-----  -----  -----  -----  -----
		0.988  0.983  0.856  0.963  0.989
	precision (micro=0.847, macro=0.832):
		    A      B      C      D      E
		-----  -----  -----  -----  -----
		0.824  0.751  0.782  0.832  0.971
	!precision (micro=0.958, macro=0.96):
		    A      B      C      D      E
		-----  -----  -----  -----  -----
		0.986  0.956  0.962  0.932  0.966
	f1 (micro=0.84, macro=0.801):
		    A      B      C      D      E
		-----  -----  -----  -----  -----
		0.813  0.626  0.853  0.772  0.942
	!f1 (micro=0.946, macro=0.957):
		    A      B      C      D      E
		-----  -----  -----  -----  -----
		0.987  0.969  0.906  0.947  0.977
	accuracy (micro=0.926, macro=0.937):
		    A      B      C      D      E
		-----  -----  -----  -----  -----
		0.976  0.943  0.886  0.914  0.967
	fpr (micro=0.064, macro=0.044):
		    A      B      C      D      E
		-----  -----  -----  -----  -----
		0.012  0.017  0.144  0.037  0.011
	roc_auc (micro=0.968, macro=0.968):
		    A      B      C      D      E
		-----  -----  -----  -----  -----
		0.984  0.951  0.958  0.959  0.987
	pr_auc (micro=0.902, macro=0.869):
		    A      B      C      D      E
		-----  -----  -----  -----  -----
		0.886  0.716  0.919  0.848  0.978
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'probability': {'type': 'object', 'properties': {'A': {'type': 'number'}, 'D': {'type': 'number'}, 'E': {'type': 'number'}, 'C': {'type': 'number'}, 'B': {'type': 'number'}}, 'description': 'A mapping of probabilities onto each of the potential output labels'}, 'prediction': {'type': 'string', 'description': 'The most likely label predicted by the estimator'}}}

