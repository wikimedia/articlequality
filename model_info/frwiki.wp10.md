Model Information:
	 - type: GradientBoosting
	 - version: 0.8.0
	 - params: {'warm_start': False, 'min_impurity_split': None, 'random_state': None, 'scale': True, 'min_samples_leaf': 1, 'verbose': 0, 'min_samples_split': 2, 'criterion': 'friedman_mse', 'labels': ['e', 'bd', 'b', 'a', 'ba', 'adq'], 'n_estimators': 100, 'subsample': 1.0, 'min_impurity_decrease': 0.0, 'label_weights': None, 'presort': 'auto', 'init': None, 'min_weight_fraction_leaf': 0.0, 'multilabel': False, 'center': True, 'max_features': 'log2', 'loss': 'deviance', 'population_rates': None, 'max_depth': 7, 'max_leaf_nodes': None, 'learning_rate': 0.01}
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
	counts (n=8926):
		label       n         ~e    ~bd    ~b    ~a    ~ba    ~adq
		-------  ----  ---  ----  -----  ----  ----  -----  ------
		'e'      1487  -->  1075    359    49     2      2       0
		'bd'     1479  -->   268    873   297    17     19       5
		'b'      1488  -->    48    263   815   111    168      83
		'a'      1491  -->    23     89   277   208    474     420
		'ba'     1491  -->     9     26   116   129    758     453
		'adq'    1490  -->     2      1    56    70    316    1045
	rates:
		              'e'    'bd'    'b'    'a'    'ba'    'adq'
		----------  -----  ------  -----  -----  ------  -------
		sample      0.167   0.166  0.167  0.167   0.167    0.167
		population  0.731   0.231  0.03   0.003   0.002    0.001
	match_rate (micro=0.45, macro=0.197):
		   b    adq     bd      a      e     ba
		----  -----  -----  -----  -----  -----
		0.12   0.13  0.213  0.045  0.541  0.133
	filter_rate (micro=0.55, macro=0.803):
		   b    adq     bd      a      e     ba
		----  -----  -----  -----  -----  -----
		0.88   0.87  0.787  0.955  0.459  0.867
	recall (micro=0.685, macro=0.535):
		    b    adq    bd     a      e     ba
		-----  -----  ----  ----  -----  -----
		0.548  0.701  0.59  0.14  0.723  0.508
	!recall (micro=0.939, macro=0.907):
		    b    adq     bd      a      e     ba
		-----  -----  -----  -----  -----  -----
		0.893  0.871  0.901  0.956  0.953  0.868
	precision (micro=0.867, macro=0.297):
		    b    adq     bd      a      e     ba
		-----  -----  -----  -----  -----  -----
		0.138  0.008  0.642  0.009  0.977  0.009
	!precision (micro=0.648, macro=0.903):
		    b    adq    bd      a      e     ba
		-----  -----  ----  -----  -----  -----
		0.984      1  0.88  0.997  0.558  0.999
	f1 (micro=0.757, macro=0.286):
		   b    adq     bd      a      e     ba
		----  -----  -----  -----  -----  -----
		0.22  0.015  0.615  0.017  0.831  0.018
	!f1 (micro=0.756, macro=0.894):
		    b    adq    bd      a      e     ba
		-----  -----  ----  -----  -----  -----
		0.937  0.931  0.89  0.976  0.704  0.929
	accuracy (micro=0.799, macro=0.865):
		    b    adq     bd      a      e     ba
		-----  -----  -----  -----  -----  -----
		0.883  0.871  0.829  0.953  0.785  0.867
	fpr (micro=0.061, macro=0.093):
		    b    adq     bd      a      e     ba
		-----  -----  -----  -----  -----  -----
		0.107  0.129  0.099  0.044  0.047  0.132
	roc_auc (micro=0.935, macro=0.86):
		    b    adq     bd      a      e     ba
		-----  -----  -----  -----  -----  -----
		0.841  0.896  0.889  0.748  0.954  0.831
	pr_auc (micro=0.88, macro=0.312):
		    b    adq    bd      a      e     ba
		-----  -----  ----  -----  -----  -----
		0.159  0.021  0.69  0.017  0.978  0.009
	
	 - score_schema: {'type': 'object', 'properties': {'prediction': {'description': 'The most likely label predicted by the estimator', 'type': 'string'}, 'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object', 'properties': {'b': {'type': 'number'}, 'adq': {'type': 'number'}, 'bd': {'type': 'number'}, 'a': {'type': 'number'}, 'e': {'type': 'number'}, 'ba': {'type': 'number'}}}}, 'title': 'Scikit learn-based classifier score with probability'}

