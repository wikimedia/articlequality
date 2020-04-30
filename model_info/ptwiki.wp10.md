Model Information:
	 - type: GradientBoosting
	 - version: 0.8.0
	 - params: {'min_samples_split': 2, 'label_weights': None, 'max_depth': 7, 'min_impurity_split': None, 'learning_rate': 0.01, 'verbose': 0, 'max_features': 'log2', 'center': True, 'subsample': 1.0, 'n_estimators': 300, 'warm_start': False, 'multilabel': False, 'min_samples_leaf': 1, 'labels': ['1', '2', '3', '4', '5', '6'], 'scale': True, 'presort': 'auto', 'population_rates': None, 'loss': 'deviance', 'random_state': None, 'max_leaf_nodes': None, 'init': None, 'n_iter_no_change': None, 'criterion': 'friedman_mse', 'min_impurity_decrease': 0.0, 'validation_fraction': 0.1, 'tol': 0.0001, 'min_weight_fraction_leaf': 0.0}
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
	counts (n=8921):
		label       n         ~1    ~2    ~3    ~4    ~5    ~6
		-------  ----  ---  ----  ----  ----  ----  ----  ----
		'1'      1495  -->  1319   107    62     5     2     0
		'2'      1494  -->    90  1057   300    21    21     5
		'3'      1497  -->    31    94  1066   166    97    43
		'4'      1489  -->    15    31   296   332   451   364
		'5'      1483  -->    10    12   116   227   750   368
		'6'      1463  -->    14    17    50   150   293   939
	rates:
		              '1'    '2'    '3'    '4'    '5'    '6'
		----------  -----  -----  -----  -----  -----  -----
		sample      0.168  0.167  0.168  0.167  0.166  0.164
		population  0.712  0.188  0.055  0.033  0.006  0.007
	match_rate (micro=0.494, macro=0.208):
		    1      2      3      4      5      6
		-----  -----  -----  -----  -----  -----
		0.635  0.161  0.144  0.081  0.118  0.108
	filter_rate (micro=0.506, macro=0.792):
		    1      2      3      4      5      6
		-----  -----  -----  -----  -----  -----
		0.365  0.839  0.856  0.919  0.882  0.892
	recall (micro=0.815, macro=0.612):
		    1      2      3      4      5      6
		-----  -----  -----  -----  -----  -----
		0.882  0.707  0.712  0.223  0.506  0.642
	!recall (micro=0.968, macro=0.923):
		    1      2      3      4      5      6
		-----  -----  -----  -----  -----  -----
		0.978  0.965  0.889  0.923  0.884  0.895
	precision (micro=0.878, macro=0.373):
		   1      2     3     4      5      6
		----  -----  ----  ----  -----  -----
		0.99  0.823  0.27  0.09  0.025  0.041
	!precision (micro=0.822, macro=0.942):
		    1      2      3      4      5      6
		-----  -----  -----  -----  -----  -----
		0.771  0.935  0.982  0.972  0.997  0.997
	f1 (micro=0.834, macro=0.39):
		    1      2      3      4      5      6
		-----  -----  -----  -----  -----  -----
		0.933  0.761  0.392  0.128  0.048  0.076
	!f1 (micro=0.886, macro=0.929):
		    1      2      3      4      5      6
		-----  -----  -----  -----  -----  -----
		0.862  0.949  0.933  0.947  0.937  0.944
	accuracy (micro=0.909, macro=0.897):
		   1      2      3    4      5      6
		----  -----  -----  ---  -----  -----
		0.91  0.917  0.879  0.9  0.882  0.894
	fpr (micro=0.032, macro=0.077):
		    1      2      3      4      5      6
		-----  -----  -----  -----  -----  -----
		0.022  0.035  0.111  0.077  0.116  0.105
	roc_auc (micro=0.963, macro=0.889):
		    1      2    3      4      5      6
		-----  -----  ---  -----  -----  -----
		0.982  0.951  0.9  0.764  0.847  0.892
	pr_auc (micro=0.9, macro=0.418):
		    1      2      3      4      5      6
		-----  -----  -----  -----  -----  -----
		0.993  0.878  0.449  0.088  0.047  0.053
	
	 - score_schema: {'type': 'object', 'properties': {'probability': {'type': 'object', 'description': 'A mapping of probabilities onto each of the potential output labels', 'properties': {'3': {'type': 'number'}, '4': {'type': 'number'}, '1': {'type': 'number'}, '5': {'type': 'number'}, '2': {'type': 'number'}, '6': {'type': 'number'}}}, 'prediction': {'type': 'string', 'description': 'The most likely label predicted by the estimator'}}, 'title': 'Scikit learn-based classifier score with probability'}

