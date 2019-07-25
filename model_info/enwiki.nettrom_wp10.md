Model Information:
	 - type: GradientBoosting
	 - version: 0.8.1
	 - params: {'max_features': 'log2', 'min_impurity_split': None, 'loss': 'deviance', 'min_samples_leaf': 1, 'subsample': 1.0, 'random_state': None, 'min_samples_split': 2, 'warm_start': False, 'labels': ['Stub', 'Start', 'C', 'B', 'GA', 'FA'], 'criterion': 'friedman_mse', 'scale': True, 'min_weight_fraction_leaf': 0.0, 'multilabel': False, 'presort': 'auto', 'min_impurity_decrease': 0.0, 'verbose': 0, 'population_rates': None, 'n_estimators': 500, 'learning_rate': 0.01, 'label_weights': None, 'max_leaf_nodes': None, 'center': True, 'max_depth': 7, 'init': None}
	Environment:
	 - revscoring_version: '2.4.0'
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
	counts (n=32402):
		label       n         ~Stub    ~Start    ~C    ~B    ~GA    ~FA
		-------  ----  ---  -------  --------  ----  ----  -----  -----
		'Stub'   5477  -->     4682       758    23    13      1      0
		'Start'  5469  -->      712      3517   835   338     64      3
		'C'      5480  -->       65       996  2726  1048    548     97
		'B'      5485  -->       33       673  1407  2142    873    357
		'GA'     5495  -->        3        42   324   330   3502   1294
		'FA'     4996  -->        1         2    25   242    917   3809
	rates:
		              'Stub'    'Start'    'C'    'B'    'GA'    'FA'
		----------  --------  ---------  -----  -----  ------  ------
		sample         0.169      0.169  0.169  0.169    0.17   0.154
		population     0.576      0.322  0.054  0.035    0.01   0.003
	match_rate (micro=0.389, macro=0.19):
		  Stub      C     GA    Start     FA      B
		------  -----  -----  -------  -----  -----
		 0.505  0.119  0.095    0.269  0.066  0.084
	filter_rate (micro=0.611, macro=0.81):
		  Stub      C     GA    Start     FA      B
		------  -----  -----  -------  -----  -----
		 0.495  0.881  0.905    0.731  0.934  0.916
	recall (micro=0.749, macro=0.631):
		  Stub      C     GA    Start     FA      B
		------  -----  -----  -------  -----  -----
		 0.855  0.497  0.637    0.643  0.762  0.391
	!recall (micro=0.944, macro=0.926):
		  Stub      C     GA    Start     FA      B
		------  -----  -----  -------  -----  -----
		  0.97  0.903  0.911    0.908  0.936  0.927
	precision (micro=0.828, macro=0.371):
		  Stub      C     GA    Start     FA     B
		------  -----  -----  -------  -----  ----
		 0.975  0.228  0.066    0.769  0.031  0.16
	!precision (micro=0.849, macro=0.936):
		  Stub      C     GA    Start     FA      B
		------  -----  -----  -------  -----  -----
		 0.831  0.969  0.996    0.843  0.999  0.977
	f1 (micro=0.777, macro=0.388):
		  Stub      C    GA    Start     FA      B
		------  -----  ----  -------  -----  -----
		 0.911  0.313  0.12    0.701  0.059  0.227
	!f1 (micro=0.893, macro=0.929):
		  Stub      C     GA    Start     FA      B
		------  -----  -----  -------  -----  -----
		 0.895  0.935  0.951    0.874  0.967  0.951
	accuracy (micro=0.877, macro=0.893):
		  Stub      C     GA    Start     FA      B
		------  -----  -----  -------  -----  -----
		 0.904  0.881  0.908    0.823  0.936  0.908
	fpr (micro=0.056, macro=0.074):
		  Stub      C     GA    Start     FA      B
		------  -----  -----  -------  -----  -----
		  0.03  0.097  0.089    0.092  0.064  0.073
	roc_auc (micro=0.942, macro=0.906):
		  Stub      C    GA    Start     FA      B
		------  -----  ----  -------  -----  -----
		 0.978  0.856  0.91    0.904  0.954  0.832
	pr_auc (micro=0.841, macro=0.401):
		  Stub      C     GA    Start     FA      B
		------  -----  -----  -------  -----  -----
		 0.983  0.251  0.134    0.787  0.075  0.174
	
	 - score_schema: {'properties': {'probability': {'properties': {'Stub': {'type': 'number'}, 'C': {'type': 'number'}, 'GA': {'type': 'number'}, 'Start': {'type': 'number'}, 'FA': {'type': 'number'}, 'B': {'type': 'number'}}, 'type': 'object', 'description': 'A mapping of probabilities onto each of the potential output labels'}, 'prediction': {'type': 'string', 'description': 'The most likely label predicted by the estimator'}}, 'title': 'Scikit learn-based classifier score with probability', 'type': 'object'}

