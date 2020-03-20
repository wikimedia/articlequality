Model Information:
	 - type: GradientBoosting
	 - version: 0.8.2
	 - params: {'warm_start': False, 'min_impurity_split': None, 'min_impurity_decrease': 0.0, 'presort': 'auto', 'n_iter_no_change': None, 'max_depth': 7, 'max_features': 'log2', 'label_weights': None, 'learning_rate': 0.01, 'loss': 'deviance', 'population_rates': None, 'min_samples_split': 2, 'max_leaf_nodes': None, 'criterion': 'friedman_mse', 'verbose': 0, 'multilabel': False, 'min_weight_fraction_leaf': 0.0, 'init': None, 'random_state': None, 'validation_fraction': 0.1, 'tol': 0.0001, 'center': True, 'subsample': 1.0, 'scale': True, 'labels': ['Stub', 'Start', 'C', 'B', 'GA', 'FA'], 'n_estimators': 500, 'min_samples_leaf': 1}
	Environment:
	 - revscoring_version: '2.6.9-no_textstat'
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
	counts (n=32351):
		label       n         ~Stub    ~Start    ~C    ~B    ~GA    ~FA
		-------  ----  ---  -------  --------  ----  ----  -----  -----
		'Stub'   5455  -->     4623       797    22    12      1      0
		'Start'  5458  -->      682      3486   886   346     55      3
		'C'      5471  -->       69       937  2751  1060    558     96
		'B'      5476  -->       40       637  1380  2222    853    344
		'GA'     5495  -->        3        36   290   320   3525   1321
		'FA'     4996  -->        1         2    25   253    894   3821
	rates:
		              'Stub'    'Start'    'C'    'B'    'GA'    'FA'
		----------  --------  ---------  -----  -----  ------  ------
		sample         0.169      0.169  0.169  0.169    0.17   0.154
		population     0.576      0.322  0.054  0.035    0.01   0.003
	match_rate (micro=0.385, macro=0.189):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.501    0.267  0.119  0.086  0.093  0.066
	filter_rate (micro=0.615, macro=0.811):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.499    0.733  0.881  0.914  0.907  0.934
	recall (micro=0.744, macro=0.634):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.847    0.639  0.503  0.406  0.641  0.765
	!recall (micro=0.945, macro=0.926):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		  0.97     0.91  0.903  0.926  0.912  0.936
	precision (micro=0.83, macro=0.373):
		  Stub    Start     C      B     GA     FA
		------  -------  ----  -----  -----  -----
		 0.975    0.772  0.23  0.164  0.067  0.031
	!precision (micro=0.845, macro=0.935):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.824    0.841  0.969  0.978  0.996  0.999
	f1 (micro=0.774, macro=0.389):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.907    0.699  0.316  0.233  0.122  0.059
	!f1 (micro=0.891, macro=0.928):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.891    0.874  0.935  0.951  0.952  0.966
	accuracy (micro=0.874, macro=0.893):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		   0.9    0.823  0.881  0.908  0.909  0.935
	fpr (micro=0.055, macro=0.074):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		  0.03     0.09  0.097  0.074  0.088  0.064
	roc_auc (micro=0.942, macro=0.907):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.977    0.904  0.859  0.835  0.913  0.954
	pr_auc (micro=0.84, macro=0.403):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.983    0.783  0.253  0.178  0.139  0.082
	
	 - score_schema: {'properties': {'prediction': {'type': 'string', 'description': 'The most likely label predicted by the estimator'}, 'probability': {'properties': {'C': {'type': 'number'}, 'Stub': {'type': 'number'}, 'Start': {'type': 'number'}, 'FA': {'type': 'number'}, 'B': {'type': 'number'}, 'GA': {'type': 'number'}}, 'type': 'object', 'description': 'A mapping of probabilities onto each of the potential output labels'}}, 'type': 'object', 'title': 'Scikit learn-based classifier score with probability'}

