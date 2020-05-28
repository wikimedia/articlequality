Model Information:
	 - type: GradientBoosting
	 - version: 0.8.0
	 - params: {'presort': 'deprecated', 'max_leaf_nodes': None, 'multilabel': False, 'validation_fraction': 0.1, 'ccp_alpha': 0.0, 'min_impurity_decrease': 0.0, 'center': True, 'min_samples_leaf': 1, 'random_state': None, 'warm_start': False, 'init': None, 'loss': 'deviance', 'verbose': 0, 'scale': True, 'n_iter_no_change': None, 'tol': 0.0001, 'max_features': 'log2', 'max_depth': 7, 'subsample': 1.0, 'min_weight_fraction_leaf': 0.0, 'n_estimators': 500, 'population_rates': None, 'learning_rate': 0.01, 'criterion': 'friedman_mse', 'label_weights': None, 'min_impurity_split': None, 'labels': ['I', 'II', 'III', 'IV', 'ВС', 'ДС'], 'min_samples_split': 2}
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
		label      n         ~I    ~II    ~III    ~IV    ~ВС    ~ДС
		-------  ---  ---  ----  -----  ------  -----  -----  -----
		'I'      150  -->    57     34      13      6     18     22
		'II'     149  -->    30     63      23     21      5      7
		'III'    150  -->     9     41      51     44      2      3
		'IV'     150  -->     6     19      42     83      0      0
		'ВС'     150  -->    13     12       2      0     86     37
		'ДС'     150  -->    39     11       3      0     39     58
	rates:
		              'I'    'II'    'III'    'IV'    'ВС'    'ДС'
		----------  -----  ------  -------  ------  ------  ------
		sample      0.167   0.166    0.167   0.167   0.167   0.167
		population  0.018   0.098    0.61    0.266   0.004   0.01
	match_rate (micro=0.231, macro=0.161):
		    I     II    III     IV     ВС     ДС
		-----  -----  -----  -----  -----  -----
		0.134  0.182  0.251  0.217  0.087  0.095
	filter_rate (micro=0.769, macro=0.839):
		    I     II    III     IV     ВС     ДС
		-----  -----  -----  -----  -----  -----
		0.866  0.818  0.749  0.783  0.913  0.905
	recall (micro=0.407, macro=0.443):
		   I     II    III     IV     ВС     ДС
		----  -----  -----  -----  -----  -----
		0.38  0.423   0.34  0.553  0.573  0.387
	!recall (micro=0.889, macro=0.889):
		   I     II    III     IV     ВС     ДС
		----  -----  -----  -----  -----  -----
		0.87  0.844  0.889  0.905  0.915  0.908
	precision (micro=0.705, macro=0.309):
		    I     II    III     IV     ВС    ДС
		-----  -----  -----  -----  -----  ----
		0.051  0.227  0.827  0.679  0.027  0.04
	!precision (micro=0.627, macro=0.87):
		    I     II    III     IV     ВС     ДС
		-----  -----  -----  -----  -----  -----
		0.987  0.931  0.463  0.848  0.998  0.993
	f1 (micro=0.485, macro=0.267):
		   I     II    III    IV     ВС     ДС
		----  -----  -----  ----  -----  -----
		0.09  0.296  0.482  0.61  0.052  0.073
	!f1 (micro=0.717, macro=0.866):
		    I     II    III     IV     ВС     ДС
		-----  -----  -----  -----  -----  -----
		0.925  0.885  0.609  0.876  0.954  0.949
	accuracy (micro=0.657, macro=0.808):
		    I     II    III     IV     ВС     ДС
		-----  -----  -----  -----  -----  -----
		0.862  0.803  0.554  0.812  0.913  0.903
	fpr (micro=0.111, macro=0.111):
		   I     II    III     IV     ВС     ДС
		----  -----  -----  -----  -----  -----
		0.13  0.156  0.111  0.095  0.085  0.092
	roc_auc (micro=0.805, macro=0.812):
		    I     II    III     IV     ВС     ДС
		-----  -----  -----  -----  -----  -----
		0.748  0.731  0.786  0.875  0.891  0.841
	pr_auc (micro=0.691, macro=0.317):
		   I     II    III     IV     ВС     ДС
		----  -----  -----  -----  -----  -----
		0.06  0.217  0.791  0.712  0.071  0.048
	
	 - score_schema: {'type': 'object', 'properties': {'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object', 'properties': {'IV': {'type': 'number'}, 'I': {'type': 'number'}, 'III': {'type': 'number'}, 'II': {'type': 'number'}, 'ВС': {'type': 'number'}, 'ДС': {'type': 'number'}}}, 'prediction': {'description': 'The most likely label predicted by the estimator', 'type': 'string'}}, 'title': 'Scikit learn-based classifier score with probability'}

