Model Information:
	 - type: GradientBoosting
	 - version: 0.8.0
	 - params: {'scale': True, 'max_leaf_nodes': None, 'n_estimators': 100, 'verbose': 0, 'n_iter_no_change': None, 'multilabel': False, 'tol': 0.0001, 'validation_fraction': 0.1, 'max_depth': 7, 'population_rates': None, 'warm_start': False, 'init': None, 'max_features': 'log2', 'loss': 'deviance', 'min_samples_split': 2, 'center': True, 'min_impurity_split': None, 'min_weight_fraction_leaf': 0.0, 'random_state': None, 'criterion': 'friedman_mse', 'learning_rate': 0.01, 'label_weights': None, 'labels': ['1', '2', '3', '4', '5', '6'], 'min_impurity_decrease': 0.0, 'min_samples_leaf': 1, 'presort': 'auto', 'subsample': 1.0}
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
	counts (n=3884):
		label      n         ~1    ~2    ~3    ~4    ~5    ~6
		-------  ---  ---  ----  ----  ----  ----  ----  ----
		'1'      625  -->   441   145    25     4     7     3
		'2'      653  -->   114   381   103    16    32     7
		'3'      652  -->    46   163   279    62    77    25
		'4'      651  -->    20    47    85   106   196   197
		'5'      650  -->     6    24    45    88   370   117
		'6'      653  -->    23    25    29   103   120   353
	rates:
		              '1'    '2'    '3'    '4'    '5'    '6'
		----------  -----  -----  -----  -----  -----  -----
		sample      0.161  0.168  0.168  0.168  0.167  0.168
		population  0.531  0.236  0.09   0.049  0.046  0.048
	match_rate (micro=0.298, macro=0.188):
		    1      2      3      4      5      6
		-----  -----  -----  -----  -----  -----
		0.405  0.233  0.119  0.088  0.154  0.129
	filter_rate (micro=0.702, macro=0.812):
		    1      2      3      4      5      6
		-----  -----  -----  -----  -----  -----
		0.595  0.767  0.881  0.912  0.846  0.871
	recall (micro=0.611, macro=0.498):
		    1      2      3      4      5      6
		-----  -----  -----  -----  -----  -----
		0.706  0.583  0.428  0.163  0.569  0.541
	!recall (micro=0.913, macro=0.899):
		    1      2      3      4      5      6
		-----  -----  -----  -----  -----  -----
		0.936  0.875  0.911  0.916  0.866  0.892
	precision (micro=0.682, macro=0.384):
		    1     2      3     4      5      6
		-----  ----  -----  ----  -----  -----
		0.926  0.59  0.323  0.09  0.171  0.202
	!precision (micro=0.82, macro=0.91):
		    1      2      3      4      5      6
		-----  -----  -----  -----  -----  -----
		0.737  0.872  0.942  0.955  0.977  0.975
	f1 (micro=0.629, macro=0.405):
		    1      2      3      4      5      6
		-----  -----  -----  -----  -----  -----
		0.801  0.587  0.368  0.116  0.262  0.294
	!f1 (micro=0.86, macro=0.901):
		    1      2      3      4      5      6
		-----  -----  -----  -----  -----  -----
		0.825  0.873  0.926  0.935  0.918  0.931
	accuracy (micro=0.825, macro=0.849):
		    1      2      3      4      5      6
		-----  -----  -----  -----  -----  -----
		0.814  0.806  0.868  0.879  0.853  0.875
	fpr (micro=0.087, macro=0.101):
		    1      2      3      4      5      6
		-----  -----  -----  -----  -----  -----
		0.064  0.125  0.089  0.084  0.134  0.108
	roc_auc (micro=0.886, macro=0.835):
		    1      2      3      4      5      6
		-----  -----  -----  -----  -----  -----
		0.934  0.859  0.803  0.722  0.849  0.841
	pr_auc (micro=0.705, macro=0.408):
		    1      2      3      4      5    6
		-----  -----  -----  -----  -----  ---
		0.936  0.643  0.353  0.089  0.229  0.2
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'properties': {'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'properties': {'5': {'type': 'number'}, '1': {'type': 'number'}, '2': {'type': 'number'}, '3': {'type': 'number'}, '4': {'type': 'number'}, '6': {'type': 'number'}}, 'type': 'object'}, 'prediction': {'description': 'The most likely label predicted by the estimator', 'type': 'string'}}, 'type': 'object'}

