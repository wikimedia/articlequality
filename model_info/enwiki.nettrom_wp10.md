Model Information:
	 - type: GradientBoosting
	 - version: 0.8.2
	 - params: {'presort': 'auto', 'verbose': 0, 'warm_start': False, 'validation_fraction': 0.1, 'max_leaf_nodes': None, 'min_weight_fraction_leaf': 0.0, 'max_depth': 7, 'max_features': 'log2', 'init': None, 'min_samples_leaf': 1, 'population_rates': None, 'n_iter_no_change': None, 'min_impurity_split': None, 'criterion': 'friedman_mse', 'tol': 0.0001, 'min_samples_split': 2, 'n_estimators': 500, 'subsample': 1.0, 'loss': 'deviance', 'label_weights': None, 'labels': ['Stub', 'Start', 'C', 'B', 'GA', 'FA'], 'learning_rate': 0.01, 'random_state': None, 'scale': True, 'center': True, 'multilabel': False, 'min_impurity_decrease': 0.0}
	Environment:
	 - revscoring_version: '2.6.8'
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
	counts (n=32356):
		label       n         ~Stub    ~Start    ~C    ~B    ~GA    ~FA
		-------  ----  ---  -------  --------  ----  ----  -----  -----
		'Stub'   5458  -->     4616       804    24    13      1      0
		'Start'  5459  -->      710      3475   853   352     65      4
		'C'      5472  -->       64       977  2724  1055    558     94
		'B'      5476  -->       33       644  1374  2211    870    344
		'GA'     5495  -->        3        39   312   333   3476   1332
		'FA'     4996  -->        1         2    19   245    920   3809
	rates:
		              'Stub'    'Start'    'C'    'B'    'GA'    'FA'
		----------  --------  ---------  -----  -----  ------  ------
		sample         0.169      0.169  0.169  0.169    0.17   0.154
		population     0.576      0.322  0.054  0.035    0.01   0.003
	match_rate (micro=0.385, macro=0.189):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		   0.5    0.267  0.118  0.086  0.095  0.067
	filter_rate (micro=0.615, macro=0.811):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		   0.5    0.733  0.882  0.914  0.905  0.933
	recall (micro=0.742, macro=0.63):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.846    0.637  0.498  0.404  0.633  0.762
	!recall (micro=0.944, macro=0.926):
		  Stub    Start      C      B    GA     FA
		------  -------  -----  -----  ----  -----
		  0.97    0.908  0.904  0.926  0.91  0.935
	precision (micro=0.828, macro=0.372):
		  Stub    Start     C      B     GA    FA
		------  -------  ----  -----  -----  ----
		 0.974    0.768  0.23  0.163  0.065  0.03
	!precision (micro=0.843, macro=0.934):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.822     0.84  0.969  0.977  0.996  0.999
	f1 (micro=0.773, macro=0.387):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.906    0.696  0.315  0.232  0.118  0.058
	!f1 (micro=0.89, macro=0.928):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		  0.89    0.873  0.935  0.951  0.951  0.966
	accuracy (micro=0.873, macro=0.892):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.898    0.821  0.882  0.908  0.907  0.935
	fpr (micro=0.056, macro=0.074):
		  Stub    Start      C      B    GA     FA
		------  -------  -----  -----  ----  -----
		  0.03    0.092  0.096  0.074  0.09  0.065
	roc_auc (micro=0.941, macro=0.905):
		  Stub    Start      C      B    GA     FA
		------  -------  -----  -----  ----  -----
		 0.978    0.902  0.856  0.832  0.91  0.954
	pr_auc (micro=0.839, macro=0.398):
		  Stub    Start     C     B    GA     FA
		------  -------  ----  ----  ----  -----
		 0.982    0.783  0.25  0.16  0.14  0.075
	
	 - score_schema: {'properties': {'probability': {'properties': {'Stub': {'type': 'number'}, 'Start': {'type': 'number'}, 'FA': {'type': 'number'}, 'B': {'type': 'number'}, 'C': {'type': 'number'}, 'GA': {'type': 'number'}}, 'type': 'object', 'description': 'A mapping of probabilities onto each of the potential output labels'}, 'prediction': {'type': 'string', 'description': 'The most likely label predicted by the estimator'}}, 'type': 'object', 'title': 'Scikit learn-based classifier score with probability'}

