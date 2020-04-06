Model Information:
	 - type: GradientBoosting
	 - version: 0.8.0
	 - params: {'scale': True, 'max_features': 'log2', 'verbose': 0, 'presort': 'auto', 'label_weights': None, 'population_rates': None, 'multilabel': False, 'center': True, 'warm_start': False, 'tol': 0.0001, 'max_leaf_nodes': None, 'subsample': 1.0, 'min_samples_split': 2, 'n_estimators': 300, 'init': None, 'n_iter_no_change': None, 'criterion': 'friedman_mse', 'min_weight_fraction_leaf': 0.0, 'validation_fraction': 0.1, 'min_impurity_decrease': 0.0, 'max_depth': 7, 'min_impurity_split': None, 'loss': 'deviance', 'labels': ['1', '2', '3', '4', '5', '6'], 'min_samples_leaf': 1, 'random_state': None, 'learning_rate': 0.01}
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
	counts (n=7137):
		label       n         ~1    ~2    ~3    ~4    ~5    ~6
		-------  ----  ---  ----  ----  ----  ----  ----  ----
		'1'      1198  -->   975    32   104    79     5     3
		'2'      1186  -->    69   723   250    95    35    14
		'3'      1192  -->    74    79   644   251   107    37
		'4'      1192  -->    79    41   323   442   152   155
		'5'      1187  -->     6    23    36    32   812   278
		'6'      1182  -->     7    15    39    37   242   842
	rates:
		              '1'    '2'    '3'    '4'    '5'    '6'
		----------  -----  -----  -----  -----  -----  -----
		sample      0.168  0.166  0.167  0.167  0.166  0.166
		population  0.712  0.188  0.055  0.033  0.006  0.007
	match_rate (micro=0.46, macro=0.192):
		    1     2      3      4      5      6
		-----  ----  -----  -----  -----  -----
		0.591  0.14  0.149  0.093  0.094  0.086
	filter_rate (micro=0.54, macro=0.808):
		    1     2      3      4      5      6
		-----  ----  -----  -----  -----  -----
		0.409  0.86  0.851  0.907  0.906  0.914
	recall (micro=0.745, macro=0.622):
		    1     2     3      4      5      6
		-----  ----  ----  -----  -----  -----
		0.814  0.61  0.54  0.371  0.684  0.712
	!recall (micro=0.955, macro=0.924):
		   1      2      3      4      5      6
		----  -----  -----  -----  -----  -----
		0.96  0.968  0.874  0.917  0.909  0.918
	precision (micro=0.867, macro=0.371):
		    1      2      3      4      5      6
		-----  -----  -----  -----  -----  -----
		0.981  0.815  0.198  0.131  0.043  0.057
	!precision (micro=0.751, macro=0.922):
		    1      2      3      4      5      6
		-----  -----  -----  -----  -----  -----
		0.676  0.915  0.971  0.977  0.998  0.998
	f1 (micro=0.788, macro=0.376):
		   1      2     3      4      5      6
		----  -----  ----  -----  -----  -----
		0.89  0.698  0.29  0.194  0.081  0.105
	!f1 (micro=0.835, macro=0.918):
		    1      2      3      4      5      6
		-----  -----  -----  -----  -----  -----
		0.793  0.941  0.919  0.946  0.951  0.956
	accuracy (micro=0.867, macro=0.889):
		    1      2      3      4      5      6
		-----  -----  -----  -----  -----  -----
		0.856  0.901  0.855  0.899  0.908  0.917
	fpr (micro=0.045, macro=0.076):
		   1      2      3      4      5      6
		----  -----  -----  -----  -----  -----
		0.04  0.032  0.126  0.083  0.091  0.082
	roc_auc (micro=0.939, macro=0.889):
		    1      2      3     4      5      6
		-----  -----  -----  ----  -----  -----
		0.962  0.909  0.852  0.78  0.914  0.919
	pr_auc (micro=0.875, macro=0.406):
		    1      2      3      4      5     6
		-----  -----  -----  -----  -----  ----
		0.984  0.803  0.311  0.151  0.106  0.08
	
	 - score_schema: {'properties': {'probability': {'properties': {'6': {'type': 'number'}, '1': {'type': 'number'}, '2': {'type': 'number'}, '5': {'type': 'number'}, '3': {'type': 'number'}, '4': {'type': 'number'}}, 'type': 'object', 'description': 'A mapping of probabilities onto each of the potential output labels'}, 'prediction': {'type': 'string', 'description': 'The most likely label predicted by the estimator'}}, 'type': 'object', 'title': 'Scikit learn-based classifier score with probability'}

