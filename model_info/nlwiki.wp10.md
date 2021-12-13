Model Information:
	 - type: GradientBoosting
	 - version: 0.9.0
	 - params: {'min_samples_leaf': 1, 'ccp_alpha': 0.0, 'population_rates': None, 'multilabel': False, 'random_state': None, 'max_leaf_nodes': None, 'min_impurity_split': None, 'scale': True, 'subsample': 1.0, 'max_depth': 5, 'n_estimators': 300, 'min_impurity_decrease': 0.0, 'max_features': 'log2', 'n_iter_no_change': None, 'labels': ['E', 'D', 'C', 'B', 'A'], 'init': None, 'verbose': 0, 'tol': 0.0001, 'min_samples_split': 2, 'label_weights': None, 'min_weight_fraction_leaf': 0.0, 'presort': 'deprecated', 'center': True, 'learning_rate': 0.5, 'validation_fraction': 0.1, 'criterion': 'friedman_mse', 'warm_start': False, 'loss': 'deviance'}
	Environment:
	 - revscoring_version: '2.11.1'
	 - platform: 'Linux-4.19.0-0.bpo.14-amd64-x86_64-with-debian-9.4'
	 - machine: 'x86_64'
	 - version: '#1 SMP Debian 4.19.171-2~deb9u1 (2021-02-08)'
	 - system: 'Linux'
	 - processor: ''
	 - python_build: ('default', 'Sep 27 2018 17:25:39')
	 - python_compiler: 'GCC 6.3.0 20170516'
	 - python_branch: ''
	 - python_implementation: 'CPython'
	 - python_revision: ''
	 - python_version: '3.5.3'
	 - release: '4.19.0-0.bpo.14-amd64'
	
	Statistics:
	counts (n=160):
		label      n         ~E    ~D    ~C    ~B    ~A
		-------  ---  ---  ----  ----  ----  ----  ----
		'E'       32  -->    20    10     1     1     0
		'D'       32  -->     3    19     6     4     0
		'C'       32  -->     0    14    14     3     1
		'B'       32  -->     1     2     5    16     8
		'A'       32  -->     0     0     3    15    14
	rates:
		              'E'    'D'    'C'    'B'    'A'
		----------  -----  -----  -----  -----  -----
		sample        0.2    0.2    0.2    0.2    0.2
		population    0.2    0.2    0.2    0.2    0.2
	match_rate (micro=0.2, macro=0.2):
		   E      D      C      B      A
		----  -----  -----  -----  -----
		0.15  0.281  0.181  0.244  0.144
	filter_rate (micro=0.8, macro=0.8):
		   E      D      C      B      A
		----  -----  -----  -----  -----
		0.85  0.719  0.819  0.756  0.856
	recall (micro=0.519, macro=0.519):
		    E      D      C    B      A
		-----  -----  -----  ---  -----
		0.625  0.594  0.438  0.5  0.438
	!recall (micro=0.88, macro=0.88):
		    E      D      C     B     A
		-----  -----  -----  ----  ----
		0.969  0.797  0.883  0.82  0.93
	precision (micro=0.551, macro=0.551):
		    E      D      C     B      A
		-----  -----  -----  ----  -----
		0.833  0.422  0.483  0.41  0.609
	!precision (micro=0.88, macro=0.88):
		    E      D      C      B      A
		-----  -----  -----  -----  -----
		0.912  0.887  0.863  0.868  0.869
	f1 (micro=0.525, macro=0.525):
		    E      D      C      B      A
		-----  -----  -----  -----  -----
		0.714  0.494  0.459  0.451  0.509
	!f1 (micro=0.879, macro=0.879):
		    E     D      C      B      A
		-----  ----  -----  -----  -----
		0.939  0.84  0.873  0.843  0.898
	accuracy (micro=0.808, macro=0.808):
		  E      D      C      B      A
		---  -----  -----  -----  -----
		0.9  0.756  0.794  0.756  0.831
	fpr (micro=0.12, macro=0.12):
		    E      D      C     B     A
		-----  -----  -----  ----  ----
		0.031  0.203  0.117  0.18  0.07
	roc_auc (micro=0.796, macro=0.796):
		    E      D      C      B      A
		-----  -----  -----  -----  -----
		0.964  0.766  0.717  0.685  0.849
	pr_auc (micro=0.537, macro=0.537):
		    E      D     C      B      A
		-----  -----  ----  -----  -----
		0.863  0.449  0.48  0.319  0.573
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'properties': {'prediction': {'description': 'The most likely label predicted by the estimator', 'type': 'string'}, 'probability': {'properties': {'A': {'type': 'number'}, 'C': {'type': 'number'}, 'D': {'type': 'number'}, 'B': {'type': 'number'}, 'E': {'type': 'number'}}, 'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object'}}, 'type': 'object'}

