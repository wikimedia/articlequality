Model Information:
	 - type: GradientBoosting
	 - version: 0.8.0
	 - params: {'min_impurity_decrease': 0.0, 'scale': True, 'verbose': 0, 'warm_start': False, 'max_features': 'log2', 'subsample': 1.0, 'multilabel': False, 'n_estimators': 100, 'min_samples_leaf': 1, 'init': None, 'presort': 'auto', 'population_rates': None, 'criterion': 'friedman_mse', 'max_leaf_nodes': None, 'center': True, 'min_weight_fraction_leaf': 0.0, 'labels': ['Stub', 'Start', 'C', 'B', 'GA', 'FA'], 'learning_rate': 0.5, 'loss': 'deviance', 'max_depth': 7, 'min_samples_split': 2, 'random_state': None, 'min_impurity_split': None, 'label_weights': None}
	Environment:
	 - revscoring_version: '2.3.3'
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
	counts (n=1234):
		label      n         ~Stub    ~Start    ~C    ~B    ~GA    ~FA
		-------  ---  ---  -------  --------  ----  ----  -----  -----
		'Stub'   225  -->      172        16    20    14      3      0
		'Start'   94  -->       22        20    38    13      0      1
		'C'      152  -->       23        21    58    35     13      2
		'B'      200  -->       15         9    23    63     68     22
		'GA'     300  -->        1         0    10    35    177     77
		'FA'     263  -->        2         0     1    18     88    154
	rates:
		              'Stub'    'Start'    'C'    'B'    'GA'    'FA'
		----------  --------  ---------  -----  -----  ------  ------
		sample         0.182      0.076  0.123  0.162   0.243   0.213
		population     0.182      0.076  0.123  0.162   0.242   0.212
	match_rate (micro=0.19, macro=0.166):
		   FA      C    Start     GA      B    Stub
		-----  -----  -------  -----  -----  ------
		0.207  0.121    0.053  0.283  0.144    0.19
	filter_rate (micro=0.81, macro=0.834):
		   FA      C    Start     GA      B    Stub
		-----  -----  -------  -----  -----  ------
		0.793  0.879    0.947  0.717  0.856    0.81
	recall (micro=0.522, macro=0.475):
		   FA      C    Start    GA      B    Stub
		-----  -----  -------  ----  -----  ------
		0.586  0.382    0.213  0.59  0.315   0.764
	!recall (micro=0.89, macro=0.902):
		   FA      C    Start     GA      B    Stub
		-----  -----  -------  -----  -----  ------
		0.895  0.915     0.96  0.816  0.889   0.938
	precision (micro=0.512, macro=0.48):
		   FA      C    Start     GA      B    Stub
		-----  -----  -------  -----  -----  ------
		0.601  0.386    0.302  0.506  0.353   0.731
	!precision (micro=0.897, macro=0.903):
		   FA      C    Start     GA      B    Stub
		-----  -----  -------  -----  -----  ------
		0.889  0.914    0.937  0.862  0.871   0.947
	f1 (micro=0.515, macro=0.475):
		   FA      C    Start     GA      B    Stub
		-----  -----  -------  -----  -----  ------
		0.593  0.384     0.25  0.545  0.333   0.747
	!f1 (micro=0.893, macro=0.902):
		   FA      C    Start     GA     B    Stub
		-----  -----  -------  -----  ----  ------
		0.892  0.914    0.948  0.838  0.88   0.942
	accuracy (micro=0.829, macro=0.841):
		   FA      C    Start     GA      B    Stub
		-----  -----  -------  -----  -----  ------
		0.829  0.849    0.903  0.761  0.796   0.906
	fpr (micro=0.11, macro=0.098):
		   FA      C    Start     GA      B    Stub
		-----  -----  -------  -----  -----  ------
		0.105  0.085     0.04  0.184  0.111   0.062
	roc_auc (micro=0.808, macro=0.805):
		   FA      C    Start     GA      B    Stub
		-----  -----  -------  -----  -----  ------
		0.817  0.807    0.781  0.776  0.706   0.943
	pr_auc (micro=0.49, macro=0.453):
		   FA      C    Start     GA      B    Stub
		-----  -----  -------  -----  -----  ------
		0.534  0.349    0.238  0.506  0.324   0.764
	
	 - score_schema: {'type': 'object', 'title': 'Scikit learn-based classifier score with probability', 'properties': {'probability': {'type': 'object', 'description': 'A mapping of probabilities onto each of the potential output labels', 'properties': {'FA': {'type': 'number'}, 'C': {'type': 'number'}, 'Start': {'type': 'number'}, 'GA': {'type': 'number'}, 'B': {'type': 'number'}, 'Stub': {'type': 'number'}}}, 'prediction': {'type': 'string', 'description': 'The most likely label predicted by the estimator'}}}

