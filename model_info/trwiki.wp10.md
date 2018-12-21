Model Information:
	 - type: GradientBoosting
	 - version: 0.8.0
	 - params: {'min_impurity_decrease': 0.0, 'center': True, 'min_samples_leaf': 1, 'presort': 'auto', 'random_state': None, 'max_features': 'log2', 'min_samples_split': 2, 'learning_rate': 0.01, 'verbose': 0, 'population_rates': None, 'n_estimators': 300, 'label_weights': None, 'multilabel': False, 'subsample': 1.0, 'min_impurity_split': None, 'labels': ['taslak', 'baslagıç', 'c', 'b', 'km', 'sm'], 'loss': 'deviance', 'warm_start': False, 'max_leaf_nodes': None, 'init': None, 'max_depth': 5, 'criterion': 'friedman_mse', 'min_weight_fraction_leaf': 0.0, 'scale': True}
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
	counts (n=1614):
		label         n         ~taslak    ~baslagıç    ~c    ~b    ~km    ~sm
		----------  ---  ---  ---------  -----------  ----  ----  -----  -----
		'taslak'    267  -->        193           71     3     0      0      0
		'baslagıç'  271  -->         66          156    42     3      4      0
		'c'         269  -->         13           49   132    38     30      7
		'b'         270  -->          5           18    39   126     42     40
		'km'        267  -->          1            5    22    15    184     40
		'sm'        270  -->          2            3     6    26     41    192
	rates:
		              'taslak'    'baslagıç'    'c'    'b'    'km'    'sm'
		----------  ----------  ------------  -----  -----  ------  ------
		sample           0.165         0.168  0.167  0.167   0.165   0.167
		population       0.58          0.248  0.086  0.053   0.017   0.016
	match_rate (micro=0.332, macro=0.174):
		    c      b     km     sm    baslagıç    taslak
		-----  -----  -----  -----  ----------  --------
		0.118  0.083  0.097  0.075       0.224     0.447
	filter_rate (micro=0.668, macro=0.826):
		    c      b     km     sm    baslagıç    taslak
		-----  -----  -----  -----  ----------  --------
		0.882  0.917  0.903  0.925       0.776     0.553
	recall (micro=0.652, macro=0.609):
		    c      b     km     sm    baslagıç    taslak
		-----  -----  -----  -----  ----------  --------
		0.491  0.467  0.689  0.711       0.576     0.723
	!recall (micro=0.923, macro=0.922):
		    c      b     km     sm    baslagıç    taslak
		-----  -----  -----  -----  ----------  --------
		0.917  0.939  0.913  0.935       0.891     0.935
	precision (micro=0.754, macro=0.417):
		    c      b    km     sm    baslagıç    taslak
		-----  -----  ----  -----  ----------  --------
		0.357  0.301  0.12  0.149       0.636     0.939
	!precision (micro=0.792, macro=0.914):
		   c      b     km     sm    baslagıç    taslak
		----  -----  -----  -----  ----------  --------
		0.95  0.969  0.994  0.995       0.864     0.709
	f1 (micro=0.686, macro=0.442):
		    c      b     km     sm    baslagıç    taslak
		-----  -----  -----  -----  ----------  --------
		0.413  0.366  0.205  0.247       0.604     0.817
	!f1 (micro=0.848, macro=0.915):
		    c      b     km     sm    baslagıç    taslak
		-----  -----  -----  -----  ----------  --------
		0.933  0.954  0.952  0.964       0.878     0.807
	accuracy (micro=0.827, macro=0.877):
		   c      b     km     sm    baslagıç    taslak
		----  -----  -----  -----  ----------  --------
		0.88  0.914  0.909  0.932       0.813     0.812
	fpr (micro=0.077, macro=0.078):
		    c      b     km     sm    baslagıç    taslak
		-----  -----  -----  -----  ----------  --------
		0.083  0.061  0.087  0.065       0.109     0.065
	roc_auc (micro=0.916, macro=0.899):
		    c      b     km     sm    baslagıç    taslak
		-----  -----  -----  -----  ----------  --------
		0.855  0.855  0.921  0.936       0.879     0.946
	pr_auc (micro=0.783, macro=0.506):
		    c      b    km     sm    baslagıç    taslak
		-----  -----  ----  -----  ----------  --------
		0.502  0.382  0.23  0.327       0.644     0.949
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'prediction': {'description': 'The most likely label predicted by the estimator', 'type': 'string'}, 'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object', 'properties': {'c': {'type': 'number'}, 'b': {'type': 'number'}, 'km': {'type': 'number'}, 'sm': {'type': 'number'}, 'baslagıç': {'type': 'number'}, 'taslak': {'type': 'number'}}}}}

