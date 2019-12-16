Model Information:
	 - type: GradientBoosting
	 - version: 0.8.2
	 - params: {'random_state': None, 'criterion': 'friedman_mse', 'max_leaf_nodes': None, 'min_impurity_decrease': 0.0, 'labels': ['Stub', 'Start', 'C', 'B', 'GA', 'FA'], 'loss': 'deviance', 'max_depth': 7, 'label_weights': None, 'min_samples_split': 2, 'center': True, 'n_iter_no_change': None, 'min_samples_leaf': 1, 'presort': 'auto', 'population_rates': None, 'tol': 0.0001, 'multilabel': False, 'min_weight_fraction_leaf': 0.0, 'verbose': 0, 'n_estimators': 500, 'warm_start': False, 'subsample': 1.0, 'max_features': 'log2', 'learning_rate': 0.01, 'scale': True, 'validation_fraction': 0.1, 'init': None, 'min_impurity_split': None}
	Environment:
	 - revscoring_version: '2.6.2'
	 - platform: 'Linux-4.9.0-11-amd64-x86_64-with-debian-9.11'
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
	counts (n=32371):
		label       n         ~Stub    ~Start    ~C    ~B    ~GA    ~FA
		-------  ----  ---  -------  --------  ----  ----  -----  -----
		'Stub'   5470  -->     4643       785    28    13      1      0
		'Start'  5461  -->      741      3461   834   355     67      3
		'C'      5472  -->       72       980  2723  1044    561     92
		'B'      5477  -->       37       662  1362  2196    885    335
		'GA'     5495  -->        3        39   317   337   3511   1288
		'FA'     4996  -->        1         2    23   227    921   3822
	rates:
		              'Stub'    'Start'    'C'    'B'    'GA'    'FA'
		----------  --------  ---------  -----  -----  ------  ------
		sample         0.169      0.169  0.169  0.169    0.17   0.154
		population     0.576      0.322  0.054  0.035    0.01   0.003
	match_rate (micro=0.386, macro=0.189):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.503    0.266  0.117  0.085  0.096  0.065
	filter_rate (micro=0.614, macro=0.811):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.497    0.734  0.883  0.915  0.904  0.935
	recall (micro=0.743, macro=0.631):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.849    0.634  0.498  0.401  0.639  0.765
	!recall (micro=0.943, macro=0.926):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.968    0.908  0.905  0.927  0.909  0.937
	precision (micro=0.827, macro=0.372):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.973    0.767  0.231  0.163  0.065  0.031
	!precision (micro=0.845, macro=0.934):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.825    0.839  0.969  0.977  0.996  0.999
	f1 (micro=0.773, macro=0.388):
		  Stub    Start      C      B     GA    FA
		------  -------  -----  -----  -----  ----
		 0.907    0.694  0.316  0.232  0.118  0.06
	!f1 (micro=0.89, macro=0.928):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.891    0.872  0.936  0.951  0.951  0.967
	accuracy (micro=0.873, macro=0.892):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.899     0.82  0.883  0.908  0.907  0.937
	fpr (micro=0.057, macro=0.074):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.032    0.092  0.095  0.073  0.091  0.063
	roc_auc (micro=0.942, macro=0.906):
		  Stub    Start      C      B    GA     FA
		------  -------  -----  -----  ----  -----
		 0.978    0.903  0.858  0.833  0.91  0.954
	pr_auc (micro=0.84, macro=0.401):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.983    0.784  0.254  0.173  0.139  0.074
	
	 - score_schema: {'type': 'object', 'title': 'Scikit learn-based classifier score with probability', 'properties': {'prediction': {'type': 'string', 'description': 'The most likely label predicted by the estimator'}, 'probability': {'type': 'object', 'description': 'A mapping of probabilities onto each of the potential output labels', 'properties': {'B': {'type': 'number'}, 'Start': {'type': 'number'}, 'C': {'type': 'number'}, 'GA': {'type': 'number'}, 'FA': {'type': 'number'}, 'Stub': {'type': 'number'}}}}}

