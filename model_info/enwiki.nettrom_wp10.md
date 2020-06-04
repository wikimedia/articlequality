Model Information:
	 - type: GradientBoosting
	 - version: 0.8.2
	 - params: {'presort': 'auto', 'n_iter_no_change': None, 'verbose': 0, 'random_state': None, 'learning_rate': 0.01, 'scale': True, 'min_samples_leaf': 1, 'min_weight_fraction_leaf': 0.0, 'loss': 'deviance', 'max_features': 'log2', 'tol': 0.0001, 'labels': ['Stub', 'Start', 'C', 'B', 'GA', 'FA'], 'center': True, 'subsample': 1.0, 'validation_fraction': 0.1, 'n_estimators': 500, 'criterion': 'friedman_mse', 'multilabel': False, 'init': None, 'max_leaf_nodes': None, 'min_samples_split': 2, 'population_rates': None, 'label_weights': None, 'min_impurity_split': None, 'warm_start': False, 'max_depth': 7, 'min_impurity_decrease': 0.0}
	Environment:
	 - revscoring_version: '2.6.9'
	 - platform: 'Linux-4.9.0-8-amd64-x86_64-with-debian-9.4'
	 - machine: 'x86_64'
	 - version: '#1 SMP Debian 4.9.144-3.1 (2019-02-19)'
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
	counts (n=32347):
		label       n         ~Stub    ~Start    ~C    ~B    ~GA    ~FA
		-------  ----  ---  -------  --------  ----  ----  -----  -----
		'Stub'   5455  -->     4648       769    23    14      1      0
		'Start'  5454  -->      710      3500   833   343     64      4
		'C'      5471  -->       71       986  2660  1048    623     83
		'B'      5476  -->       43       661  1373  2161    899    339
		'GA'     5495  -->        3        38   304   333   3519   1298
		'FA'     4996  -->        1         2    26   244    937   3786
	rates:
		              'Stub'    'Start'    'C'    'B'    'GA'    'FA'
		----------  --------  ---------  -----  -----  ------  ------
		sample         0.169      0.169  0.169  0.169    0.17   0.154
		population     0.576      0.322  0.054  0.035    0.01   0.003
	match_rate (micro=0.388, macro=0.19):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.504    0.269  0.117  0.085  0.099  0.065
	filter_rate (micro=0.612, macro=0.81):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.496    0.731  0.883  0.915  0.901  0.935
	recall (micro=0.746, macro=0.629):
		  Stub    Start      C      B    GA     FA
		------  -------  -----  -----  ----  -----
		 0.852    0.642  0.486  0.395  0.64  0.758
	!recall (micro=0.944, macro=0.925):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.969    0.909  0.905  0.926  0.906  0.937
	precision (micro=0.828, macro=0.371):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.974     0.77  0.227  0.161  0.063  0.031
	!precision (micro=0.847, macro=0.935):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.828    0.842  0.968  0.977  0.996  0.999
	f1 (micro=0.775, macro=0.387):
		  Stub    Start     C      B     GA     FA
		------  -------  ----  -----  -----  -----
		 0.909      0.7  0.31  0.228  0.115  0.059
	!f1 (micro=0.892, macro=0.928):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.893    0.874  0.935  0.951  0.949  0.967
	accuracy (micro=0.875, macro=0.892):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.902    0.823  0.882  0.908  0.903  0.936
	fpr (micro=0.056, macro=0.075):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.031    0.091  0.095  0.074  0.094  0.063
	roc_auc (micro=0.941, macro=0.905):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.978    0.903  0.855  0.831  0.909  0.953
	pr_auc (micro=0.84, macro=0.397):
		  Stub    Start     C      B     GA     FA
		------  -------  ----  -----  -----  -----
		 0.983    0.783  0.25  0.163  0.128  0.074
	
	 - score_schema: {'type': 'object', 'properties': {'prediction': {'type': 'string', 'description': 'The most likely label predicted by the estimator'}, 'probability': {'type': 'object', 'properties': {'B': {'type': 'number'}, 'C': {'type': 'number'}, 'Stub': {'type': 'number'}, 'GA': {'type': 'number'}, 'FA': {'type': 'number'}, 'Start': {'type': 'number'}}, 'description': 'A mapping of probabilities onto each of the potential output labels'}}, 'title': 'Scikit learn-based classifier score with probability'}

