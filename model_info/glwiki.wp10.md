Model Information:
	 - type: GradientBoosting
	 - version: 0.8.0
	 - params: {'multilabel': False, 'min_samples_split': 2, 'max_features': 'log2', 'loss': 'deviance', 'max_depth': 3, 'population_rates': None, 'subsample': 1.0, 'learning_rate': 0.01, 'tol': 0.0001, 'init': None, 'label_weights': None, 'min_weight_fraction_leaf': 0.0, 'n_estimators': 500, 'validation_fraction': 0.1, 'verbose': 0, 'labels': ['Stub', 'Start', 'C', 'B', 'GA', 'FA'], 'min_impurity_split': None, 'min_impurity_decrease': 0.0, 'presort': 'auto', 'random_state': None, 'max_leaf_nodes': None, 'center': True, 'warm_start': False, 'min_samples_leaf': 1, 'criterion': 'friedman_mse', 'n_iter_no_change': None, 'scale': True}
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
	counts (n=401):
		label      n         ~Stub    ~Start    ~C    ~B    ~GA    ~FA
		-------  ---  ---  -------  --------  ----  ----  -----  -----
		'Stub'    67  -->       46        21     0     0      0      0
		'Start'   67  -->       23        24    13     4      3      0
		'C'       67  -->        2        11    29    15      5      5
		'B'       67  -->        1         3    16    19     12     16
		'GA'      66  -->        0         2     9    11     32     12
		'FA'      67  -->        0         0     7    17      8     35
	rates:
		          'Stub'    'Start'    'C'    'B'    'GA'    'FA'
		------  --------  ---------  -----  -----  ------  ------
		sample     0.167      0.167  0.167  0.167   0.165   0.167
	match_rate (micro=0.167, macro=0.167):
		  GA      C    FA    Stub      B    Start
		----  -----  ----  ------  -----  -------
		0.15  0.185  0.17    0.18  0.165    0.152
	filter_rate (micro=0.833, macro=0.833):
		  GA      C    FA    Stub      B    Start
		----  -----  ----  ------  -----  -------
		0.85  0.815  0.83    0.82  0.835    0.848
	recall (micro=0.461, macro=0.461):
		   GA      C     FA    Stub      B    Start
		-----  -----  -----  ------  -----  -------
		0.485  0.433  0.522   0.687  0.284    0.358
	!recall (micro=0.892, macro=0.892):
		   GA      C     FA    Stub      B    Start
		-----  -----  -----  ------  -----  -------
		0.916  0.865  0.901   0.922  0.859    0.889
	precision (micro=0.46, macro=0.46):
		   GA      C     FA    Stub      B    Start
		-----  -----  -----  ------  -----  -------
		0.533  0.392  0.515   0.639  0.288    0.393
	!precision (micro=0.892, macro=0.892):
		  GA      C     FA    Stub      B    Start
		----  -----  -----  ------  -----  -------
		 0.9  0.884  0.904   0.936  0.857    0.874
	f1 (micro=0.46, macro=0.46):
		   GA      C     FA    Stub      B    Start
		-----  -----  -----  ------  -----  -------
		0.508  0.411  0.519   0.662  0.286    0.375
	!f1 (micro=0.892, macro=0.892):
		   GA      C     FA    Stub      B    Start
		-----  -----  -----  ------  -----  -------
		0.908  0.874  0.903   0.929  0.858    0.881
	accuracy (micro=0.82, macro=0.82):
		   GA      C     FA    Stub      B    Start
		-----  -----  -----  ------  -----  -------
		0.845  0.793  0.838   0.883  0.763      0.8
	fpr (micro=0.108, macro=0.108):
		   GA      C     FA    Stub      B    Start
		-----  -----  -----  ------  -----  -------
		0.084  0.135  0.099   0.078  0.141    0.111
	roc_auc (micro=0.805, macro=0.805):
		   GA      C     FA    Stub      B    Start
		-----  -----  -----  ------  -----  -------
		0.821  0.744  0.844   0.941  0.714    0.766
	pr_auc (micro=0.459, macro=0.459):
		   GA     C     FA    Stub      B    Start
		-----  ----  -----  ------  -----  -------
		0.519  0.38  0.482   0.678  0.319    0.376
	
	 - score_schema: {'properties': {'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'properties': {'GA': {'type': 'number'}, 'C': {'type': 'number'}, 'FA': {'type': 'number'}, 'Stub': {'type': 'number'}, 'B': {'type': 'number'}, 'Start': {'type': 'number'}}, 'type': 'object'}, 'prediction': {'description': 'The most likely label predicted by the estimator', 'type': 'string'}}, 'type': 'object', 'title': 'Scikit learn-based classifier score with probability'}

