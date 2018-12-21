Model Information:
	 - type: GradientBoosting
	 - version: 0.8.0
	 - params: {'min_impurity_decrease': 0.0, 'multilabel': False, 'criterion': 'friedman_mse', 'max_depth': 5, 'scale': True, 'min_samples_split': 2, 'labels': ['IV', 'III', 'II', 'I', 'ХС', 'ДС', 'ИС'], 'max_features': 'log2', 'warm_start': False, 'min_samples_leaf': 1, 'init': None, 'loss': 'deviance', 'random_state': None, 'max_leaf_nodes': None, 'subsample': 1.0, 'min_weight_fraction_leaf': 0.0, 'presort': 'auto', 'min_impurity_split': None, 'learning_rate': 0.01, 'verbose': 0, 'n_estimators': 300, 'population_rates': None, 'center': True, 'label_weights': None}
	Environment:
	 - revscoring_version: '2.3.0'
	 - platform: 'Linux-4.9.0-8-amd64-x86_64-with-debian-9.5'
	 - machine: 'x86_64'
	 - version: '#1 SMP Debian 4.9.110-3+deb9u6 (2018-10-08)'
	 - system: 'Linux'
	 - processor: ''
	 - python_build: ('default', 'Jan 19 2017 14:11:04')
	 - python_compiler: 'GCC 6.3.0 20170118'
	 - python_branch: ''
	 - python_implementation: 'CPython'
	 - python_revision: ''
	 - python_version: '3.5.3'
	 - release: '4.9.0-8-amd64'
	
	Statistics:
	counts (n=10282):
		label       n         ~IV    ~III    ~II    ~I    ~ХС    ~ДС    ~ИС
		-------  ----  ---  -----  ------  -----  ----  -----  -----  -----
		'IV'     1465  -->   1080     289     55     5      4     26      6
		'III'    1465  -->    392     632    268    35     14    113     11
		'II'     1461  -->     98     290    504   148    114    271     36
		'I'      1458  -->     50     100    252   240    364    286    166
		'ХС'     1469  -->     12      14     33   114    919    109    268
		'ДС'     1488  -->      0      61     56    29    108   1223     11
		'ИС'     1476  -->     13      18     15    52    282     53   1043
	rates:
		              'IV'    'III'    'II'    'I'    'ХС'    'ДС'    'ИС'
		----------  ------  -------  ------  -----  ------  ------  ------
		sample       0.142    0.142   0.142  0.142   0.143   0.145   0.144
		population   0.487    0.363   0.093  0.029   0.011   0.009   0.007
	match_rate (micro=0.281, macro=0.146):
		   IV      I    III     ХС     ДС     II     ИС
		-----  -----  -----  -----  -----  -----  -----
		0.392  0.047  0.212  0.107  0.104  0.102  0.061
	filter_rate (micro=0.719, macro=0.854):
		   IV      I    III     ХС     ДС     II     ИС
		-----  -----  -----  -----  -----  -----  -----
		0.608  0.953  0.788  0.893  0.896  0.898  0.939
	recall (micro=0.573, macro=0.547):
		   IV      I    III     ХС     ДС     II     ИС
		-----  -----  -----  -----  -----  -----  -----
		0.737  0.165  0.431  0.626  0.822  0.345  0.707
	!recall (micro=0.926, macro=0.925):
		   IV      I    III     ХС     ДС     II     ИС
		-----  -----  -----  -----  -----  -----  -----
		0.936  0.957  0.912  0.899  0.902  0.923  0.943
	precision (micro=0.748, macro=0.328):
		   IV      I    III     ХС     ДС     II     ИС
		-----  -----  -----  -----  -----  -----  -----
		0.916  0.102  0.737  0.067  0.073  0.315  0.086
	!precision (micro=0.795, macro=0.918):
		   IV      I    III     ХС     ДС     II     ИС
		-----  -----  -----  -----  -----  -----  -----
		0.789  0.975  0.738  0.995  0.998  0.932  0.998
	f1 (micro=0.633, macro=0.318):
		   IV      I    III     ХС     ДС     II     ИС
		-----  -----  -----  -----  -----  -----  -----
		0.817  0.126  0.544  0.121  0.134  0.329  0.153
	!f1 (micro=0.854, macro=0.918):
		   IV      I    III     ХС     ДС     II    ИС
		-----  -----  -----  -----  -----  -----  ----
		0.856  0.965  0.816  0.945  0.948  0.928  0.97
	accuracy (micro=0.81, macro=0.874):
		   IV      I    III     ХС     ДС     II     ИС
		-----  -----  -----  -----  -----  -----  -----
		0.839  0.934  0.738  0.896  0.902  0.869  0.942
	fpr (micro=0.074, macro=0.075):
		   IV      I    III     ХС     ДС     II     ИС
		-----  -----  -----  -----  -----  -----  -----
		0.064  0.043  0.088  0.101  0.098  0.077  0.057
	roc_auc (micro=0.889, macro=0.871):
		   IV      I    III     ХС     ДС     II     ИС
		-----  -----  -----  -----  -----  -----  -----
		0.941  0.736  0.854  0.898  0.941  0.792  0.937
	pr_auc (micro=0.749, macro=0.358):
		   IV      I    III     ХС     ДС     II     ИС
		-----  -----  -----  -----  -----  -----  -----
		0.923  0.088  0.737  0.085  0.127  0.268  0.278
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'probability': {'properties': {'IV': {'type': 'number'}, 'I': {'type': 'number'}, 'III': {'type': 'number'}, 'ХС': {'type': 'number'}, 'ДС': {'type': 'number'}, 'II': {'type': 'number'}, 'ИС': {'type': 'number'}}, 'type': 'object', 'description': 'A mapping of probabilities onto each of the potential output labels'}, 'prediction': {'type': 'string', 'description': 'The most likely label predicted by the estimator'}}}

