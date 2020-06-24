Model Information:
	 - type: GradientBoosting
	 - version: 0.8.0
	 - params: {'loss': 'deviance', 'subsample': 1.0, 'init': None, 'criterion': 'friedman_mse', 'min_samples_split': 2, 'validation_fraction': 0.1, 'presort': 'deprecated', 'tol': 0.0001, 'min_impurity_split': None, 'population_rates': None, 'random_state': None, 'n_iter_no_change': None, 'warm_start': False, 'labels': ['1', '2', '3', '4', '5', '6'], 'label_weights': None, 'verbose': 0, 'multilabel': False, 'max_leaf_nodes': None, 'min_weight_fraction_leaf': 0.0, 'n_estimators': 100, 'max_depth': 7, 'max_features': 'log2', 'scale': True, 'learning_rate': 0.01, 'ccp_alpha': 0.0, 'min_impurity_decrease': 0.0, 'center': True, 'min_samples_leaf': 1}
	Environment:
	 - revscoring_version: '2.8.2'
	 - platform: 'Linux-4.9.0-12-amd64-x86_64-with-debian-9.12'
	 - machine: 'x86_64'
	 - version: '#1 SMP Debian 4.9.210-1+deb9u1 (2020-06-07)'
	 - system: 'Linux'
	 - processor: ''
	 - python_build: ('default', 'Sep 27 2018 17:25:39')
	 - python_compiler: 'GCC 6.3.0 20170516'
	 - python_branch: ''
	 - python_implementation: 'CPython'
	 - python_revision: ''
	 - python_version: '3.5.3'
	 - release: '4.9.0-12-amd64'
	
	Statistics:
	counts (n=3888):
		label      n         ~1    ~2    ~3    ~4    ~5    ~6
		-------  ---  ---  ----  ----  ----  ----  ----  ----
		'1'      632  -->   429   171    23     2     6     1
		'2'      653  -->   115   394    99     9    32     4
		'3'      649  -->    50   142   283    62    90    22
		'4'      651  -->    20    47    83   116   188   197
		'5'      650  -->     6    19    42    82   379   122
		'6'      653  -->    16    34    26    92   129   356
	rates:
		              '1'    '2'    '3'    '4'    '5'    '6'
		----------  -----  -----  -----  -----  -----  -----
		sample      0.163  0.168  0.167  0.167  0.167  0.168
		population  0.531  0.236  0.09   0.049  0.046  0.048
	match_rate (micro=0.292, macro=0.186):
		   1     2      3      4      5      6
		----  ----  -----  -----  -----  -----
		0.39  0.24  0.116  0.081  0.158  0.128
	filter_rate (micro=0.708, macro=0.814):
		   1     2      3      4      5      6
		----  ----  -----  -----  -----  -----
		0.61  0.76  0.884  0.919  0.842  0.872
	recall (micro=0.604, macro=0.504):
		    1      2      3      4      5      6
		-----  -----  -----  -----  -----  -----
		0.679  0.603  0.436  0.178  0.583  0.545
	!recall (micro=0.913, macro=0.901):
		    1      2      3      4      5      6
		-----  -----  -----  -----  -----  -----
		0.936  0.872  0.916  0.924  0.863  0.893
	precision (micro=0.684, macro=0.39):
		    1      2      3      4     5      6
		-----  -----  -----  -----  ----  -----
		0.924  0.593  0.338  0.107  0.17  0.205
	!precision (micro=0.813, macro=0.908):
		   1      2      3      4      5      6
		----  -----  -----  -----  -----  -----
		0.72  0.877  0.943  0.956  0.977  0.975
	f1 (micro=0.624, macro=0.409):
		    1      2      3      4      5      6
		-----  -----  -----  -----  -----  -----
		0.783  0.598  0.381  0.133  0.263  0.298
	!f1 (micro=0.855, macro=0.901):
		    1      2      3     4      5      6
		-----  -----  -----  ----  -----  -----
		0.814  0.875  0.929  0.94  0.916  0.932
	accuracy (micro=0.819, macro=0.849):
		  1      2      3      4     5      6
		---  -----  -----  -----  ----  -----
		0.8  0.809  0.873  0.887  0.85  0.876
	fpr (micro=0.087, macro=0.099):
		    1      2      3      4      5      6
		-----  -----  -----  -----  -----  -----
		0.064  0.128  0.084  0.076  0.137  0.107
	roc_auc (micro=0.889, macro=0.836):
		   1      2      3      4     5      6
		----  -----  -----  -----  ----  -----
		0.94  0.861  0.802  0.719  0.85  0.845
	pr_auc (micro=0.709, macro=0.411):
		    1      2      3      4      5      6
		-----  -----  -----  -----  -----  -----
		0.937  0.664  0.329  0.092  0.232  0.211
	
	 - score_schema: {'type': 'object', 'properties': {'probability': {'type': 'object', 'properties': {'6': {'type': 'number'}, '5': {'type': 'number'}, '3': {'type': 'number'}, '2': {'type': 'number'}, '4': {'type': 'number'}, '1': {'type': 'number'}}, 'description': 'A mapping of probabilities onto each of the potential output labels'}, 'prediction': {'type': 'string', 'description': 'The most likely label predicted by the estimator'}}, 'title': 'Scikit learn-based classifier score with probability'}

