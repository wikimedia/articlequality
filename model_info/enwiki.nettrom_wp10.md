Model Information:
	 - type: GradientBoosting
	 - version: 0.8.1
	 - params: {'min_impurity_split': None, 'random_state': None, 'max_leaf_nodes': None, 'population_rates': None, 'loss': 'deviance', 'labels': ['Stub', 'Start', 'C', 'B', 'GA', 'FA'], 'verbose': 0, 'criterion': 'friedman_mse', 'init': None, 'presort': 'auto', 'max_depth': 7, 'learning_rate': 0.01, 'subsample': 1.0, 'min_weight_fraction_leaf': 0.0, 'min_samples_leaf': 1, 'min_impurity_decrease': 0.0, 'warm_start': False, 'max_features': 'log2', 'center': True, 'min_samples_split': 2, 'n_estimators': 500, 'multilabel': False, 'label_weights': None, 'scale': True}
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
	counts (n=32415):
		label       n         ~Stub    ~Start    ~C    ~B    ~GA    ~FA
		-------  ----  ---  -------  --------  ----  ----  -----  -----
		'Stub'   5483  -->     4654       786    24    18      1      0
		'Start'  5473  -->      716      3514   832   346     61      4
		'C'      5483  -->       68       987  2707  1063    558    100
		'B'      5485  -->       38       660  1377  2169    880    361
		'GA'     5495  -->        3        42   361   344   3447   1298
		'FA'     4996  -->        1         2    23   231    949   3790
	rates:
		              'Stub'    'Start'    'C'    'B'    'GA'    'FA'
		----------  --------  ---------  -----  -----  ------  ------
		sample         0.169      0.169  0.169  0.169    0.17   0.154
		population     0.576      0.322  0.054  0.035    0.01   0.003
	match_rate (micro=0.387, macro=0.19):
		   FA      C    Start     GA    Stub      B
		-----  -----  -------  -----  ------  -----
		0.066  0.119    0.269  0.096   0.502  0.085
	filter_rate (micro=0.613, macro=0.81):
		   FA      C    Start     GA    Stub      B
		-----  -----  -------  -----  ------  -----
		0.934  0.881    0.731  0.904   0.498  0.915
	recall (micro=0.745, macro=0.628):
		   FA      C    Start     GA    Stub      B
		-----  -----  -------  -----  ------  -----
		0.759  0.494    0.642  0.627   0.849  0.395
	!recall (micro=0.944, macro=0.925):
		   FA      C    Start     GA    Stub      B
		-----  -----  -------  -----  ------  -----
		0.936  0.903    0.908  0.909   0.969  0.926
	precision (micro=0.828, macro=0.371):
		  FA      C    Start     GA    Stub     B
		----  -----  -------  -----  ------  ----
		0.03  0.226    0.769  0.064   0.974  0.16
	!precision (micro=0.846, macro=0.935):
		   FA      C    Start     GA    Stub      B
		-----  -----  -------  -----  ------  -----
		0.999  0.969    0.842  0.996   0.825  0.977
	f1 (micro=0.774, macro=0.387):
		   FA     C    Start     GA    Stub      B
		-----  ----  -------  -----  ------  -----
		0.058  0.31      0.7  0.116   0.907  0.228
	!f1 (micro=0.891, macro=0.928):
		   FA      C    Start     GA    Stub      B
		-----  -----  -------  -----  ------  -----
		0.966  0.935    0.874  0.951   0.891  0.951
	accuracy (micro=0.874, macro=0.892):
		   FA      C    Start     GA    Stub      B
		-----  -----  -------  -----  ------  -----
		0.935  0.881    0.822  0.906     0.9  0.907
	fpr (micro=0.056, macro=0.075):
		   FA      C    Start     GA    Stub      B
		-----  -----  -------  -----  ------  -----
		0.064  0.097    0.092  0.091   0.031  0.074
	roc_auc (micro=0.941, macro=0.905):
		   FA      C    Start     GA    Stub      B
		-----  -----  -------  -----  ------  -----
		0.954  0.855    0.903  0.908   0.978  0.831
	pr_auc (micro=0.84, macro=0.399):
		   FA      C    Start     GA    Stub      B
		-----  -----  -------  -----  ------  -----
		0.076  0.249    0.783  0.133   0.983  0.172
	
	 - score_schema: {'type': 'object', 'properties': {'prediction': {'description': 'The most likely label predicted by the estimator', 'type': 'string'}, 'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object', 'properties': {'FA': {'type': 'number'}, 'C': {'type': 'number'}, 'Start': {'type': 'number'}, 'GA': {'type': 'number'}, 'Stub': {'type': 'number'}, 'B': {'type': 'number'}}}}, 'title': 'Scikit learn-based classifier score with probability'}

