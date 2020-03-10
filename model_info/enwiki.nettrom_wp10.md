Model Information:
	 - type: GradientBoosting
	 - version: 0.8.2
	 - params: {'criterion': 'friedman_mse', 'init': None, 'presort': 'auto', 'subsample': 1.0, 'labels': ['Stub', 'Start', 'C', 'B', 'GA', 'FA'], 'max_features': 'log2', 'min_samples_leaf': 1, 'n_iter_no_change': None, 'min_impurity_split': None, 'max_depth': 7, 'verbose': 0, 'label_weights': None, 'max_leaf_nodes': None, 'population_rates': None, 'validation_fraction': 0.1, 'center': True, 'warm_start': False, 'tol': 0.0001, 'n_estimators': 500, 'multilabel': False, 'loss': 'deviance', 'min_samples_split': 2, 'scale': True, 'min_impurity_decrease': 0.0, 'random_state': None, 'min_weight_fraction_leaf': 0.0, 'learning_rate': 0.01}
	Environment:
	 - revscoring_version: '2.6.7'
	 - platform: 'Linux-5.3.0-40-generic-x86_64-with-debian-buster-sid'
	 - machine: 'x86_64'
	 - version: '#32-Ubuntu SMP Fri Jan 31 20:24:34 UTC 2020'
	 - system: 'Linux'
	 - processor: 'x86_64'
	 - python_build: ('default', 'Aug 26 2018 21:41:56')
	 - python_compiler: 'GCC 7.3.0'
	 - python_branch: ''
	 - python_implementation: 'CPython'
	 - python_revision: ''
	 - python_version: '3.5.6'
	 - release: '5.3.0-40-generic'
	
	Statistics:
	counts (n=32353):
		label       n         ~Stub    ~Start    ~C    ~B    ~GA    ~FA
		-------  ----  ---  -------  --------  ----  ----  -----  -----
		'Stub'   5457  -->     4645       771    26    14      1      0
		'Start'  5458  -->      723      3483   853   333     62      4
		'C'      5471  -->       68       962  2748  1037    565     91
		'B'      5476  -->       35       656  1385  2175    880    345
		'GA'     5495  -->        3        44   328   337   3490   1293
		'FA'     4996  -->        1         2    21   237    930   3805
	rates:
		              'Stub'    'Start'    'C'    'B'    'GA'    'FA'
		----------  --------  ---------  -----  -----  ------  ------
		sample         0.169      0.169  0.169  0.169    0.17   0.154
		population     0.576      0.322  0.054  0.035    0.01   0.003
	match_rate (micro=0.387, macro=0.189):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.504    0.267  0.119  0.084  0.096  0.065
	filter_rate (micro=0.613, macro=0.811):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.496    0.733  0.881  0.916  0.904  0.935
	recall (micro=0.746, macro=0.631):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.851    0.638  0.502  0.397  0.635  0.762
	!recall (micro=0.944, macro=0.926):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.969    0.909  0.903  0.927  0.909  0.937
	precision (micro=0.828, macro=0.372):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.974     0.77  0.229  0.163  0.065  0.031
	!precision (micro=0.847, macro=0.935):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.827    0.841  0.969  0.977  0.996  0.999
	f1 (micro=0.775, macro=0.388):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.908    0.698  0.315  0.231  0.118  0.059
	!f1 (micro=0.892, macro=0.928):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.893    0.874  0.935  0.952  0.951  0.967
	accuracy (micro=0.875, macro=0.893):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.901    0.822  0.881  0.909  0.907  0.936
	fpr (micro=0.056, macro=0.074):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.031    0.091  0.097  0.073  0.091  0.063
	roc_auc (micro=0.941, macro=0.906):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.978    0.903  0.856  0.832  0.911  0.954
	pr_auc (micro=0.84, macro=0.399):
		  Stub    Start      C      B    GA     FA
		------  -------  -----  -----  ----  -----
		 0.983    0.782  0.251  0.173  0.13  0.077
	
	 - score_schema: {'properties': {'prediction': {'description': 'The most likely label predicted by the estimator', 'type': 'string'}, 'probability': {'properties': {'Stub': {'type': 'number'}, 'C': {'type': 'number'}, 'GA': {'type': 'number'}, 'Start': {'type': 'number'}, 'FA': {'type': 'number'}, 'B': {'type': 'number'}}, 'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object'}}, 'title': 'Scikit learn-based classifier score with probability', 'type': 'object'}

