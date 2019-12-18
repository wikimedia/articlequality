Model Information:
	 - type: RandomForest
	 - version: 0.8.1
	 - params: {'min_samples_leaf': 3, 'scale': True, 'n_estimators': 320, 'min_impurity_split': None, 'population_rates': None, 'random_state': None, 'verbose': 0, 'warm_start': False, 'max_leaf_nodes': None, 'min_weight_fraction_leaf': 0.0, 'label_weights': None, 'labels': ['Stub', 'Start', 'C', 'B', 'GA', 'FA'], 'n_jobs': None, 'max_features': 'log2', 'oob_score': False, 'center': True, 'class_weight': None, 'criterion': 'gini', 'multilabel': False, 'max_depth': None, 'bootstrap': True, 'min_samples_split': 2, 'min_impurity_decrease': 0.0}
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
	counts (n=454):
		label      n         ~Stub    ~Start    ~C    ~B    ~GA    ~FA
		-------  ---  ---  -------  --------  ----  ----  -----  -----
		'Stub'    80  -->       49        18    13     0      0      0
		'Start'   75  -->       16        32    24     3      0      0
		'C'       86  -->        5         8    57    13      3      0
		'B'       73  -->        0         0     9    43     19      2
		'GA'      75  -->        0         0     1    17     40     17
		'FA'      65  -->        0         0     0     2     12     51
	rates:
		          'Stub'    'Start'    'C'    'B'    'GA'    'FA'
		------  --------  ---------  -----  -----  ------  ------
		sample     0.176      0.165  0.189  0.161   0.165   0.143
	match_rate (micro=0.168, macro=0.167):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.154    0.128  0.229  0.172  0.163  0.154
	filter_rate (micro=0.832, macro=0.833):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.846    0.872  0.771  0.828  0.837  0.846
	recall (micro=0.599, macro=0.601):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.612    0.427  0.663  0.589  0.533  0.785
	!recall (micro=0.918, macro=0.92):
		  Stub    Start      C      B    GA     FA
		------  -------  -----  -----  ----  -----
		 0.944    0.931  0.872  0.908  0.91  0.951
	precision (micro=0.601, macro=0.603):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		   0.7    0.552  0.548  0.551  0.541  0.729
	!precision (micro=0.919, macro=0.92):
		  Stub    Start      C     B     GA     FA
		------  -------  -----  ----  -----  -----
		 0.919    0.891  0.917  0.92  0.908  0.964
	f1 (micro=0.597, macro=0.599):
		  Stub    Start    C     B     GA     FA
		------  -------  ---  ----  -----  -----
		 0.653    0.481  0.6  0.57  0.537  0.756
	!f1 (micro=0.918, macro=0.92):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.931    0.911  0.894  0.914  0.909  0.957
	accuracy (micro=0.864, macro=0.866):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.885    0.848  0.833  0.857  0.848  0.927
	fpr (micro=0.082, macro=0.08):
		  Stub    Start      C      B    GA     FA
		------  -------  -----  -----  ----  -----
		 0.056    0.069  0.128  0.092  0.09  0.049
	roc_auc (micro=0.894, macro=0.896):
		  Stub    Start      C      B    GA     FA
		------  -------  -----  -----  ----  -----
		 0.943    0.869  0.864  0.881  0.86  0.959
	pr_auc (micro=0.602, macro=0.601):
		  Stub    Start      C     B     GA     FA
		------  -------  -----  ----  -----  -----
		 0.727    0.513  0.652  0.55  0.467  0.699
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'prediction': {'type': 'string', 'description': 'The most likely label predicted by the estimator'}, 'probability': {'type': 'object', 'description': 'A mapping of probabilities onto each of the potential output labels', 'properties': {'Start': {'type': 'number'}, 'C': {'type': 'number'}, 'B': {'type': 'number'}, 'GA': {'type': 'number'}, 'FA': {'type': 'number'}, 'Stub': {'type': 'number'}}}}}

