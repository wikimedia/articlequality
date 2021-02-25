Model Information:
	 - type: GradientBoosting
	 - version: 0.8.0
	 - params: {'random_state': None, 'validation_fraction': 0.1, 'subsample': 1.0, 'presort': 'deprecated', 'n_estimators': 300, 'label_weights': None, 'min_impurity_split': None, 'loss': 'deviance', 'center': True, 'max_features': 'log2', 'tol': 0.0001, 'population_rates': None, 'min_samples_leaf': 1, 'ccp_alpha': 0.0, 'min_weight_fraction_leaf': 0.0, 'init': None, 'n_iter_no_change': None, 'verbose': 0, 'multilabel': False, 'learning_rate': 0.01, 'max_leaf_nodes': None, 'min_impurity_decrease': 0.0, 'min_samples_split': 2, 'warm_start': False, 'max_depth': 3, 'criterion': 'friedman_mse', 'scale': True, 'labels': ['E', 'D', 'C', 'B', 'A']}
	Environment:
	 - revscoring_version: '2.8.2'
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
	counts (n=1650):
		label      n         ~E    ~D    ~C    ~B    ~A
		-------  ---  ---  ----  ----  ----  ----  ----
		'E'      330  -->   212   118     0     0     0
		'D'      330  -->     2   267    46    15     0
		'C'      330  -->     0    40   290     0     0
		'B'      330  -->     0    26     2   192   110
		'A'      330  -->     0     0     0   108   222
	rates:
		              'E'    'D'    'C'    'B'    'A'
		----------  -----  -----  -----  -----  -----
		sample        0.2    0.2    0.2    0.2    0.2
		population    0.2    0.2    0.2    0.2    0.2
	match_rate (micro=0.2, macro=0.2):
		   E      D      C      B      A
		----  -----  -----  -----  -----
		0.13  0.273  0.205  0.191  0.201
	filter_rate (micro=0.8, macro=0.8):
		   E      D      C      B      A
		----  -----  -----  -----  -----
		0.87  0.727  0.795  0.809  0.799
	recall (micro=0.717, macro=0.717):
		    E      D      C      B      A
		-----  -----  -----  -----  -----
		0.642  0.809  0.879  0.582  0.673
	!recall (micro=0.929, macro=0.929):
		    E      D      C      B      A
		-----  -----  -----  -----  -----
		0.998  0.861  0.964  0.907  0.917
	precision (micro=0.744, macro=0.744):
		    E      D      C     B      A
		-----  -----  -----  ----  -----
		0.991  0.592  0.858  0.61  0.669
	!precision (micro=0.93, macro=0.93):
		    E      D     C      B      A
		-----  -----  ----  -----  -----
		0.918  0.947  0.97  0.897  0.918
	f1 (micro=0.719, macro=0.719):
		    E      D      C      B      A
		-----  -----  -----  -----  -----
		0.779  0.684  0.868  0.595  0.671
	!f1 (micro=0.929, macro=0.929):
		    E      D      C      B      A
		-----  -----  -----  -----  -----
		0.956  0.902  0.967  0.902  0.917
	accuracy (micro=0.887, macro=0.887):
		    E     D      C      B      A
		-----  ----  -----  -----  -----
		0.927  0.85  0.947  0.842  0.868
	fpr (micro=0.071, macro=0.071):
		    E      D      C      B      A
		-----  -----  -----  -----  -----
		0.002  0.139  0.036  0.093  0.083
	roc_auc (micro=0.94, macro=0.94):
		    E      D      C      B     A
		-----  -----  -----  -----  ----
		0.986  0.913  0.978  0.892  0.93
	pr_auc (micro=0.788, macro=0.788):
		    E      D      C      B      A
		-----  -----  -----  -----  -----
		0.969  0.806  0.873  0.617  0.674
	
	 - score_schema: {'type': 'object', 'title': 'Scikit learn-based classifier score with probability', 'properties': {'prediction': {'type': 'string', 'description': 'The most likely label predicted by the estimator'}, 'probability': {'type': 'object', 'description': 'A mapping of probabilities onto each of the potential output labels', 'properties': {'A': {'type': 'number'}, 'C': {'type': 'number'}, 'D': {'type': 'number'}, 'E': {'type': 'number'}, 'B': {'type': 'number'}}}}}

