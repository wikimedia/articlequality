Model Information:
	 - type: GradientBoosting
	 - version: 0.8.0
	 - params: {'min_impurity_split': None, 'n_iter_no_change': None, 'max_features': 'log2', 'scale': True, 'n_estimators': 500, 'verbose': 0, 'multilabel': False, 'label_weights': None, 'min_samples_leaf': 1, 'min_samples_split': 2, 'min_weight_fraction_leaf': 0.0, 'criterion': 'friedman_mse', 'validation_fraction': 0.1, 'subsample': 1.0, 'loss': 'deviance', 'max_leaf_nodes': None, 'center': True, 'population_rates': None, 'ccp_alpha': 0.0, 'random_state': None, 'learning_rate': 0.01, 'warm_start': False, 'presort': 'deprecated', 'labels': ['IV', 'III', 'II', 'I', 'ДС', 'ВС'], 'min_impurity_decrease': 0.0, 'init': None, 'tol': 0.0001, 'max_depth': 7}
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
		label      n         ~IV    ~III    ~II    ~I    ~ДС    ~ВС
		-------  ---  ---  -----  ------  -----  ----  -----  -----
		'IV'     150  -->     81      45     19     5      0      0
		'III'    150  -->     43      50     42    10      3      2
		'II'     149  -->     21      20     63    34      6      5
		'I'      150  -->      6      12     36    56     24     16
		'ДС'     150  -->      0       3     11    40     56     40
		'ВС'     150  -->      0       2     11    18     39     80
	rates:
		              'IV'    'III'    'II'    'I'    'ДС'    'ВС'
		----------  ------  -------  ------  -----  ------  ------
		sample       0.167    0.167   0.166  0.167   0.167   0.167
		population   0.266    0.61    0.098  0.018   0.01    0.004
	match_rate (micro=0.227, macro=0.162):
		   IV    III     II      I     ДС     ВС
		-----  -----  -----  -----  -----  -----
		0.212  0.246  0.185  0.147  0.099  0.086
	filter_rate (micro=0.773, macro=0.838):
		   IV    III     II      I     ДС     ВС
		-----  -----  -----  -----  -----  -----
		0.788  0.754  0.815  0.853  0.901  0.914
	recall (micro=0.399, macro=0.429):
		  IV    III     II      I     ДС     ВС
		----  -----  -----  -----  -----  -----
		0.54  0.333  0.423  0.373  0.373  0.533
	!recall (micro=0.89, macro=0.886):
		   IV    III     II      I     ДС     ВС
		-----  -----  -----  -----  -----  -----
		0.907  0.891  0.841  0.857  0.904  0.916
	precision (micro=0.703, macro=0.306):
		   IV    III     II      I     ДС     ВС
		-----  -----  -----  -----  -----  -----
		0.676  0.826  0.224  0.046  0.037  0.026
	!precision (micro=0.625, macro=0.869):
		   IV    III     II      I     ДС     ВС
		-----  -----  -----  -----  -----  -----
		0.845  0.461  0.931  0.987  0.993  0.998
	f1 (micro=0.478, macro=0.261):
		   IV    III     II      I     ДС     ВС
		-----  -----  -----  -----  -----  -----
		0.601  0.475  0.293  0.081  0.068  0.049
	!f1 (micro=0.715, macro=0.864):
		   IV    III     II      I     ДС     ВС
		-----  -----  -----  -----  -----  -----
		0.875  0.607  0.884  0.917  0.946  0.955
	accuracy (micro=0.654, macro=0.804):
		   IV    III    II      I     ДС     ВС
		-----  -----  ----  -----  -----  -----
		0.809  0.551   0.8  0.848  0.899  0.914
	fpr (micro=0.11, macro=0.114):
		   IV    III     II      I     ДС     ВС
		-----  -----  -----  -----  -----  -----
		0.093  0.109  0.159  0.143  0.096  0.084
	roc_auc (micro=0.807, macro=0.813):
		   IV    III     II      I     ДС     ВС
		-----  -----  -----  -----  -----  -----
		0.874  0.791  0.733  0.747  0.842  0.893
	pr_auc (micro=0.693, macro=0.314):
		   IV    III     II      I    ДС     ВС
		-----  -----  -----  -----  ----  -----
		0.713  0.795  0.217  0.058  0.05  0.052
	
	 - score_schema: {'properties': {'probability': {'properties': {'III': {'type': 'number'}, 'ВС': {'type': 'number'}, 'IV': {'type': 'number'}, 'II': {'type': 'number'}, 'ДС': {'type': 'number'}, 'I': {'type': 'number'}}, 'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object'}, 'prediction': {'description': 'The most likely label predicted by the estimator', 'type': 'string'}}, 'title': 'Scikit learn-based classifier score with probability', 'type': 'object'}

