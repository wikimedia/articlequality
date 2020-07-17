Model Information:
	 - type: GradientBoosting
	 - version: 0.8.0
	 - params: {'min_samples_split': 2, 'validation_fraction': 0.1, 'max_leaf_nodes': None, 'warm_start': False, 'population_rates': None, 'subsample': 1.0, 'verbose': 0, 'n_estimators': 500, 'multilabel': False, 'init': None, 'labels': ['IV', 'III', 'II', 'I', 'ВС', 'ДС'], 'min_weight_fraction_leaf': 0.0, 'max_depth': 7, 'max_features': 'log2', 'criterion': 'friedman_mse', 'min_impurity_split': None, 'learning_rate': 0.01, 'min_samples_leaf': 1, 'ccp_alpha': 0.0, 'scale': True, 'center': True, 'loss': 'deviance', 'tol': 0.0001, 'n_iter_no_change': None, 'presort': 'deprecated', 'label_weights': None, 'min_impurity_decrease': 0.0, 'random_state': None}
	Environment:
	 - revscoring_version: '2.8.2'
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
	counts (n=899):
		label      n         ~IV    ~III    ~II    ~I    ~ВС    ~ДС
		-------  ---  ---  -----  ------  -----  ----  -----  -----
		'IV'     150  -->     82      46     16     6      0      0
		'III'    150  -->     43      52     39    12      1      3
		'II'     149  -->     21      21     64    31      5      7
		'I'      150  -->      5      14     32    60     14     25
		'ВС'     150  -->      0       4     11    14     84     37
		'ДС'     150  -->      0       2     12    37     38     61
	rates:
		              'IV'    'III'    'II'    'I'    'ВС'    'ДС'
		----------  ------  -------  ------  -----  ------  ------
		sample       0.167    0.167   0.166  0.167   0.167   0.167
		population   0.266    0.61    0.098  0.018   0.004   0.01
	match_rate (micro=0.233, macro=0.16):
		   IV    III     II      I     ВС     ДС
		-----  -----  -----  -----  -----  -----
		0.213  0.257  0.174  0.138  0.079  0.099
	filter_rate (micro=0.767, macro=0.84):
		   IV    III     II      I     ВС     ДС
		-----  -----  -----  -----  -----  -----
		0.787  0.743  0.826  0.862  0.921  0.901
	recall (micro=0.41, macro=0.448):
		   IV    III    II    I    ВС     ДС
		-----  -----  ----  ---  ----  -----
		0.547  0.347  0.43  0.4  0.56  0.407
	!recall (micro=0.887, macro=0.89):
		   IV    III     II      I     ВС     ДС
		-----  -----  -----  -----  -----  -----
		0.908  0.884  0.853  0.866  0.923  0.904
	precision (micro=0.705, macro=0.311):
		   IV    III     II      I     ВС    ДС
		-----  -----  -----  -----  -----  ----
		0.682  0.823  0.241  0.052  0.029  0.04
	!precision (micro=0.628, macro=0.87):
		   IV    III     II      I     ВС     ДС
		-----  -----  -----  -----  -----  -----
		0.847  0.464  0.932  0.987  0.998  0.994
	f1 (micro=0.489, macro=0.271):
		   IV    III     II      I     ВС     ДС
		-----  -----  -----  -----  -----  -----
		0.607  0.488  0.309  0.092  0.055  0.073
	!f1 (micro=0.717, macro=0.867):
		   IV    III     II      I     ВС     ДС
		-----  -----  -----  -----  -----  -----
		0.876  0.609  0.891  0.923  0.959  0.947
	accuracy (micro=0.659, macro=0.81):
		   IV    III     II      I     ВС     ДС
		-----  -----  -----  -----  -----  -----
		0.812  0.556  0.812  0.858  0.921  0.899
	fpr (micro=0.113, macro=0.11):
		   IV    III     II      I     ВС     ДС
		-----  -----  -----  -----  -----  -----
		0.092  0.116  0.147  0.134  0.077  0.096
	roc_auc (micro=0.805, macro=0.813):
		   IV    III     II      I     ВС     ДС
		-----  -----  -----  -----  -----  -----
		0.875  0.786  0.733  0.748  0.894  0.839
	pr_auc (micro=0.691, macro=0.313):
		   IV    III     II     I     ВС     ДС
		-----  -----  -----  ----  -----  -----
		0.713  0.791  0.219  0.06  0.049  0.049
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object', 'properties': {'I': {'type': 'number'}, 'IV': {'type': 'number'}, 'II': {'type': 'number'}, 'III': {'type': 'number'}, 'ДС': {'type': 'number'}, 'ВС': {'type': 'number'}}}, 'prediction': {'description': 'The most likely label predicted by the estimator', 'type': 'string'}}}

