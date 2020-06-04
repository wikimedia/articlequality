Model Information:
	 - type: GradientBoosting
	 - version: 0.8.0
	 - params: {'min_impurity_split': None, 'label_weights': None, 'population_rates': None, 'min_samples_split': 2, 'max_leaf_nodes': None, 'ccp_alpha': 0.0, 'subsample': 1.0, 'n_estimators': 500, 'max_depth': 3, 'multilabel': False, 'verbose': 0, 'presort': 'deprecated', 'loss': 'deviance', 'validation_fraction': 0.1, 'random_state': None, 'tol': 0.0001, 'labels': ['Stub', 'Start', 'C', 'B', 'GA', 'FA'], 'criterion': 'friedman_mse', 'max_features': 'log2', 'min_weight_fraction_leaf': 0.0, 'learning_rate': 0.01, 'min_impurity_decrease': 0.0, 'min_samples_leaf': 1, 'init': None, 'warm_start': False, 'scale': True, 'n_iter_no_change': None, 'center': True}
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
	counts (n=401):
		label      n         ~Stub    ~Start    ~C    ~B    ~GA    ~FA
		-------  ---  ---  -------  --------  ----  ----  -----  -----
		'Stub'    67  -->       45        22     0     0      0      0
		'Start'   67  -->       24        22    14     4      3      0
		'C'       67  -->        2        12    29    14      5      5
		'B'       67  -->        1         3    14    23     11     15
		'GA'      66  -->        0         2     9    11     33     11
		'FA'      67  -->        0         0     5    14     14     34
	rates:
		          'Stub'    'Start'    'C'    'B'    'GA'    'FA'
		------  --------  ---------  -----  -----  ------  ------
		sample     0.167      0.167  0.167  0.167   0.165   0.167
	match_rate (micro=0.167, macro=0.167):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		  0.18    0.152  0.177  0.165  0.165  0.162
	filter_rate (micro=0.833, macro=0.833):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		  0.82    0.848  0.823  0.835  0.835  0.838
	recall (micro=0.464, macro=0.464):
		  Stub    Start      C      B    GA     FA
		------  -------  -----  -----  ----  -----
		 0.672    0.328  0.433  0.343   0.5  0.507
	!recall (micro=0.893, macro=0.893):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.919    0.883  0.874  0.871  0.901  0.907
	precision (micro=0.461, macro=0.461):
		  Stub    Start      C      B    GA     FA
		------  -------  -----  -----  ----  -----
		 0.625    0.361  0.408  0.348   0.5  0.523
	!precision (micro=0.893, macro=0.893):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.933    0.868  0.885  0.869  0.901  0.902
	f1 (micro=0.462, macro=0.462):
		  Stub    Start     C      B    GA     FA
		------  -------  ----  -----  ----  -----
		 0.647    0.344  0.42  0.346   0.5  0.515
	!f1 (micro=0.893, macro=0.893):
		  Stub    Start     C     B     GA     FA
		------  -------  ----  ----  -----  -----
		 0.926    0.875  0.88  0.87  0.901  0.904
	accuracy (micro=0.821, macro=0.821):
		  Stub    Start    C      B     GA    FA
		------  -------  ---  -----  -----  ----
		 0.878    0.791  0.8  0.783  0.835  0.84
	fpr (micro=0.107, macro=0.107):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.081    0.117  0.126  0.129  0.099  0.093
	roc_auc (micro=0.802, macro=0.802):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.941    0.765  0.731  0.718  0.816  0.843
	pr_auc (micro=0.456, macro=0.457):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.703    0.363  0.352  0.317  0.524  0.479
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'properties': {'probability': {'properties': {'Start': {'type': 'number'}, 'GA': {'type': 'number'}, 'FA': {'type': 'number'}, 'Stub': {'type': 'number'}, 'C': {'type': 'number'}, 'B': {'type': 'number'}}, 'type': 'object', 'description': 'A mapping of probabilities onto each of the potential output labels'}, 'prediction': {'description': 'The most likely label predicted by the estimator', 'type': 'string'}}, 'type': 'object'}

