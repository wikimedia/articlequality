Model Information:
	 - type: GradientBoosting
	 - version: 0.5.0
	 - params: {'warm_start': False, 'min_samples_leaf': 1, 'validation_fraction': 0.1, 'label_weights': None, 'random_state': None, 'tol': 0.0001, 'max_leaf_nodes': None, 'population_rates': None, 'criterion': 'friedman_mse', 'learning_rate': 0.01, 'n_estimators': 500, 'ccp_alpha': 0.0, 'init': None, 'min_samples_split': 2, 'max_features': 'log2', 'labels': ['A', 'B', 'C', 'D', 'E'], 'center': True, 'multilabel': False, 'loss': 'deviance', 'scale': True, 'presort': 'deprecated', 'n_iter_no_change': None, 'max_depth': 5, 'subsample': 1.0, 'verbose': 0, 'min_weight_fraction_leaf': 0.0, 'min_impurity_decrease': 0.0, 'min_impurity_split': None}
	Environment:
	 - revscoring_version: '2.8.2'
	 - platform: 'Linux-4.9.0-8-amd64-x86_64-with-debian-9.3'
	 - machine: 'x86_64'
	 - version: '#1 SMP Debian 4.9.144-3.1 (2019-02-19)'
	 - system: 'Linux'
	 - processor: ''
	 - python_build: ('default', 'Jul  9 2020 13:00:10')
	 - python_compiler: 'GCC 6.3.0 20170516'
	 - python_branch: ''
	 - python_implementation: 'CPython'
	 - python_revision: ''
	 - python_version: '3.5.3'
	 - release: '4.9.0-8-amd64'
	
	Statistics:
	counts (n=8988):
		label       n         ~A    ~B    ~C    ~D    ~E
		-------  ----  ---  ----  ----  ----  ----  ----
		'A'       895  -->   779    67    48     1     0
		'B'       786  -->    88   462   218    18     0
		'C'      2286  -->    44   130  1987   120     5
		'D'      1994  -->     0     8   116  1727   143
		'E'      3027  -->     0     0     2    83  2942
	rates:
		          'A'    'B'    'C'    'D'    'E'
		------  -----  -----  -----  -----  -----
		sample    0.1  0.087  0.254  0.222  0.337
	match_rate (micro=0.248, macro=0.2):
		    A      B      C      D      E
		-----  -----  -----  -----  -----
		0.101  0.074  0.264  0.217  0.344
	filter_rate (micro=0.752, macro=0.8):
		    A      B      C      D      E
		-----  -----  -----  -----  -----
		0.899  0.926  0.736  0.783  0.656
	recall (micro=0.879, macro=0.833):
		   A      B      C      D      E
		----  -----  -----  -----  -----
		0.87  0.588  0.869  0.866  0.972
	!recall (micro=0.966, macro=0.969):
		    A      B      C      D      E
		-----  -----  -----  -----  -----
		0.984  0.975  0.943  0.968  0.975
	precision (micro=0.876, macro=0.845):
		    A      B      C      D      E
		-----  -----  -----  -----  -----
		0.855  0.693  0.838  0.886  0.952
	!precision (micro=0.97, macro=0.97):
		    A      B      C      D      E
		-----  -----  -----  -----  -----
		0.986  0.961  0.955  0.962  0.986
	f1 (micro=0.877, macro=0.838):
		    A      B      C      D      E
		-----  -----  -----  -----  -----
		0.863  0.636  0.853  0.876  0.962
	!f1 (micro=0.968, macro=0.969):
		    A      B      C      D     E
		-----  -----  -----  -----  ----
		0.985  0.968  0.949  0.965  0.98
	accuracy (micro=0.952, macro=0.951):
		    A      B      C      D      E
		-----  -----  -----  -----  -----
		0.972  0.941  0.924  0.946  0.974
	fpr (micro=0.034, macro=0.031):
		    A      B      C      D      E
		-----  -----  -----  -----  -----
		0.016  0.025  0.057  0.032  0.025
	roc_auc (micro=0.975, macro=0.972):
		    A      B      C      D      E
		-----  -----  -----  -----  -----
		0.981  0.953  0.967  0.972  0.988
	pr_auc (micro=0.918, macro=0.884):
		    A      B      C      D      E
		-----  -----  -----  -----  -----
		0.897  0.712  0.909  0.914  0.985
	
	 - score_schema: {'properties': {'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'properties': {'D': {'type': 'number'}, 'C': {'type': 'number'}, 'E': {'type': 'number'}, 'A': {'type': 'number'}, 'B': {'type': 'number'}}, 'type': 'object'}, 'prediction': {'description': 'The most likely label predicted by the estimator', 'type': 'string'}}, 'title': 'Scikit learn-based classifier score with probability', 'type': 'object'}

