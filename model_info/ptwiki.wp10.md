Model Information:
	 - type: GradientBoosting
	 - version: 0.8.0
	 - params: {'tol': 0.0001, 'loss': 'deviance', 'max_depth': 7, 'population_rates': None, 'n_estimators': 300, 'criterion': 'friedman_mse', 'validation_fraction': 0.1, 'verbose': 0, 'min_impurity_decrease': 0.0, 'min_weight_fraction_leaf': 0.0, 'scale': True, 'min_impurity_split': None, 'min_samples_leaf': 1, 'n_iter_no_change': None, 'warm_start': False, 'labels': ['1', '2', '3', '4', '5', '6'], 'multilabel': False, 'min_samples_split': 2, 'init': None, 'label_weights': None, 'random_state': None, 'learning_rate': 0.01, 'center': True, 'max_features': 'log2', 'presort': 'auto', 'subsample': 1.0, 'max_leaf_nodes': None}
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
	counts (n=8574):
		label       n         ~1    ~2    ~3    ~4    ~5    ~6
		-------  ----  ---  ----  ----  ----  ----  ----  ----
		'1'      1489  -->  1261   129    87     3     7     2
		'2'      1497  -->   116  1040   301    15    19     6
		'3'      1494  -->    48    87  1048   190    70    51
		'4'      1489  -->    19    28   235   409   393   405
		'5'      1210  -->    12    17    66   259   619   237
		'6'      1395  -->    12    23    57   232   196   875
	rates:
		              '1'    '2'    '3'    '4'    '5'    '6'
		----------  -----  -----  -----  -----  -----  -----
		sample      0.174  0.175  0.174  0.174  0.141  0.163
		population  0.712  0.188  0.055  0.033  0.006  0.007
	match_rate (micro=0.478, macro=0.202):
		    1      2      3      4      5      6
		-----  -----  -----  -----  -----  -----
		0.612  0.163  0.138  0.104  0.096  0.101
	filter_rate (micro=0.522, macro=0.798):
		    1      2      3      4      5      6
		-----  -----  -----  -----  -----  -----
		0.388  0.837  0.862  0.896  0.904  0.899
	recall (micro=0.788, macro=0.609):
		    1      2      3      4      5      6
		-----  -----  -----  -----  -----  -----
		0.847  0.695  0.701  0.275  0.512  0.627
	!recall (micro=0.961, macro=0.923):
		    1     2      3      4      5      6
		-----  ----  -----  -----  -----  -----
		0.971  0.96  0.895  0.901  0.907  0.902
	precision (micro=0.871, macro=0.371):
		    1    2      3      4      5      6
		-----  ---  -----  -----  -----  -----
		0.986  0.8  0.278  0.086  0.032  0.042
	!precision (micro=0.785, macro=0.933):
		    1      2      3      4      5      6
		-----  -----  -----  -----  -----  -----
		0.719  0.932  0.981  0.973  0.997  0.997
	f1 (micro=0.815, macro=0.387):
		    1      2      3      4     5      6
		-----  -----  -----  -----  ----  -----
		0.911  0.744  0.398  0.131  0.06  0.079
	!f1 (micro=0.86, macro=0.923):
		    1      2      3      4     5      6
		-----  -----  -----  -----  ----  -----
		0.826  0.946  0.936  0.936  0.95  0.947
	accuracy (micro=0.888, macro=0.894):
		    1     2      3      4      5    6
		-----  ----  -----  -----  -----  ---
		0.883  0.91  0.884  0.881  0.905  0.9
	fpr (micro=0.039, macro=0.077):
		    1     2      3      4      5      6
		-----  ----  -----  -----  -----  -----
		0.029  0.04  0.105  0.099  0.093  0.098
	roc_auc (micro=0.955, macro=0.893):
		    1      2      3      4      5      6
		-----  -----  -----  -----  -----  -----
		0.973  0.941  0.898  0.778  0.875  0.895
	pr_auc (micro=0.891, macro=0.41):
		    1      2      3      4      5      6
		-----  -----  -----  -----  -----  -----
		0.988  0.856  0.418  0.085  0.055  0.057
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'properties': {'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'properties': {'2': {'type': 'number'}, '6': {'type': 'number'}, '5': {'type': 'number'}, '4': {'type': 'number'}, '1': {'type': 'number'}, '3': {'type': 'number'}}, 'type': 'object'}, 'prediction': {'description': 'The most likely label predicted by the estimator', 'type': 'string'}}, 'type': 'object'}

