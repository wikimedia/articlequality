Model Information:
	 - type: GradientBoosting
	 - version: 0.8.1
	 - params: {'min_impurity_split': None, 'learning_rate': 0.01, 'min_impurity_decrease': 0.0, 'warm_start': False, 'max_depth': 7, 'min_weight_fraction_leaf': 0.0, 'population_rates': None, 'max_leaf_nodes': None, 'scale': True, 'validation_fraction': 0.1, 'min_samples_split': 2, 'n_iter_no_change': None, 'init': None, 'max_features': 'log2', 'multilabel': False, 'presort': 'auto', 'center': True, 'verbose': 0, 'random_state': None, 'n_estimators': 500, 'subsample': 1.0, 'tol': 0.0001, 'criterion': 'friedman_mse', 'labels': ['Stub', 'Start', 'C', 'B', 'GA', 'FA'], 'label_weights': None, 'min_samples_leaf': 1, 'loss': 'deviance'}
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
	counts (n=32400):
		label       n         ~Stub    ~Start    ~C    ~B    ~GA    ~FA
		-------  ----  ---  -------  --------  ----  ----  -----  -----
		'Stub'   5477  -->     4635       803    26    12      1      0
		'Start'  5469  -->      704      3498   857   339     70      1
		'C'      5479  -->       75       987  2712  1028    584     93
		'B'      5484  -->       40       664  1379  2155    894    352
		'GA'     5495  -->        3        42   331   329   3509   1281
		'FA'     4996  -->        1         2    23   232    930   3808
	rates:
		              'Stub'    'Start'    'C'    'B'    'GA'    'FA'
		----------  --------  ---------  -----  -----  ------  ------
		sample         0.169      0.169  0.169  0.169    0.17   0.154
		population     0.576      0.322  0.054  0.035    0.01   0.003
	match_rate (micro=0.386, macro=0.189):
		  Stub      B      C     FA     GA    Start
		------  -----  -----  -----  -----  -------
		 0.501  0.083  0.119  0.065  0.097    0.269
	filter_rate (micro=0.614, macro=0.811):
		  Stub      B      C     FA     GA    Start
		------  -----  -----  -----  -----  -------
		 0.499  0.917  0.881  0.935  0.903    0.731
	recall (micro=0.743, macro=0.629):
		  Stub      B      C     FA     GA    Start
		------  -----  -----  -----  -----  -------
		 0.846  0.393  0.495  0.762  0.639     0.64
	!recall (micro=0.944, macro=0.925):
		  Stub      B      C     FA     GA    Start
		------  -----  -----  -----  -----  -------
		 0.969  0.928  0.903  0.937  0.908    0.907
	precision (micro=0.827, macro=0.371):
		  Stub      B      C     FA     GA    Start
		------  -----  -----  -----  -----  -------
		 0.974  0.163  0.227  0.031  0.064    0.766
	!precision (micro=0.844, macro=0.934):
		  Stub      B      C     FA     GA    Start
		------  -----  -----  -----  -----  -------
		 0.823  0.977  0.969  0.999  0.996    0.841
	f1 (micro=0.773, macro=0.387):
		  Stub      B      C    FA     GA    Start
		------  -----  -----  ----  -----  -------
		 0.906  0.231  0.311  0.06  0.117    0.697
	!f1 (micro=0.89, macro=0.928):
		  Stub      B      C     FA    GA    Start
		------  -----  -----  -----  ----  -------
		  0.89  0.952  0.935  0.967  0.95    0.873
	accuracy (micro=0.873, macro=0.892):
		  Stub      B      C     FA     GA    Start
		------  -----  -----  -----  -----  -------
		 0.898  0.909  0.881  0.937  0.905    0.821
	fpr (micro=0.056, macro=0.075):
		  Stub      B      C     FA     GA    Start
		------  -----  -----  -----  -----  -------
		 0.031  0.072  0.097  0.063  0.092    0.093
	roc_auc (micro=0.941, macro=0.905):
		  Stub      B      C     FA    GA    Start
		------  -----  -----  -----  ----  -------
		 0.978  0.831  0.857  0.954  0.91    0.903
	pr_auc (micro=0.84, macro=0.399):
		  Stub      B     C     FA     GA    Start
		------  -----  ----  -----  -----  -------
		 0.983  0.174  0.25  0.073  0.134    0.783
	
	 - score_schema: {'type': 'object', 'title': 'Scikit learn-based classifier score with probability', 'properties': {'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object', 'properties': {'Stub': {'type': 'number'}, 'B': {'type': 'number'}, 'C': {'type': 'number'}, 'FA': {'type': 'number'}, 'GA': {'type': 'number'}, 'Start': {'type': 'number'}}}, 'prediction': {'description': 'The most likely label predicted by the estimator', 'type': 'string'}}}

