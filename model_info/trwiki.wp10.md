Model Information:
	 - type: GradientBoosting
	 - version: 0.8.0
	 - params: {'warm_start': False, 'center': True, 'min_weight_fraction_leaf': 0.0, 'loss': 'deviance', 'min_impurity_decrease': 0.0, 'min_samples_split': 2, 'max_features': 'log2', 'min_samples_leaf': 1, 'max_depth': 5, 'n_iter_no_change': None, 'multilabel': False, 'scale': True, 'max_leaf_nodes': None, 'label_weights': None, 'presort': 'deprecated', 'n_estimators': 300, 'criterion': 'friedman_mse', 'verbose': 0, 'population_rates': None, 'random_state': None, 'validation_fraction': 0.1, 'subsample': 1.0, 'labels': ['taslak', 'baslagıç', 'c', 'b', 'km', 'sm'], 'ccp_alpha': 0.0, 'learning_rate': 0.01, 'min_impurity_split': None, 'init': None, 'tol': 0.0001}
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
	counts (n=1614):
		label         n         ~taslak    ~baslagıç    ~c    ~b    ~km    ~sm
		----------  ---  ---  ---------  -----------  ----  ----  -----  -----
		'taslak'    267  -->        192           72     3     0      0      0
		'baslagıç'  271  -->         64          158    43     2      4      0
		'c'         269  -->         13           50   131    39     29      7
		'b'         270  -->          5           17    38   127     38     45
		'km'        267  -->          1            6    20    14    184     42
		'sm'        270  -->          2            3     6    26     41    192
	rates:
		              'taslak'    'baslagıç'    'c'    'b'    'km'    'sm'
		----------  ----------  ------------  -----  -----  ------  ------
		sample           0.165         0.168  0.167  0.167   0.165   0.167
		population       0.58          0.248  0.086  0.053   0.017   0.016
	match_rate (micro=0.331, macro=0.174):
		  taslak    baslagıç      c      b     km    sm
		--------  ----------  -----  -----  -----  ----
		   0.444       0.227  0.117  0.082  0.093  0.08
	filter_rate (micro=0.669, macro=0.826):
		  taslak    baslagıç      c      b     km    sm
		--------  ----------  -----  -----  -----  ----
		   0.556       0.773  0.883  0.918  0.907  0.92
	recall (micro=0.652, macro=0.61):
		  taslak    baslagıç      c     b     km     sm
		--------  ----------  -----  ----  -----  -----
		   0.719       0.583  0.487  0.47  0.689  0.711
	!recall (micro=0.923, macro=0.922):
		  taslak    baslagıç      c     b     km    sm
		--------  ----------  -----  ----  -----  ----
		   0.937        0.89  0.918  0.94  0.917  0.93
	precision (micro=0.755, macro=0.417):
		  taslak    baslagıç      c      b     km    sm
		--------  ----------  -----  -----  -----  ----
		    0.94       0.635  0.359  0.305  0.125  0.14
	!precision (micro=0.791, macro=0.914):
		  taslak    baslagıç     c      b     km     sm
		--------  ----------  ----  -----  -----  -----
		   0.707       0.866  0.95  0.969  0.994  0.995
	f1 (micro=0.686, macro=0.442):
		  taslak    baslagıç      c     b     km     sm
		--------  ----------  -----  ----  -----  -----
		   0.815       0.608  0.413  0.37  0.212  0.234
	!f1 (micro=0.848, macro=0.915):
		  taslak    baslagıç      c      b     km     sm
		--------  ----------  -----  -----  -----  -----
		   0.806       0.878  0.934  0.954  0.954  0.961
	accuracy (micro=0.826, macro=0.877):
		  taslak    baslagıç      c      b     km     sm
		--------  ----------  -----  -----  -----  -----
		    0.81       0.814  0.881  0.915  0.913  0.927
	fpr (micro=0.077, macro=0.078):
		  taslak    baslagıç      c     b     km    sm
		--------  ----------  -----  ----  -----  ----
		   0.063        0.11  0.082  0.06  0.083  0.07
	roc_auc (micro=0.917, macro=0.898):
		  taslak    baslagıç      c      b    km     sm
		--------  ----------  -----  -----  ----  -----
		   0.947        0.88  0.851  0.856  0.92  0.935
	pr_auc (micro=0.781, macro=0.502):
		  taslak    baslagıç      c      b     km     sm
		--------  ----------  -----  -----  -----  -----
		    0.95       0.641  0.493  0.372  0.236  0.322
	
	 - score_schema: {'type': 'object', 'title': 'Scikit learn-based classifier score with probability', 'properties': {'probability': {'type': 'object', 'description': 'A mapping of probabilities onto each of the potential output labels', 'properties': {'taslak': {'type': 'number'}, 'baslagıç': {'type': 'number'}, 'c': {'type': 'number'}, 'b': {'type': 'number'}, 'km': {'type': 'number'}, 'sm': {'type': 'number'}}}, 'prediction': {'type': 'string', 'description': 'The most likely label predicted by the estimator'}}}

