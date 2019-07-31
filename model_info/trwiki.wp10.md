Model Information:
	 - type: GradientBoosting
	 - version: 0.8.0
	 - params: {'max_leaf_nodes': None, 'presort': 'auto', 'init': None, 'max_depth': 5, 'labels': ['taslak', 'baslagıç', 'c', 'b', 'km', 'sm'], 'tol': 0.0001, 'min_weight_fraction_leaf': 0.0, 'scale': True, 'verbose': 0, 'min_samples_leaf': 1, 'center': True, 'learning_rate': 0.01, 'population_rates': None, 'warm_start': False, 'validation_fraction': 0.1, 'label_weights': None, 'subsample': 1.0, 'min_impurity_decrease': 0.0, 'loss': 'deviance', 'n_iter_no_change': None, 'n_estimators': 300, 'random_state': None, 'multilabel': False, 'criterion': 'friedman_mse', 'max_features': 'log2', 'min_samples_split': 2, 'min_impurity_split': None}
	Environment:
	 - revscoring_version: '2.5.1'
	 - platform: 'Linux-4.9.0-9-amd64-x86_64-with-debian-9.9'
	 - machine: 'x86_64'
	 - version: '#1 SMP Debian 4.9.168-1+deb9u2 (2019-05-13)'
	 - system: 'Linux'
	 - processor: ''
	 - python_build: ('default', 'Sep 27 2018 17:25:39')
	 - python_compiler: 'GCC 6.3.0 20170516'
	 - python_branch: ''
	 - python_implementation: 'CPython'
	 - python_revision: ''
	 - python_version: '3.5.3'
	 - release: '4.9.0-9-amd64'
	
	Statistics:
	counts (n=1614):
		label         n         ~taslak    ~baslagıç    ~c    ~b    ~km    ~sm
		----------  ---  ---  ---------  -----------  ----  ----  -----  -----
		'taslak'    267  -->        199           66     2     0      0      0
		'baslagıç'  271  -->         69          152    43     3      4      0
		'c'         269  -->         13           52   137    34     27      6
		'b'         270  -->          5           18    39   124     41     43
		'km'        267  -->          1            4    24    15    184     39
		'sm'        270  -->          2            3     7    25     38    195
	rates:
		              'taslak'    'baslagıç'    'c'    'b'    'km'    'sm'
		----------  ----------  ------------  -----  -----  ------  ------
		sample           0.165         0.168  0.167  0.167   0.165   0.167
		population       0.58          0.248  0.086  0.053   0.017   0.016
	match_rate (micro=0.339, macro=0.175):
		  taslak     km      b    baslagıç     sm      c
		--------  -----  -----  ----------  -----  -----
		   0.461  0.092  0.079       0.219  0.076  0.122
	filter_rate (micro=0.661, macro=0.825):
		  taslak     km      b    baslagıç     sm      c
		--------  -----  -----  ----------  -----  -----
		   0.539  0.908  0.921       0.781  0.924  0.878
	recall (micro=0.663, macro=0.614):
		  taslak     km      b    baslagıç     sm      c
		--------  -----  -----  ----------  -----  -----
		   0.745  0.689  0.459       0.561  0.722  0.509
	!recall (micro=0.922, macro=0.923):
		  taslak     km      b    baslagıç     sm      c
		--------  -----  -----  ----------  -----  -----
		   0.933  0.918  0.943       0.894  0.935  0.914
	precision (micro=0.754, macro=0.42):
		  taslak     km      b    baslagıç    sm      c
		--------  -----  -----  ----------  ----  -----
		   0.939  0.127  0.311       0.634  0.15  0.359
	!precision (micro=0.8, macro=0.916):
		  taslak     km      b    baslagıç     sm      c
		--------  -----  -----  ----------  -----  -----
		   0.726  0.994  0.969       0.861  0.995  0.952
	f1 (micro=0.693, macro=0.447):
		  taslak     km      b    baslagıç     sm      c
		--------  -----  -----  ----------  -----  -----
		   0.831  0.215  0.371       0.595  0.248  0.421
	!f1 (micro=0.854, macro=0.917):
		  taslak     km      b    baslagıç     sm      c
		--------  -----  -----  ----------  -----  -----
		   0.817  0.955  0.956       0.877  0.964  0.933
	accuracy (micro=0.834, macro=0.88):
		  taslak     km      b    baslagıç     sm     c
		--------  -----  -----  ----------  -----  ----
		   0.824  0.914  0.917       0.811  0.931  0.88
	fpr (micro=0.078, macro=0.077):
		  taslak     km      b    baslagıç     sm      c
		--------  -----  -----  ----------  -----  -----
		   0.067  0.082  0.057       0.106  0.065  0.086
	roc_auc (micro=0.917, macro=0.899):
		  taslak    km      b    baslagıç     sm      c
		--------  ----  -----  ----------  -----  -----
		   0.947  0.92  0.858        0.88  0.935  0.856
	pr_auc (micro=0.784, macro=0.504):
		  taslak     km      b    baslagıç     sm      c
		--------  -----  -----  ----------  -----  -----
		    0.95  0.238  0.376       0.647  0.312  0.501
	
	 - score_schema: {'type': 'object', 'properties': {'prediction': {'type': 'string', 'description': 'The most likely label predicted by the estimator'}, 'probability': {'type': 'object', 'properties': {'taslak': {'type': 'number'}, 'km': {'type': 'number'}, 'b': {'type': 'number'}, 'baslagıç': {'type': 'number'}, 'sm': {'type': 'number'}, 'c': {'type': 'number'}}, 'description': 'A mapping of probabilities onto each of the potential output labels'}}, 'title': 'Scikit learn-based classifier score with probability'}

