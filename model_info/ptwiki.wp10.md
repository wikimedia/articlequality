Model Information:
	 - type: GradientBoosting
	 - version: 0.8.0
	 - params: {'population_rates': None, 'loss': 'deviance', 'center': True, 'min_weight_fraction_leaf': 0.0, 'tol': 0.0001, 'min_samples_split': 2, 'multilabel': False, 'n_estimators': 300, 'max_depth': 7, 'labels': ['1', '2', '3', '4', '5', '6'], 'validation_fraction': 0.1, 'label_weights': None, 'n_iter_no_change': None, 'subsample': 1.0, 'scale': True, 'min_impurity_decrease': 0.0, 'criterion': 'friedman_mse', 'verbose': 0, 'init': None, 'max_features': 'log2', 'random_state': None, 'presort': 'auto', 'warm_start': False, 'max_leaf_nodes': None, 'learning_rate': 0.01, 'min_samples_leaf': 1, 'min_impurity_split': None}
	Environment:
	 - revscoring_version: '2.7.2'
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
	counts (n=8922):
		label       n         ~1    ~2    ~3    ~4    ~5    ~6
		-------  ----  ---  ----  ----  ----  ----  ----  ----
		'1'      1494  -->  1311   118    55     7     2     1
		'2'      1497  -->    86  1098   278    16    12     7
		'3'      1495  -->    42   119  1026   166   104    38
		'4'      1490  -->    18    41   300   311   452   368
		'5'      1483  -->    10    17   112   234   745   365
		'6'      1463  -->    17    24    54   163   278   927
	rates:
		              '1'    '2'    '3'    '4'    '5'    '6'
		----------  -----  -----  -----  -----  -----  -----
		sample      0.167  0.168  0.168  0.167  0.166  0.164
		population  0.712  0.188  0.055  0.033  0.006  0.007
	match_rate (micro=0.494, macro=0.208):
		    1      2      3      4      5      6
		-----  -----  -----  -----  -----  -----
		0.632  0.173  0.139  0.083  0.116  0.108
	filter_rate (micro=0.506, macro=0.792):
		    1      2      3      4      5      6
		-----  -----  -----  -----  -----  -----
		0.368  0.827  0.861  0.917  0.884  0.892
	recall (micro=0.814, macro=0.607):
		    1      2      3      4      5      6
		-----  -----  -----  -----  -----  -----
		0.878  0.733  0.686  0.209  0.502  0.634
	!recall (micro=0.966, macro=0.921):
		    1      2      3      4      5      6
		-----  -----  -----  -----  -----  -----
		0.977  0.957  0.892  0.921  0.886  0.896
	precision (micro=0.872, macro=0.367):
		    1      2      3      4      5     6
		-----  -----  -----  -----  -----  ----
		0.989  0.798  0.269  0.082  0.026  0.04
	!precision (micro=0.818, macro=0.941):
		    1     2     3      4      5      6
		-----  ----  ----  -----  -----  -----
		0.763  0.94  0.98  0.972  0.997  0.997
	f1 (micro=0.832, macro=0.387):
		   1      2      3      4      5      6
		----  -----  -----  -----  -----  -----
		0.93  0.764  0.387  0.118  0.049  0.075
	!f1 (micro=0.882, macro=0.928):
		    1      2      3      4      5      6
		-----  -----  -----  -----  -----  -----
		0.857  0.948  0.934  0.946  0.938  0.944
	accuracy (micro=0.906, macro=0.896):
		    1      2      3      4      5      6
		-----  -----  -----  -----  -----  -----
		0.906  0.915  0.881  0.898  0.884  0.894
	fpr (micro=0.034, macro=0.079):
		    1      2      3      4      5      6
		-----  -----  -----  -----  -----  -----
		0.023  0.043  0.108  0.079  0.114  0.104
	roc_auc (micro=0.963, macro=0.889):
		    1      2      3      4      5      6
		-----  -----  -----  -----  -----  -----
		0.981  0.952  0.898  0.762  0.846  0.892
	pr_auc (micro=0.899, macro=0.415):
		    1      2      3      4      5      6
		-----  -----  -----  -----  -----  -----
		0.992  0.879  0.432  0.086  0.048  0.052
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'properties': {'probability': {'properties': {'6': {'type': 'number'}, '4': {'type': 'number'}, '5': {'type': 'number'}, '1': {'type': 'number'}, '3': {'type': 'number'}, '2': {'type': 'number'}}, 'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object'}, 'prediction': {'description': 'The most likely label predicted by the estimator', 'type': 'string'}}, 'type': 'object'}

