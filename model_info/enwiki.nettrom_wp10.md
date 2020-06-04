Model Information:
	 - type: GradientBoosting
	 - version: 0.8.2
	 - params: {'population_rates': None, 'loss': 'deviance', 'max_features': 'log2', 'validation_fraction': 0.1, 'min_impurity_split': None, 'scale': True, 'tol': 0.0001, 'criterion': 'friedman_mse', 'warm_start': False, 'min_weight_fraction_leaf': 0.0, 'ccp_alpha': 0.0, 'max_leaf_nodes': None, 'presort': 'deprecated', 'subsample': 1.0, 'labels': ['Stub', 'Start', 'C', 'B', 'GA', 'FA'], 'verbose': 0, 'min_impurity_decrease': 0.0, 'center': True, 'n_estimators': 500, 'init': None, 'learning_rate': 0.01, 'n_iter_no_change': None, 'random_state': None, 'min_samples_leaf': 1, 'min_samples_split': 2, 'multilabel': False, 'max_depth': 7, 'label_weights': None}
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
	counts (n=32347):
		label       n         ~Stub    ~Start    ~C    ~B    ~GA    ~FA
		-------  ----  ---  -------  --------  ----  ----  -----  -----
		'Stub'   5455  -->     4653       763    25    13      1      0
		'Start'  5454  -->      710      3494   838   342     66      4
		'C'      5471  -->       75       978  2671  1041    625     81
		'B'      5476  -->       41       667  1363  2158    915    332
		'GA'     5495  -->        3        39   302   330   3526   1295
		'FA'     4996  -->        1         2    23   248    934   3788
	rates:
		              'Stub'    'Start'    'C'    'B'    'GA'    'FA'
		----------  --------  ---------  -----  -----  ------  ------
		sample         0.169      0.169  0.169  0.169    0.17   0.154
		population     0.576      0.322  0.054  0.035    0.01   0.003
	match_rate (micro=0.388, macro=0.19):
		  Stub    Start      C      B    GA     FA
		------  -------  -----  -----  ----  -----
		 0.505    0.268  0.116  0.085   0.1  0.064
	filter_rate (micro=0.612, macro=0.81):
		  Stub    Start      C      B    GA     FA
		------  -------  -----  -----  ----  -----
		 0.495    0.732  0.884  0.915   0.9  0.936
	recall (micro=0.747, macro=0.629):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.853    0.641  0.488  0.394  0.642  0.758
	!recall (micro=0.944, macro=0.925):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.969    0.909  0.905  0.927  0.905  0.937
	precision (micro=0.828, macro=0.371):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.974     0.77  0.229  0.161  0.063  0.031
	!precision (micro=0.848, macro=0.935):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.829    0.842  0.968  0.977  0.996  0.999
	f1 (micro=0.776, macro=0.387):
		  Stub    Start      C      B     GA    FA
		------  -------  -----  -----  -----  ----
		  0.91    0.699  0.311  0.229  0.115  0.06
	!f1 (micro=0.892, macro=0.928):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.894    0.874  0.936  0.951  0.949  0.967
	accuracy (micro=0.876, macro=0.892):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.902    0.822  0.882  0.908  0.903  0.937
	fpr (micro=0.056, macro=0.075):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.031    0.091  0.095  0.073  0.095  0.063
	roc_auc (micro=0.941, macro=0.905):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.978    0.903  0.856  0.831  0.909  0.954
	pr_auc (micro=0.839, macro=0.397):
		  Stub    Start     C      B     GA     FA
		------  -------  ----  -----  -----  -----
		 0.983    0.783  0.25  0.164  0.131  0.075
	
	 - score_schema: {'type': 'object', 'properties': {'prediction': {'description': 'The most likely label predicted by the estimator', 'type': 'string'}, 'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'properties': {'B': {'type': 'number'}, 'GA': {'type': 'number'}, 'Start': {'type': 'number'}, 'C': {'type': 'number'}, 'Stub': {'type': 'number'}, 'FA': {'type': 'number'}}, 'type': 'object'}}, 'title': 'Scikit learn-based classifier score with probability'}

