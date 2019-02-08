Model Information:
	 - type: GradientBoosting
	 - version: 0.8.0
	 - params: {'verbose': 0, 'criterion': 'friedman_mse', 'learning_rate': 0.01, 'presort': 'auto', 'min_impurity_split': None, 'random_state': None, 'min_samples_split': 2, 'label_weights': None, 'subsample': 1.0, 'max_features': 'log2', 'warm_start': False, 'max_depth': 5, 'min_weight_fraction_leaf': 0.0, 'n_estimators': 300, 'center': True, 'labels': ['IV', 'III', 'II', 'I', 'ХС', 'ДС', 'ИС'], 'multilabel': False, 'loss': 'deviance', 'scale': True, 'population_rates': None, 'min_impurity_decrease': 0.0, 'init': None, 'max_leaf_nodes': None, 'min_samples_leaf': 1}
	Environment:
	 - revscoring_version: '2.3.4'
	 - platform: 'Linux-4.9.0-8-amd64-x86_64-with-debian-9.5'
	 - machine: 'x86_64'
	 - version: '#1 SMP Debian 4.9.110-3+deb9u6 (2018-10-08)'
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
	counts (n=10282):
		label       n         ~IV    ~III    ~II    ~I    ~ХС    ~ДС    ~ИС
		-------  ----  ---  -----  ------  -----  ----  -----  -----  -----
		'IV'     1465  -->   1082     288     55     4      4     26      6
		'III'    1465  -->    395     636    269    33     15    107     10
		'II'     1461  -->     96     292    499   152    113    270     39
		'I'      1458  -->     52     102    252   243    357    280    172
		'ХС'     1469  -->     10      16     37   112    906    111    277
		'ДС'     1488  -->      0      59     60    31    109   1218     11
		'ИС'     1476  -->     12      17     17    49    273     54   1054
	rates:
		              'IV'    'III'    'II'    'I'    'ХС'    'ДС'    'ИС'
		----------  ------  -------  ------  -----  ------  ------  ------
		sample       0.142    0.142   0.142  0.142   0.143   0.145   0.144
		population   0.487    0.363   0.093  0.029   0.011   0.009   0.007
	match_rate (micro=0.282, macro=0.147):
		   ДС     ХС     ИС     II    III     IV      I
		-----  -----  -----  -----  -----  -----  -----
		0.103  0.105  0.063  0.103  0.213  0.393  0.047
	filter_rate (micro=0.718, macro=0.853):
		   ДС     ХС     ИС     II    III     IV      I
		-----  -----  -----  -----  -----  -----  -----
		0.897  0.895  0.937  0.897  0.787  0.607  0.953
	recall (micro=0.574, macro=0.547):
		   ДС     ХС     ИС     II    III     IV      I
		-----  -----  -----  -----  -----  -----  -----
		0.819  0.617  0.714  0.342  0.434  0.739  0.167
	!recall (micro=0.926, macro=0.925):
		   ДС     ХС     ИС     II    III     IV      I
		-----  -----  -----  -----  -----  -----  -----
		0.904  0.901  0.942  0.922  0.912  0.936  0.957
	precision (micro=0.748, macro=0.327):
		   ДС     ХС     ИС     II    III     IV      I
		-----  -----  -----  -----  -----  -----  -----
		0.074  0.067  0.084  0.309  0.738  0.916  0.103
	!precision (micro=0.796, macro=0.918):
		   ДС     ХС     ИС     II    III    IV      I
		-----  -----  -----  -----  -----  ----  -----
		0.998  0.995  0.998  0.932  0.739  0.79  0.975
	f1 (micro=0.634, macro=0.318):
		   ДС     ХС     ИС     II    III     IV      I
		-----  -----  -----  -----  -----  -----  -----
		0.135  0.121  0.151  0.325  0.547  0.818  0.128
	!f1 (micro=0.855, macro=0.918):
		   ДС     ХС     ИС     II    III     IV      I
		-----  -----  -----  -----  -----  -----  -----
		0.948  0.946  0.969  0.927  0.817  0.857  0.966
	accuracy (micro=0.811, macro=0.874):
		   ДС     ХС    ИС     II    III    IV      I
		-----  -----  ----  -----  -----  ----  -----
		0.903  0.898  0.94  0.868  0.739  0.84  0.934
	fpr (micro=0.074, macro=0.075):
		   ДС     ХС     ИС     II    III     IV      I
		-----  -----  -----  -----  -----  -----  -----
		0.096  0.099  0.058  0.078  0.088  0.064  0.043
	roc_auc (micro=0.889, macro=0.871):
		   ДС     ХС     ИС     II    III     IV      I
		-----  -----  -----  -----  -----  -----  -----
		0.941  0.898  0.937  0.791  0.853  0.941  0.736
	pr_auc (micro=0.749, macro=0.36):
		   ДС     ХС    ИС     II    III     IV     I
		-----  -----  ----  -----  -----  -----  ----
		0.126  0.085  0.28  0.277  0.735  0.923  0.09
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'probability': {'type': 'object', 'properties': {'ДС': {'type': 'number'}, 'ХС': {'type': 'number'}, 'ИС': {'type': 'number'}, 'II': {'type': 'number'}, 'III': {'type': 'number'}, 'IV': {'type': 'number'}, 'I': {'type': 'number'}}, 'description': 'A mapping of probabilities onto each of the potential output labels'}, 'prediction': {'type': 'string', 'description': 'The most likely label predicted by the estimator'}}}

