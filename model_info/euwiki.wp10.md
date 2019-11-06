Model Information:
	 - type: RandomForest
	 - version: 0.8.1
	 - params: {'bootstrap': True, 'oob_score': False, 'population_rates': None, 'labels': ['Stub', 'Start', 'C', 'B', 'GA', 'FA'], 'random_state': None, 'verbose': 0, 'max_features': 'log2', 'class_weight': None, 'min_weight_fraction_leaf': 0.0, 'min_impurity_split': None, 'n_jobs': None, 'max_leaf_nodes': None, 'multilabel': False, 'center': True, 'max_depth': None, 'criterion': 'gini', 'min_samples_split': 2, 'min_impurity_decrease': 0.0, 'n_estimators': 320, 'scale': True, 'min_samples_leaf': 3, 'label_weights': None, 'warm_start': False}
	Environment:
	 - revscoring_version: '2.6.1'
	 - platform: 'Linux-4.9.0-9-amd64-x86_64-with-debian-9.11'
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
	counts (n=454):
		label      n         ~Stub    ~Start    ~C    ~B    ~GA    ~FA
		-------  ---  ---  -------  --------  ----  ----  -----  -----
		'Stub'    80  -->       47        28     5     0      0      0
		'Start'   75  -->       12        37    24     2      0      0
		'C'       86  -->        4         7    60    12      3      0
		'B'       73  -->        0         0    10    44     16      3
		'GA'      75  -->        0         0     1    18     39     17
		'FA'      65  -->        0         0     0     2     14     49
	rates:
		          'Stub'    'Start'    'C'    'B'    'GA'    'FA'
		------  --------  ---------  -----  -----  ------  ------
		sample     0.176      0.165  0.189  0.161   0.165   0.143
	match_rate (micro=0.168, macro=0.167):
		  Stub    Start     C      B     GA     FA
		------  -------  ----  -----  -----  -----
		 0.139    0.159  0.22  0.172  0.159  0.152
	filter_rate (micro=0.832, macro=0.833):
		  Stub    Start     C      B     GA     FA
		------  -------  ----  -----  -----  -----
		 0.861    0.841  0.78  0.828  0.841  0.848
	recall (micro=0.608, macro=0.609):
		  Stub    Start      C      B    GA     FA
		------  -------  -----  -----  ----  -----
		 0.588    0.493  0.698  0.603  0.52  0.754
	!recall (micro=0.921, macro=0.921):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.957    0.908  0.891  0.911  0.913  0.949
	precision (micro=0.612, macro=0.613):
		  Stub    Start    C      B     GA    FA
		------  -------  ---  -----  -----  ----
		 0.746    0.514  0.6  0.564  0.542  0.71
	!precision (micro=0.921, macro=0.922):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.916    0.901  0.927  0.923  0.906  0.958
	f1 (micro=0.607, macro=0.608):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.657    0.503  0.645  0.583  0.531  0.731
	!f1 (micro=0.921, macro=0.921):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.936    0.904  0.909  0.917  0.909  0.953
	accuracy (micro=0.868, macro=0.869):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.892    0.839  0.855  0.861  0.848  0.921
	fpr (micro=0.079, macro=0.079):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.043    0.092  0.109  0.089  0.087  0.051
	roc_auc (micro=0.895, macro=0.897):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.947    0.872  0.872  0.875  0.858  0.956
	pr_auc (micro=0.607, macro=0.605):
		  Stub    Start      C     B     GA     FA
		------  -------  -----  ----  -----  -----
		 0.731    0.528  0.684  0.53  0.463  0.693
	
	 - score_schema: {'properties': {'prediction': {'description': 'The most likely label predicted by the estimator', 'type': 'string'}, 'probability': {'properties': {'C': {'type': 'number'}, 'Stub': {'type': 'number'}, 'B': {'type': 'number'}, 'FA': {'type': 'number'}, 'Start': {'type': 'number'}, 'GA': {'type': 'number'}}, 'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object'}}, 'title': 'Scikit learn-based classifier score with probability', 'type': 'object'}

