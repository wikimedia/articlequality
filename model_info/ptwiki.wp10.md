Model Information:
	 - type: GradientBoosting
	 - version: 0.8.0
	 - params: {'scale': True, 'learning_rate': 0.01, 'criterion': 'friedman_mse', 'labels': ['1', '2', '3', '4', '5', '6'], 'center': True, 'min_weight_fraction_leaf': 0.0, 'loss': 'deviance', 'tol': 0.0001, 'max_features': 'log2', 'multilabel': False, 'n_iter_no_change': None, 'n_estimators': 300, 'min_impurity_decrease': 0.0, 'max_depth': 7, 'validation_fraction': 0.1, 'min_samples_leaf': 1, 'min_impurity_split': None, 'init': None, 'max_leaf_nodes': None, 'random_state': None, 'min_samples_split': 2, 'warm_start': False, 'label_weights': None, 'verbose': 0, 'subsample': 1.0, 'population_rates': None, 'presort': 'auto'}
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
	counts (n=7151):
		label       n         ~1    ~2    ~3    ~4    ~5    ~6
		-------  ----  ---  ----  ----  ----  ----  ----  ----
		'1'      1197  -->  1052    82    58     3     1     1
		'2'      1198  -->    82   874   211    14    12     5
		'3'      1196  -->    34    89   831   120    86    36
		'4'      1192  -->    14    26   208   249   370   325
		'5'      1186  -->    10    16    53   161   717   229
		'6'      1182  -->    11    20    50   158   202   741
	rates:
		              '1'    '2'    '3'    '4'    '5'    '6'
		----------  -----  -----  -----  -----  -----  -----
		sample      0.167  0.168  0.167  0.167  0.166  0.165
		population  0.712  0.188  0.055  0.033  0.006  0.007
	match_rate (micro=0.494, macro=0.205):
		    1      2     3      4      5      6
		-----  -----  ----  -----  -----  -----
		0.633  0.169  0.13  0.081  0.115  0.103
	filter_rate (micro=0.506, macro=0.795):
		    1      2     3      4      5      6
		-----  -----  ----  -----  -----  -----
		0.367  0.831  0.87  0.919  0.885  0.897
	recall (micro=0.815, macro=0.624):
		    1     2      3      4      5      6
		-----  ----  -----  -----  -----  -----
		0.879  0.73  0.695  0.209  0.605  0.627
	!recall (micro=0.965, macro=0.925):
		    1      2      3      4      5    6
		-----  -----  -----  -----  -----  ---
		0.975  0.961  0.903  0.923  0.888  0.9
	precision (micro=0.875, macro=0.375):
		    1      2      3      4      5      6
		-----  -----  -----  -----  -----  -----
		0.988  0.812  0.292  0.085  0.031  0.041
	!precision (micro=0.819, macro=0.942):
		    1      2      3      4      5      6
		-----  -----  -----  -----  -----  -----
		0.765  0.939  0.981  0.972  0.997  0.997
	f1 (micro=0.834, macro=0.395):
		   1      2      3      4      5      6
		----  -----  -----  -----  -----  -----
		0.93  0.768  0.411  0.121  0.059  0.078
	!f1 (micro=0.883, macro=0.93):
		    1     2     3      4      5      6
		-----  ----  ----  -----  -----  -----
		0.857  0.95  0.94  0.947  0.939  0.946
	accuracy (micro=0.907, macro=0.9):
		    1      2      3    4      5      6
		-----  -----  -----  ---  -----  -----
		0.906  0.917  0.891  0.9  0.886  0.898
	fpr (micro=0.035, macro=0.075):
		    1      2      3      4      5    6
		-----  -----  -----  -----  -----  ---
		0.025  0.039  0.097  0.077  0.112  0.1
	roc_auc (micro=0.962, macro=0.894):
		   1      2      3      4      5      6
		----  -----  -----  -----  -----  -----
		0.98  0.951  0.904  0.762  0.876  0.892
	pr_auc (micro=0.898, macro=0.416):
		    1      2      3      4      5      6
		-----  -----  -----  -----  -----  -----
		0.992  0.881  0.422  0.083  0.058  0.056
	
	 - score_schema: {'properties': {'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'properties': {'1': {'type': 'number'}, '3': {'type': 'number'}, '4': {'type': 'number'}, '2': {'type': 'number'}, '5': {'type': 'number'}, '6': {'type': 'number'}}, 'type': 'object'}, 'prediction': {'description': 'The most likely label predicted by the estimator', 'type': 'string'}}, 'title': 'Scikit learn-based classifier score with probability', 'type': 'object'}

