Model Information:
	 - type: GradientBoosting
	 - version: 0.8.0
	 - params: {'min_weight_fraction_leaf': 0.0, 'init': None, 'loss': 'deviance', 'min_samples_split': 2, 'min_impurity_split': None, 'subsample': 1.0, 'max_features': 'log2', 'max_depth': 7, 'n_iter_no_change': None, 'warm_start': False, 'labels': ['1', '2', '3', '4', '5', '6'], 'label_weights': None, 'population_rates': None, 'center': True, 'n_estimators': 300, 'scale': True, 'learning_rate': 0.01, 'min_samples_leaf': 1, 'tol': 0.0001, 'random_state': None, 'min_impurity_decrease': 0.0, 'verbose': 0, 'multilabel': False, 'criterion': 'friedman_mse', 'max_leaf_nodes': None, 'presort': 'auto', 'validation_fraction': 0.1}
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
	counts (n=7147):
		label       n         ~1    ~2    ~3    ~4    ~5    ~6
		-------  ----  ---  ----  ----  ----  ----  ----  ----
		'1'      1197  -->  1018    95    71     7     2     4
		'2'      1199  -->    89   875   208    12    13     2
		'3'      1193  -->    32    70   823   131    99    38
		'4'      1189  -->    10    18   185   274   369   333
		'5'      1186  -->     9    11    46   197   689   234
		'6'      1183  -->    13    14    44   161   194   757
	rates:
		              '1'    '2'    '3'    '4'    '5'    '6'
		----------  -----  -----  -----  -----  -----  -----
		sample      0.167  0.168  0.167  0.166  0.166  0.166
		population  0.712  0.188  0.055  0.033  0.006  0.007
	match_rate (micro=0.479, macro=0.203):
		    1      2      3     4      5      6
		-----  -----  -----  ----  -----  -----
		0.613  0.165  0.126  0.09  0.116  0.106
	filter_rate (micro=0.521, macro=0.797):
		    1      2      3     4      5      6
		-----  -----  -----  ----  -----  -----
		0.387  0.835  0.874  0.91  0.884  0.894
	recall (micro=0.796, macro=0.62):
		   1     2     3     4      5     6
		----  ----  ----  ----  -----  ----
		0.85  0.73  0.69  0.23  0.581  0.64
	!recall (micro=0.966, macro=0.924):
		    1      2      3      4      5      6
		-----  -----  -----  -----  -----  -----
		0.974  0.965  0.907  0.915  0.886  0.898
	precision (micro=0.879, macro=0.378):
		    1      2    3      4     5      6
		-----  -----  ---  -----  ----  -----
		0.988  0.828  0.3  0.084  0.03  0.041
	!precision (micro=0.791, macro=0.935):
		    1      2      3      4      5      6
		-----  -----  -----  -----  -----  -----
		0.725  0.939  0.981  0.972  0.997  0.997
	f1 (micro=0.824, macro=0.394):
		    1      2      3      4      5      6
		-----  -----  -----  -----  -----  -----
		0.914  0.776  0.418  0.123  0.056  0.078
	!f1 (micro=0.865, macro=0.925):
		    1      2      3      4      5      6
		-----  -----  -----  -----  -----  -----
		0.831  0.952  0.942  0.943  0.939  0.945
	accuracy (micro=0.893, macro=0.896):
		    1      2      3      4      5      6
		-----  -----  -----  -----  -----  -----
		0.886  0.921  0.895  0.892  0.885  0.896
	fpr (micro=0.034, macro=0.076):
		    1      2      3      4      5      6
		-----  -----  -----  -----  -----  -----
		0.026  0.035  0.093  0.085  0.114  0.102
	roc_auc (micro=0.959, macro=0.893):
		    1      2      3      4      5      6
		-----  -----  -----  -----  -----  -----
		0.974  0.955  0.901  0.764  0.873  0.891
	pr_auc (micro=0.898, macro=0.415):
		   1      2      3      4      5      6
		----  -----  -----  -----  -----  -----
		0.99  0.885  0.427  0.077  0.055  0.055
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'properties': {'prediction': {'description': 'The most likely label predicted by the estimator', 'type': 'string'}, 'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'properties': {'4': {'type': 'number'}, '3': {'type': 'number'}, '2': {'type': 'number'}, '5': {'type': 'number'}, '6': {'type': 'number'}, '1': {'type': 'number'}}, 'type': 'object'}}, 'type': 'object'}

