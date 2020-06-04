Model Information:
	 - type: RandomForest
	 - version: 0.8.1
	 - params: {'n_jobs': None, 'labels': ['Stub', 'Start', 'C', 'B', 'GA', 'FA'], 'max_features': 'log2', 'population_rates': None, 'n_estimators': 320, 'max_samples': None, 'criterion': 'gini', 'oob_score': False, 'min_impurity_decrease': 0.0, 'max_depth': None, 'min_impurity_split': None, 'scale': True, 'max_leaf_nodes': None, 'min_samples_split': 2, 'min_weight_fraction_leaf': 0.0, 'class_weight': None, 'bootstrap': True, 'ccp_alpha': 0.0, 'warm_start': False, 'verbose': 0, 'multilabel': False, 'random_state': None, 'label_weights': None, 'center': True, 'min_samples_leaf': 3}
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
	counts (n=454):
		label      n         ~Stub    ~Start    ~C    ~B    ~GA    ~FA
		-------  ---  ---  -------  --------  ----  ----  -----  -----
		'Stub'    80  -->       47        24     9     0      0      0
		'Start'   75  -->       13        30    30     2      0      0
		'C'       86  -->        4         7    60    13      2      0
		'B'       73  -->        0         0    10    43     18      2
		'GA'      75  -->        0         0     1    16     42     16
		'FA'      65  -->        0         0     0     1     16     48
	rates:
		          'Stub'    'Start'    'C'    'B'    'GA'    'FA'
		------  --------  ---------  -----  -----  ------  ------
		sample     0.176      0.165  0.189  0.161   0.165   0.143
	match_rate (micro=0.169, macro=0.167):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.141    0.134  0.242  0.165  0.172  0.145
	filter_rate (micro=0.831, macro=0.833):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.859    0.866  0.758  0.835  0.828  0.855
	recall (micro=0.595, macro=0.595):
		  Stub    Start      C      B    GA     FA
		------  -------  -----  -----  ----  -----
		 0.588      0.4  0.698  0.589  0.56  0.738
	!recall (micro=0.917, macro=0.919):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.955    0.918  0.864  0.916  0.905  0.954
	precision (micro=0.599, macro=0.602):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.734    0.492  0.545  0.573  0.538  0.727
	!precision (micro=0.918, macro=0.919):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.915    0.885  0.924  0.921  0.912  0.956
	f1 (micro=0.593, macro=0.595):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.653    0.441  0.612  0.581  0.549  0.733
	!f1 (micro=0.917, macro=0.919):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.935    0.902  0.893  0.918  0.909  0.955
	accuracy (micro=0.863, macro=0.865):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		  0.89    0.833  0.833  0.863  0.848  0.923
	fpr (micro=0.083, macro=0.081):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.045    0.082  0.136  0.084  0.095  0.046
	roc_auc (micro=0.894, macro=0.896):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.945    0.867  0.866  0.876  0.862  0.957
	pr_auc (micro=0.597, macro=0.595):
		  Stub    Start     C     B    GA     FA
		------  -------  ----  ----  ----  -----
		 0.735    0.486  0.66  0.54  0.46  0.692
	
	 - score_schema: {'properties': {'probability': {'properties': {'Start': {'type': 'number'}, 'GA': {'type': 'number'}, 'C': {'type': 'number'}, 'B': {'type': 'number'}, 'Stub': {'type': 'number'}, 'FA': {'type': 'number'}}, 'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object'}, 'prediction': {'description': 'The most likely label predicted by the estimator', 'type': 'string'}}, 'title': 'Scikit learn-based classifier score with probability', 'type': 'object'}

