Model Information:
	 - type: GradientBoosting
	 - version: 0.4.0
	 - params: {'max_depth': 5, 'verbose': 0, 'multilabel': False, 'labels': ['A', 'B', 'C', 'D', 'E'], 'center': True, 'min_impurity_decrease': 0.0, 'population_rates': None, 'max_leaf_nodes': None, 'max_features': 'log2', 'warm_start': False, 'init': None, 'min_impurity_split': None, 'label_weights': None, 'scale': True, 'subsample': 1.0, 'learning_rate': 0.01, 'min_samples_split': 2, 'loss': 'deviance', 'min_samples_leaf': 1, 'random_state': None, 'min_weight_fraction_leaf': 0.0, 'n_estimators': 500, 'criterion': 'friedman_mse', 'presort': 'auto'}
	Environment:
	 - revscoring_version: '2.3.3'
	 - platform: 'Linux-4.9.0-8-amd64-x86_64-with-debian-9.5'
	 - machine: 'x86_64'
	 - version: '#1 SMP Debian 4.9.110-3+deb9u6 (2018-10-08)'
	 - system: 'Linux'
	 - processor: ''
	 - python_build: ('default', 'Jan 19 2017 14:11:04')
	 - python_compiler: 'GCC 6.3.0 20170118'
	 - python_branch: ''
	 - python_implementation: 'CPython'
	 - python_revision: ''
	 - python_version: '3.5.3'
	 - release: '4.9.0-8-amd64'
	
	Statistics:
	counts (n=4964):
		label       n         ~A    ~B    ~C    ~D    ~E
		-------  ----  ---  ----  ----  ----  ----  ----
		'A'       322  -->   258    32    32     0     0
		'B'       438  -->    24   263   147     4     0
		'C'      1756  -->    35    49  1615    50     7
		'D'       996  -->     0     1    33   834   128
		'E'      1452  -->     0     0     4    15  1433
	rates:
		          'A'    'B'    'C'    'D'    'E'
		------  -----  -----  -----  -----  -----
		sample  0.065  0.088  0.354  0.201  0.293
	match_rate (micro=0.27, macro=0.2):
		    C      E     B      D      A
		-----  -----  ----  -----  -----
		0.369  0.316  0.07  0.182  0.064
	filter_rate (micro=0.73, macro=0.8):
		    C      E     B      D      A
		-----  -----  ----  -----  -----
		0.631  0.684  0.93  0.818  0.936
	recall (micro=0.887, macro=0.829):
		   C      E    B      D      A
		----  -----  ---  -----  -----
		0.92  0.987  0.6  0.837  0.801
	!recall (micro=0.959, macro=0.969):
		    C      E      B      D      A
		-----  -----  -----  -----  -----
		0.933  0.962  0.982  0.983  0.987
	precision (micro=0.885, macro=0.859):
		    C      E      B      D      A
		-----  -----  -----  -----  -----
		0.882  0.914  0.762  0.924  0.814
	!precision (micro=0.97, macro=0.972):
		    C      E      B     D      A
		-----  -----  -----  ----  -----
		0.955  0.994  0.962  0.96  0.986
	f1 (micro=0.884, macro=0.841):
		  C      E      B      D      A
		---  -----  -----  -----  -----
		0.9  0.949  0.672  0.878  0.808
	!f1 (micro=0.964, macro=0.97):
		    C      E      B      D      A
		-----  -----  -----  -----  -----
		0.944  0.978  0.972  0.971  0.987
	accuracy (micro=0.95, macro=0.955):
		    C      E      B      D      A
		-----  -----  -----  -----  -----
		0.928  0.969  0.948  0.953  0.975
	fpr (micro=0.041, macro=0.031):
		    C      E      B      D      A
		-----  -----  -----  -----  -----
		0.067  0.038  0.018  0.017  0.013
	roc_auc (micro=0.972, macro=0.97):
		    C      E     B      D      A
		-----  -----  ----  -----  -----
		0.966  0.988  0.95  0.964  0.984
	pr_auc (micro=0.915, macro=0.884):
		    C      E      B      D      A
		-----  -----  -----  -----  -----
		0.928  0.972  0.734  0.898  0.886
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object', 'properties': {'D': {'type': 'number'}, 'C': {'type': 'number'}, 'A': {'type': 'number'}, 'B': {'type': 'number'}, 'E': {'type': 'number'}}}, 'prediction': {'description': 'The most likely label predicted by the estimator', 'type': 'string'}}}

