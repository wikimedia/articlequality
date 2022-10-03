Model Information:
	 - type: GradientBoosting
	 - version: 0.9.0
	 - params: {'scale': True, 'center': True, 'labels': ['Stub', 'Start', 'C', 'B', 'GA', 'FA'], 'multilabel': False, 'population_rates': None, 'ccp_alpha': 0.0, 'criterion': 'friedman_mse', 'init': None, 'learning_rate': 0.5, 'loss': 'deviance', 'max_depth': 7, 'max_features': 'log2', 'max_leaf_nodes': None, 'min_impurity_decrease': 0.0, 'min_impurity_split': None, 'min_samples_leaf': 1, 'min_samples_split': 2, 'min_weight_fraction_leaf': 0.0, 'n_estimators': 100, 'n_iter_no_change': None, 'presort': 'deprecated', 'random_state': None, 'subsample': 1.0, 'tol': 0.0001, 'validation_fraction': 0.1, 'verbose': 0, 'warm_start': False, 'label_weights': None}
	Environment:
	 - revscoring_version: '2.11.6'
	 - platform: 'Linux-4.19.0-20-cloud-amd64-x86_64-with-glibc2.29'
	 - machine: 'x86_64'
	 - version: '#1 SMP Debian 4.19.235-1 (2022-03-17)'
	 - system: 'Linux'
	 - processor: 'x86_64'
	 - python_build: ('default', 'Jul 28 2020 12:59:40')
	 - python_compiler: 'GCC 9.3.0'
	 - python_branch: ''
	 - python_implementation: 'CPython'
	 - python_revision: ''
	 - python_version: '3.8.5'
	 - release: '4.19.0-20-cloud-amd64'
	
	Statistics:
	counts (n=1229):
		label      n         ~Stub    ~Start    ~C    ~B    ~GA    ~FA
		-------  ---  ---  -------  --------  ----  ----  -----  -----
		'Stub'   224  -->      142        18    35    26      2      1
		'Start'   93  -->       24        21    37     8      3      0
		'C'      150  -->       16        21    63    36     12      2
		'B'      199  -->       12        14    32    59     54     28
		'GA'     300  -->        1         1    11    41    168     78
		'FA'     263  -->        0         3     2    23     80    155
	rates:
		              'Stub'    'Start'    'C'    'B'    'GA'    'FA'
		----------  --------  ---------  -----  -----  ------  ------
		sample         0.182      0.076  0.122  0.162   0.244   0.214
		population     0.182      0.076  0.123  0.162   0.242   0.212
	match_rate (micro=0.186, macro=0.166):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.158    0.064  0.147  0.157  0.259  0.214
	filter_rate (micro=0.814, macro=0.834):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.842    0.936  0.853  0.843  0.741  0.786
	recall (micro=0.494, macro=0.454):
		  Stub    Start     C      B    GA     FA
		------  -------  ----  -----  ----  -----
		 0.634    0.226  0.42  0.296  0.56  0.589
	!recall (micro=0.889, macro=0.897):
		  Stub    Start      C     B     GA     FA
		------  -------  -----  ----  -----  -----
		 0.947     0.95  0.892  0.87  0.837  0.887
	precision (micro=0.498, macro=0.461):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.728     0.27  0.352  0.305  0.524  0.585
	!precision (micro=0.89, macro=0.898):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.921    0.937  0.917  0.865  0.856  0.889
	f1 (micro=0.495, macro=0.456):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.678    0.246  0.383  0.301  0.542  0.587
	!f1 (micro=0.889, macro=0.897):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.934    0.943  0.904  0.868  0.847  0.888
	accuracy (micro=0.822, macro=0.832):
		  Stub    Start      C      B    GA     FA
		------  -------  -----  -----  ----  -----
		  0.89    0.895  0.834  0.777  0.77  0.824
	fpr (micro=0.111, macro=0.103):
		  Stub    Start      C     B     GA     FA
		------  -------  -----  ----  -----  -----
		 0.053     0.05  0.108  0.13  0.163  0.113
	roc_auc (micro=0.805, macro=0.8):
		  Stub    Start      C      B    GA     FA
		------  -------  -----  -----  ----  -----
		 0.927    0.782  0.807  0.659  0.79  0.838
	pr_auc (micro=0.497, macro=0.455):
		  Stub    Start      C     B     GA     FA
		------  -------  -----  ----  -----  -----
		 0.773    0.245  0.326  0.28  0.516  0.591
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'prediction': {'description': 'The most likely label predicted by the estimator', 'type': 'string'}, 'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object', 'properties': {'Stub': {'type': 'number'}, 'Start': {'type': 'number'}, 'C': {'type': 'number'}, 'B': {'type': 'number'}, 'GA': {'type': 'number'}, 'FA': {'type': 'number'}}}}}

