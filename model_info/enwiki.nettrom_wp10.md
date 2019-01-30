Model Information:
	 - type: GradientBoosting
	 - version: 0.8.1
	 - params: {'n_estimators': 500, 'min_impurity_decrease': 0.0, 'verbose': 0, 'min_impurity_split': None, 'criterion': 'friedman_mse', 'loss': 'deviance', 'multilabel': False, 'subsample': 1.0, 'presort': 'auto', 'max_features': 'log2', 'labels': ['Stub', 'Start', 'C', 'B', 'GA', 'FA'], 'scale': True, 'learning_rate': 0.01, 'random_state': None, 'min_samples_leaf': 1, 'label_weights': None, 'init': None, 'warm_start': False, 'population_rates': None, 'center': True, 'max_leaf_nodes': None, 'min_samples_split': 2, 'max_depth': 7, 'min_weight_fraction_leaf': 0.0}
	Environment:
	 - revscoring_version: '2.3.0'
	 - platform: 'Linux-4.9.0-8-amd64-x86_64-with-debian-9.5'
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
	counts (n=32415):
		label       n         ~Stub    ~Start    ~C    ~B    ~GA    ~FA
		-------  ----  ---  -------  --------  ----  ----  -----  -----
		'Stub'   5483  -->     4661       782    25    14      1      0
		'Start'  5473  -->      718      3536   825   329     62      3
		'C'      5483  -->       71       986  2697  1082    555     92
		'B'      5485  -->       38       658  1374  2185    871    359
		'GA'     5495  -->        3        42   355   333   3461   1301
		'FA'     4996  -->        1         2    23   234    948   3788
	rates:
		              'Stub'    'Start'    'C'    'B'    'GA'    'FA'
		----------  --------  ---------  -----  -----  ------  ------
		sample         0.169      0.169  0.169  0.169    0.17   0.154
		population     0.576      0.322  0.054  0.035    0.01   0.003
	match_rate (micro=0.387, macro=0.19):
		    B    Stub     GA      C     FA    Start
		-----  ------  -----  -----  -----  -------
		0.085   0.503  0.096  0.118  0.066     0.27
	filter_rate (micro=0.613, macro=0.81):
		    B    Stub     GA      C     FA    Start
		-----  ------  -----  -----  -----  -------
		0.915   0.497  0.904  0.882  0.934     0.73
	recall (micro=0.747, macro=0.629):
		    B    Stub    GA      C     FA    Start
		-----  ------  ----  -----  -----  -------
		0.398    0.85  0.63  0.492  0.758    0.646
	!recall (micro=0.944, macro=0.925):
		    B    Stub     GA      C     FA    Start
		-----  ------  -----  -----  -----  -------
		0.926   0.969  0.909  0.903  0.936    0.908
	precision (micro=0.828, macro=0.371):
		    B    Stub     GA      C    FA    Start
		-----  ------  -----  -----  ----  -------
		0.162   0.974  0.064  0.227  0.03     0.77
	!precision (micro=0.847, macro=0.935):
		    B    Stub     GA      C     FA    Start
		-----  ------  -----  -----  -----  -------
		0.977   0.826  0.996  0.969  0.999    0.844
	f1 (micro=0.776, macro=0.388):
		   B    Stub     GA     C     FA    Start
		----  ------  -----  ----  -----  -------
		0.23   0.908  0.117  0.31  0.059    0.703
	!f1 (micro=0.892, macro=0.928):
		    B    Stub     GA      C     FA    Start
		-----  ------  -----  -----  -----  -------
		0.951   0.892  0.951  0.935  0.967    0.875
	accuracy (micro=0.875, macro=0.893):
		    B    Stub     GA      C     FA    Start
		-----  ------  -----  -----  -----  -------
		0.908   0.901  0.907  0.881  0.936    0.824
	fpr (micro=0.056, macro=0.075):
		    B    Stub     GA      C     FA    Start
		-----  ------  -----  -----  -----  -------
		0.074   0.031  0.091  0.097  0.064    0.092
	roc_auc (micro=0.941, macro=0.905):
		    B    Stub     GA      C     FA    Start
		-----  ------  -----  -----  -----  -------
		0.831   0.978  0.908  0.855  0.954    0.903
	pr_auc (micro=0.839, macro=0.398):
		    B    Stub     GA      C     FA    Start
		-----  ------  -----  -----  -----  -------
		0.171   0.983  0.133  0.247  0.073    0.783
	
	 - score_schema: {'properties': {'prediction': {'description': 'The most likely label predicted by the estimator', 'type': 'string'}, 'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'properties': {'B': {'type': 'number'}, 'Stub': {'type': 'number'}, 'GA': {'type': 'number'}, 'C': {'type': 'number'}, 'FA': {'type': 'number'}, 'Start': {'type': 'number'}}, 'type': 'object'}}, 'type': 'object', 'title': 'Scikit learn-based classifier score with probability'}

