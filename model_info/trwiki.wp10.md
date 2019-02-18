Model Information:
	 - type: GradientBoosting
	 - version: 0.8.0
	 - params: {'warm_start': False, 'verbose': 0, 'max_features': 'log2', 'init': None, 'presort': 'auto', 'subsample': 1.0, 'label_weights': None, 'criterion': 'friedman_mse', 'center': True, 'min_samples_split': 2, 'labels': ['taslak', 'baslagıç', 'c', 'b', 'km', 'sm'], 'min_weight_fraction_leaf': 0.0, 'random_state': None, 'multilabel': False, 'n_estimators': 300, 'learning_rate': 0.01, 'min_samples_leaf': 1, 'min_impurity_split': None, 'min_impurity_decrease': 0.0, 'max_leaf_nodes': None, 'max_depth': 5, 'loss': 'deviance', 'population_rates': None, 'scale': True}
	Environment:
	 - revscoring_version: '2.3.4'
	 - platform: 'Linux-4.9.0-8-amd64-x86_64-with-debian-9.5'
	 - machine: 'x86_64'
	 - version: '#1 SMP Debian 4.9.110-3+deb9u6 (2018-10-08)'
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
	counts (n=1614):
		label         n         ~taslak    ~baslagıç    ~c    ~b    ~km    ~sm
		----------  ---  ---  ---------  -----------  ----  ----  -----  -----
		'taslak'    267  -->        197           67     3     0      0      0
		'baslagıç'  271  -->         69          153    42     3      4      0
		'c'         269  -->         13           52   133    34     29      8
		'b'         270  -->          5           14    40   124     39     48
		'km'        267  -->          2            3    24    15    182     41
		'sm'        270  -->          2            3     6    25     36    198
	rates:
		              'taslak'    'baslagıç'    'c'    'b'    'km'    'sm'
		----------  ----------  ------------  -----  -----  ------  ------
		sample           0.165         0.168  0.167  0.167   0.165   0.167
		population       0.58          0.248  0.086  0.053   0.017   0.016
	match_rate (micro=0.336, macro=0.174):
		   sm      b    baslagıç      c    km    taslak
		-----  -----  ----------  -----  ----  --------
		0.083  0.079       0.218  0.121  0.09     0.457
	filter_rate (micro=0.664, macro=0.826):
		   sm      b    baslagıç      c    km    taslak
		-----  -----  ----------  -----  ----  --------
		0.917  0.921       0.782  0.879  0.91     0.543
	recall (micro=0.658, macro=0.612):
		   sm      b    baslagıç      c     km    taslak
		-----  -----  ----------  -----  -----  --------
		0.733  0.459       0.565  0.494  0.682     0.738
	!recall (micro=0.922, macro=0.922):
		   sm      b    baslagıç      c    km    taslak
		-----  -----  ----------  -----  ----  --------
		0.928  0.943       0.897  0.914  0.92     0.932
	precision (micro=0.755, macro=0.418):
		  sm      b    baslagıç      c     km    taslak
		----  -----  ----------  -----  -----  --------
		0.14  0.311       0.642  0.352  0.128     0.938
	!precision (micro=0.797, macro=0.915):
		   sm      b    baslagıç      c     km    taslak
		-----  -----  ----------  -----  -----  --------
		0.995  0.969       0.862  0.951  0.994      0.72
	f1 (micro=0.691, macro=0.443):
		   sm      b    baslagıç      c     km    taslak
		-----  -----  ----------  -----  -----  --------
		0.235  0.371       0.601  0.411  0.215     0.826
	!f1 (micro=0.852, macro=0.916):
		  sm      b    baslagıç      c     km    taslak
		----  -----  ----------  -----  -----  --------
		0.96  0.956       0.879  0.932  0.956     0.813
	accuracy (micro=0.832, macro=0.878):
		   sm      b    baslagıç      c     km    taslak
		-----  -----  ----------  -----  -----  --------
		0.925  0.917       0.814  0.878  0.916     0.819
	fpr (micro=0.078, macro=0.078):
		   sm      b    baslagıç      c    km    taslak
		-----  -----  ----------  -----  ----  --------
		0.072  0.057       0.103  0.086  0.08     0.068
	roc_auc (micro=0.918, macro=0.899):
		   sm      b    baslagıç      c     km    taslak
		-----  -----  ----------  -----  -----  --------
		0.935  0.857       0.881  0.853  0.919     0.949
	pr_auc (micro=0.783, macro=0.503):
		   sm      b    baslagıç      c     km    taslak
		-----  -----  ----------  -----  -----  --------
		0.308  0.392       0.643  0.492  0.234     0.951
	
	 - score_schema: {'type': 'object', 'properties': {'probability': {'type': 'object', 'description': 'A mapping of probabilities onto each of the potential output labels', 'properties': {'sm': {'type': 'number'}, 'b': {'type': 'number'}, 'baslagıç': {'type': 'number'}, 'c': {'type': 'number'}, 'km': {'type': 'number'}, 'taslak': {'type': 'number'}}}, 'prediction': {'type': 'string', 'description': 'The most likely label predicted by the estimator'}}, 'title': 'Scikit learn-based classifier score with probability'}

