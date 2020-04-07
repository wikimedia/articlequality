Model Information:
	 - type: GradientBoosting
	 - version: 0.8.0
	 - params: {'scale': True, 'min_samples_leaf': 1, 'presort': 'auto', 'loss': 'deviance', 'min_impurity_split': None, 'labels': ['1', '2', '3', '4', '5', '6'], 'warm_start': False, 'init': None, 'min_impurity_decrease': 0.0, 'center': True, 'criterion': 'friedman_mse', 'min_samples_split': 2, 'random_state': None, 'max_leaf_nodes': None, 'learning_rate': 0.01, 'n_estimators': 300, 'population_rates': None, 'max_features': 'log2', 'subsample': 1.0, 'verbose': 0, 'multilabel': False, 'max_depth': 7, 'tol': 0.0001, 'n_iter_no_change': None, 'min_weight_fraction_leaf': 0.0, 'validation_fraction': 0.1, 'label_weights': None}
	Environment:
	 - revscoring_version: '2.6.9'
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
	counts (n=7153):
		label       n         ~1    ~2    ~3    ~4    ~5    ~6
		-------  ----  ---  ----  ----  ----  ----  ----  ----
		'1'      1197  -->  1069    55    63     7     3     0
		'2'      1198  -->    73   850   231    20    18     6
		'3'      1195  -->    34    86   805   139    88    43
		'4'      1193  -->    16    20   200   264   373   320
		'5'      1187  -->     8    15    54   183   692   235
		'6'      1183  -->    15    11    43   154   198   762
	rates:
		              '1'    '2'    '3'    '4'    '5'    '6'
		----------  -----  -----  -----  -----  -----  -----
		sample      0.167  0.167  0.167  0.167  0.166  0.165
		population  0.712  0.188  0.055  0.033  0.006  0.007
	match_rate (micro=0.499, macro=0.207):
		    1      2      3      4      5      6
		-----  -----  -----  -----  -----  -----
		0.643  0.159  0.131  0.089  0.117  0.105
	filter_rate (micro=0.501, macro=0.793):
		    1      2      3      4      5      6
		-----  -----  -----  -----  -----  -----
		0.357  0.841  0.869  0.911  0.883  0.895
	recall (micro=0.821, macro=0.621):
		    1     2      3      4      5      6
		-----  ----  -----  -----  -----  -----
		0.893  0.71  0.674  0.221  0.583  0.644
	!recall (micro=0.967, macro=0.924):
		    1      2      3      4      5      6
		-----  -----  -----  -----  -----  -----
		0.975  0.969  0.901  0.916  0.886  0.899
	precision (micro=0.88, macro=0.377):
		    1      2      3      4     5      6
		-----  -----  -----  -----  ----  -----
		0.989  0.839  0.282  0.082  0.03  0.042
	!precision (micro=0.834, macro=0.945):
		    1      2     3      4      5      6
		-----  -----  ----  -----  -----  -----
		0.787  0.935  0.98  0.972  0.997  0.997
	f1 (micro=0.839, macro=0.393):
		    1      2      3      4      5      6
		-----  -----  -----  -----  -----  -----
		0.939  0.769  0.397  0.119  0.056  0.079
	!f1 (micro=0.893, macro=0.931):
		    1      2      3      4      5      6
		-----  -----  -----  -----  -----  -----
		0.871  0.952  0.939  0.943  0.938  0.945
	accuracy (micro=0.915, macro=0.9):
		    1     2      3      4      5      6
		-----  ----  -----  -----  -----  -----
		0.917  0.92  0.888  0.893  0.884  0.897
	fpr (micro=0.033, macro=0.076):
		    1      2      3      4      5      6
		-----  -----  -----  -----  -----  -----
		0.025  0.031  0.099  0.084  0.114  0.101
	roc_auc (micro=0.961, macro=0.894):
		    1      2      3      4      5      6
		-----  -----  -----  -----  -----  -----
		0.979  0.949  0.901  0.765  0.878  0.894
	pr_auc (micro=0.898, macro=0.416):
		    1      2      3      4      5      6
		-----  -----  -----  -----  -----  -----
		0.992  0.878  0.432  0.087  0.057  0.051
	
	 - score_schema: {'properties': {'probability': {'properties': {'3': {'type': 'number'}, '1': {'type': 'number'}, '6': {'type': 'number'}, '2': {'type': 'number'}, '5': {'type': 'number'}, '4': {'type': 'number'}}, 'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object'}, 'prediction': {'description': 'The most likely label predicted by the estimator', 'type': 'string'}}, 'title': 'Scikit learn-based classifier score with probability', 'type': 'object'}

