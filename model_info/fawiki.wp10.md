Model Information:
	 - type: GradientBoosting
	 - version: 0.8.0
	 - params: {'tol': 0.0001, 'ccp_alpha': 0.0, 'min_impurity_decrease': 0.0, 'population_rates': None, 'min_weight_fraction_leaf': 0.0, 'max_leaf_nodes': None, 'init': None, 'min_samples_split': 2, 'criterion': 'friedman_mse', 'n_estimators': 100, 'validation_fraction': 0.1, 'warm_start': False, 'learning_rate': 0.5, 'scale': True, 'presort': 'deprecated', 'min_impurity_split': None, 'max_depth': 7, 'min_samples_leaf': 1, 'center': True, 'max_features': 'log2', 'multilabel': False, 'verbose': 0, 'label_weights': None, 'labels': ['Stub', 'Start', 'C', 'B', 'GA', 'FA'], 'n_iter_no_change': None, 'loss': 'deviance', 'random_state': None, 'subsample': 1.0}
	Environment:
	 - revscoring_version: '2.8.2'
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
	counts (n=1235):
		label      n         ~Stub    ~Start    ~C    ~B    ~GA    ~FA
		-------  ---  ---  -------  --------  ----  ----  -----  -----
		'Stub'   226  -->      161        21    25    17      1      1
		'Start'   94  -->       22        26    33    12      0      1
		'C'      152  -->       21        17    57    41     14      2
		'B'      200  -->       11        15    29    62     58     25
		'GA'     300  -->        1         0    10    42    168     79
		'FA'     263  -->        2         0     1    16     83    161
	rates:
		              'Stub'    'Start'    'C'    'B'    'GA'    'FA'
		----------  --------  ---------  -----  -----  ------  ------
		sample         0.183      0.076  0.123  0.162   0.243   0.213
		population     0.182      0.076  0.123  0.162   0.242   0.212
	match_rate (micro=0.187, macro=0.166):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.176    0.064  0.125  0.154  0.262  0.218
	filter_rate (micro=0.813, macro=0.834):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.824    0.936  0.875  0.846  0.738  0.782
	recall (micro=0.514, macro=0.474):
		  Stub    Start      C     B    GA     FA
		------  -------  -----  ----  ----  -----
		 0.712    0.277  0.375  0.31  0.56  0.612
	!recall (micro=0.891, macro=0.901):
		  Stub    Start     C      B     GA     FA
		------  -------  ----  -----  -----  -----
		 0.944    0.954  0.91  0.876  0.833  0.889
	precision (micro=0.511, macro=0.479):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.737    0.329  0.367  0.326  0.518  0.598
	!precision (micro=0.894, macro=0.901):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.937    0.941  0.912  0.868  0.856  0.895
	f1 (micro=0.512, macro=0.476):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.724      0.3  0.371  0.318  0.538  0.605
	!f1 (micro=0.892, macro=0.901):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		  0.94    0.947  0.911  0.872  0.844  0.892
	accuracy (micro=0.828, macro=0.838):
		  Stub    Start      C      B     GA    FA
		------  -------  -----  -----  -----  ----
		 0.902    0.902  0.844  0.785  0.767  0.83
	fpr (micro=0.109, macro=0.099):
		  Stub    Start     C      B     GA     FA
		------  -------  ----  -----  -----  -----
		 0.056    0.046  0.09  0.124  0.167  0.111
	roc_auc (micro=0.805, macro=0.8):
		  Stub    Start      C      B     GA     FA
		------  -------  -----  -----  -----  -----
		 0.929    0.771  0.793  0.694  0.772  0.842
	pr_auc (micro=0.485, macro=0.447):
		  Stub    Start      C      B    GA     FA
		------  -------  -----  -----  ----  -----
		 0.753    0.228  0.337  0.315  0.48  0.569
	
	 - score_schema: {'properties': {'probability': {'properties': {'Start': {'type': 'number'}, 'FA': {'type': 'number'}, 'B': {'type': 'number'}, 'GA': {'type': 'number'}, 'Stub': {'type': 'number'}, 'C': {'type': 'number'}}, 'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object'}, 'prediction': {'description': 'The most likely label predicted by the estimator', 'type': 'string'}}, 'type': 'object', 'title': 'Scikit learn-based classifier score with probability'}

