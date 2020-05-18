Model Information:
	 - type: GradientBoosting
	 - version: 0.8.0
	 - params: {'multilabel': False, 'random_state': None, 'center': True, 'init': None, 'label_weights': None, 'n_iter_no_change': None, 'n_estimators': 300, 'scale': True, 'verbose': 0, 'subsample': 1.0, 'labels': ['1', '2', '3', '4', '5', '6'], 'min_weight_fraction_leaf': 0.0, 'max_depth': 7, 'max_leaf_nodes': None, 'learning_rate': 0.01, 'criterion': 'friedman_mse', 'validation_fraction': 0.1, 'min_samples_split': 2, 'loss': 'deviance', 'min_impurity_decrease': 0.0, 'warm_start': False, 'min_impurity_split': None, 'max_features': 'log2', 'tol': 0.0001, 'presort': 'auto', 'population_rates': None, 'min_samples_leaf': 1}
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
		'1'      1494  -->  1309   117    60     5     2     1
		'2'      1497  -->    87  1095   278    17    13     7
		'3'      1495  -->    42   115  1036   157   103    42
		'4'      1490  -->    18    38   300   315   455   364
		'5'      1483  -->    13    11   113   248   742   356
		'6'      1463  -->    16    22    55   166   278   926
	rates:
		              '1'    '2'    '3'    '4'    '5'    '6'
		----------  -----  -----  -----  -----  -----  -----
		sample      0.167  0.168  0.168  0.167  0.166  0.164
		population  0.712  0.188  0.055  0.033  0.006  0.007
	match_rate (micro=0.493, macro=0.208):
		    1     2     3      4      5      6
		-----  ----  ----  -----  -----  -----
		0.631  0.17  0.14  0.084  0.117  0.107
	filter_rate (micro=0.507, macro=0.792):
		    1     2     3      4      5      6
		-----  ----  ----  -----  -----  -----
		0.369  0.83  0.86  0.916  0.883  0.893
	recall (micro=0.813, macro=0.608):
		    1      2      3      4    5      6
		-----  -----  -----  -----  ---  -----
		0.876  0.731  0.693  0.211  0.5  0.633
	!recall (micro=0.966, macro=0.922):
		    1      2      3     4      5      6
		-----  -----  -----  ----  -----  -----
		0.976  0.959  0.891  0.92  0.886  0.897
	precision (micro=0.873, macro=0.369):
		    1      2      3      4      5      6
		-----  -----  -----  -----  -----  -----
		0.989  0.805  0.269  0.082  0.025  0.041
	!precision (micro=0.816, macro=0.941):
		    1      2      3      4      5      6
		-----  -----  -----  -----  -----  -----
		0.761  0.939  0.981  0.972  0.997  0.997
	f1 (micro=0.832, macro=0.388):
		    1      2      3      4      5      6
		-----  -----  -----  -----  -----  -----
		0.929  0.767  0.388  0.119  0.048  0.076
	!f1 (micro=0.881, macro=0.928):
		    1      2      3      4      5      6
		-----  -----  -----  -----  -----  -----
		0.855  0.949  0.934  0.945  0.938  0.944
	accuracy (micro=0.905, macro=0.896):
		    1      2      3      4      5      6
		-----  -----  -----  -----  -----  -----
		0.905  0.916  0.881  0.897  0.883  0.895
	fpr (micro=0.034, macro=0.078):
		    1      2      3     4      5      6
		-----  -----  -----  ----  -----  -----
		0.024  0.041  0.109  0.08  0.114  0.103
	roc_auc (micro=0.963, macro=0.889):
		    1      2      3      4      5      6
		-----  -----  -----  -----  -----  -----
		0.982  0.953  0.899  0.763  0.845  0.892
	pr_auc (micro=0.899, macro=0.413):
		    1     2      3      4      5      6
		-----  ----  -----  -----  -----  -----
		0.992  0.88  0.428  0.087  0.051  0.043
	
	 - score_schema: {'type': 'object', 'title': 'Scikit learn-based classifier score with probability', 'properties': {'probability': {'type': 'object', 'description': 'A mapping of probabilities onto each of the potential output labels', 'properties': {'4': {'type': 'number'}, '1': {'type': 'number'}, '2': {'type': 'number'}, '3': {'type': 'number'}, '6': {'type': 'number'}, '5': {'type': 'number'}}}, 'prediction': {'type': 'string', 'description': 'The most likely label predicted by the estimator'}}}

