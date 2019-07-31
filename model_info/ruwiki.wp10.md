Model Information:
	 - type: GradientBoosting
	 - version: 0.8.0
	 - params: {'labels': ['IV', 'III', 'II', 'I', 'ХС', 'ДС', 'ИС'], 'min_samples_leaf': 1, 'loss': 'deviance', 'min_impurity_decrease': 0.0, 'tol': 0.0001, 'criterion': 'friedman_mse', 'subsample': 1.0, 'init': None, 'population_rates': None, 'scale': True, 'max_features': 'log2', 'warm_start': False, 'verbose': 0, 'min_weight_fraction_leaf': 0.0, 'label_weights': None, 'multilabel': False, 'learning_rate': 0.01, 'n_estimators': 300, 'max_leaf_nodes': None, 'presort': 'auto', 'min_impurity_split': None, 'center': True, 'min_samples_split': 2, 'n_iter_no_change': None, 'max_depth': 5, 'random_state': None, 'validation_fraction': 0.1}
	Environment:
	 - revscoring_version: '2.5.1'
	 - platform: 'Linux-4.9.0-9-amd64-x86_64-with-debian-9.9'
	 - machine: 'x86_64'
	 - version: '#1 SMP Debian 4.9.168-1+deb9u2 (2019-05-13)'
	 - system: 'Linux'
	 - processor: ''
	 - python_build: ('default', 'Sep 27 2018 17:25:39')
	 - python_compiler: 'GCC 6.3.0 20170516'
	 - python_branch: ''
	 - python_implementation: 'CPython'
	 - python_revision: ''
	 - python_version: '3.5.3'
	 - release: '4.9.0-9-amd64'
	
	Statistics:
	counts (n=10282):
		label       n         ~IV    ~III    ~II    ~I    ~ХС    ~ДС    ~ИС
		-------  ----  ---  -----  ------  -----  ----  -----  -----  -----
		'IV'     1465  -->   1075     299     54     3      4     25      5
		'III'    1465  -->    392     635    274    28     15    111     10
		'II'     1461  -->     95     294    514   145    108    265     40
		'I'      1458  -->     50     101    257   240    366    275    169
		'ХС'     1469  -->     10      16     38   119    903    110    273
		'ДС'     1488  -->      2      56     61    31    110   1217     11
		'ИС'     1476  -->     13      16     14    52    274     54   1053
	rates:
		              'IV'    'III'    'II'    'I'    'ХС'    'ДС'    'ИС'
		----------  ------  -------  ------  -----  ------  ------  ------
		sample       0.142    0.142   0.142  0.142   0.143   0.145   0.144
		population   0.487    0.363   0.093  0.029   0.011   0.009   0.007
	match_rate (micro=0.281, macro=0.146):
		  IV     ДС     ИС     II      I     ХС    III
		----  -----  -----  -----  -----  -----  -----
		0.39  0.102  0.063  0.104  0.046  0.105  0.214
	filter_rate (micro=0.719, macro=0.854):
		  IV     ДС     ИС     II      I     ХС    III
		----  -----  -----  -----  -----  -----  -----
		0.61  0.898  0.937  0.896  0.954  0.895  0.786
	recall (micro=0.572, macro=0.547):
		   IV     ДС     ИС     II      I     ХС    III
		-----  -----  -----  -----  -----  -----  -----
		0.734  0.818  0.713  0.352  0.165  0.615  0.433
	!recall (micro=0.926, macro=0.925):
		   IV     ДС     ИС     II      I    ХС    III
		-----  -----  -----  -----  -----  ----  -----
		0.936  0.904  0.942  0.921  0.957   0.9  0.911
	precision (micro=0.747, macro=0.328):
		   IV     ДС     ИС     II      I     ХС    III
		-----  -----  -----  -----  -----  -----  -----
		0.916  0.074  0.085  0.313  0.103  0.066  0.735
	!precision (micro=0.795, macro=0.918):
		   IV     ДС     ИС     II      I     ХС    III
		-----  -----  -----  -----  -----  -----  -----
		0.787  0.998  0.998  0.933  0.975  0.995  0.739
	f1 (micro=0.633, macro=0.318):
		   IV     ДС     ИС     II      I    ХС    III
		-----  -----  -----  -----  -----  ----  -----
		0.815  0.136  0.152  0.331  0.127  0.12  0.545
	!f1 (micro=0.854, macro=0.918):
		   IV     ДС     ИС     II      I     ХС    III
		-----  -----  -----  -----  -----  -----  -----
		0.855  0.949  0.969  0.927  0.966  0.945  0.816
	accuracy (micro=0.809, macro=0.874):
		   IV     ДС     ИС     II      I     ХС    III
		-----  -----  -----  -----  -----  -----  -----
		0.838  0.904  0.941  0.868  0.934  0.897  0.738
	fpr (micro=0.074, macro=0.075):
		   IV     ДС     ИС     II      I    ХС    III
		-----  -----  -----  -----  -----  ----  -----
		0.064  0.096  0.058  0.079  0.043   0.1  0.089
	roc_auc (micro=0.889, macro=0.871):
		   IV     ДС     ИС     II      I     ХС    III
		-----  -----  -----  -----  -----  -----  -----
		0.941  0.941  0.937  0.792  0.735  0.897  0.853
	pr_auc (micro=0.748, macro=0.356):
		   IV     ДС     ИС     II      I     ХС    III
		-----  -----  -----  -----  -----  -----  -----
		0.923  0.117  0.279  0.267  0.089  0.085  0.736
	
	 - score_schema: {'type': 'object', 'title': 'Scikit learn-based classifier score with probability', 'properties': {'probability': {'type': 'object', 'properties': {'IV': {'type': 'number'}, 'ДС': {'type': 'number'}, 'ИС': {'type': 'number'}, 'II': {'type': 'number'}, 'I': {'type': 'number'}, 'ХС': {'type': 'number'}, 'III': {'type': 'number'}}, 'description': 'A mapping of probabilities onto each of the potential output labels'}, 'prediction': {'type': 'string', 'description': 'The most likely label predicted by the estimator'}}}

