Model Information:
	 - type: GradientBoosting
	 - version: 0.9.2
	 - params: {'scale': True, 'center': True, 'labels': ['Stub', 'Start', 'C', 'B', 'GA', 'FA'], 'multilabel': False, 'population_rates': None, 'ccp_alpha': 0.0, 'criterion': 'friedman_mse', 'init': None, 'learning_rate': 0.01, 'loss': 'deviance', 'max_depth': 7, 'max_features': 'log2', 'max_leaf_nodes': None, 'min_impurity_decrease': 0.0, 'min_impurity_split': None, 'min_samples_leaf': 1, 'min_samples_split': 2, 'min_weight_fraction_leaf': 0.0, 'n_estimators': 500, 'n_iter_no_change': None, 'presort': 'deprecated', 'random_state': None, 'subsample': 1.0, 'tol': 0.0001, 'validation_fraction': 0.1, 'verbose': 0, 'warm_start': False, 'label_weights': None}
	Environment:
	 - revscoring_version: '2.11.1'
	 - platform: 'Linux-4.19.0-14-amd64-x86_64-with-debian-10.11'
	 - machine: 'x86_64'
	 - version: '#1 SMP Debian 4.19.171-2 (2021-01-30)'
	 - system: 'Linux'
	 - processor: ''
	 - python_build: ('default', 'Jul 25 2020 13:03:44')
	 - python_compiler: 'GCC 8.3.0'
	 - python_branch: ''
	 - python_implementation: 'CPython'
	 - python_revision: ''
	 - python_version: '3.7.3'
	 - release: '4.19.0-14-amd64'
	
	Statistics:
	counts (n=32277):
		label       n         ~Stub    ~Start    ~C    ~B    ~GA    ~FA
		-------  ----  ---  -------  --------  ----  ----  -----  -----
		'Stub'   5413  -->     4598       781    23    10      1      0
		'Start'  5437  -->      694      3522   810   338     70      3
		'C'      5465  -->       66       971  2697  1039    603     89
		'B'      5472  -->       39       663  1342  2163    926    339
		'GA'     5495  -->        3        39   315   352   3499   1287
		'FA'     4995  -->        1         2    21   235    914   3822
	rates:
		              'Stub'    'Start'    'C'    'B'    'GA'    'FA'
		----------  --------  ---------  -----  -----  ------  ------
		sample         0.168      0.168  0.169  0.17     0.17   0.155
		population     0.576      0.322  0.054  0.035    0.01   0.003
	match_rate (micro=0.387, macro=0.19):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.502    0.271  0.115  0.085  0.099  0.065
	filter_rate (micro=0.613, macro=0.81):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.498    0.729  0.885  0.915  0.901  0.935
	recall (micro=0.747, macro=0.631):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.849    0.648  0.494  0.395  0.637  0.765
	!recall (micro=0.945, macro=0.926):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		  0.97    0.908  0.906  0.926  0.906  0.937
	precision (micro=0.829, macro=0.372):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.975    0.771  0.233  0.161  0.063  0.031
	!precision (micro=0.847, macro=0.935):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.826    0.844  0.969  0.977  0.996  0.999
	f1 (micro=0.776, macro=0.389):
		  Stub    Start      C      B     GA    FA
		------  -------  -----  -----  -----  ----
		 0.908    0.704  0.316  0.229  0.115  0.06
	!f1 (micro=0.892, macro=0.929):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.892    0.875  0.937  0.951  0.949  0.967
	accuracy (micro=0.876, macro=0.893):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.901    0.824  0.884  0.908  0.903  0.937
	fpr (micro=0.055, macro=0.074):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		  0.03    0.092  0.094  0.074  0.094  0.063
	roc_auc (micro=0.942, macro=0.906):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.978    0.905  0.858  0.831  0.909  0.955
	pr_auc (micro=0.841, macro=0.398):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.983    0.788  0.253  0.164  0.127  0.076
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'prediction': {'description': 'The most likely label predicted by the estimator', 'type': 'string'}, 'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object', 'properties': {'Stub': {'type': 'number'}, 'Start': {'type': 'number'}, 'C': {'type': 'number'}, 'B': {'type': 'number'}, 'GA': {'type': 'number'}, 'FA': {'type': 'number'}}}}}

