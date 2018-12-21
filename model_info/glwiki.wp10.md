Model Information:
	 - type: GradientBoosting
	 - version: 0.8.0
	 - params: {'min_impurity_decrease': 0.0, 'min_impurity_split': None, 'multilabel': False, 'max_features': 'log2', 'warm_start': False, 'loss': 'deviance', 'center': True, 'min_samples_leaf': 1, 'criterion': 'friedman_mse', 'label_weights': None, 'verbose': 0, 'init': None, 'random_state': None, 'max_leaf_nodes': None, 'labels': ['Stub', 'Start', 'C', 'B', 'GA', 'FA'], 'population_rates': None, 'min_weight_fraction_leaf': 0.0, 'max_depth': 3, 'n_estimators': 500, 'presort': 'auto', 'subsample': 1.0, 'learning_rate': 0.01, 'min_samples_split': 2, 'scale': True}
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
	counts (n=401):
		label      n         ~Stub    ~Start    ~C    ~B    ~GA    ~FA
		-------  ---  ---  -------  --------  ----  ----  -----  -----
		'Stub'    67  -->       46        21     0     0      0      0
		'Start'   67  -->       22        25    14     3      3      0
		'C'       67  -->        2        10    29    15      5      6
		'B'       67  -->        1         4    15    19     11     17
		'GA'      66  -->        0         2     7     9     33     15
		'FA'      67  -->        0         0     5    15     10     37
	rates:
		          'Stub'    'Start'    'C'    'B'    'GA'    'FA'
		------  --------  ---------  -----  -----  ------  ------
		sample     0.167      0.167  0.167  0.167   0.165   0.167
	match_rate (micro=0.167, macro=0.167):
		    C     FA     GA      B    Start    Stub
		-----  -----  -----  -----  -------  ------
		0.175  0.187  0.155  0.152    0.155   0.177
	filter_rate (micro=0.833, macro=0.833):
		    C     FA     GA      B    Start    Stub
		-----  -----  -----  -----  -------  ------
		0.825  0.813  0.845  0.848    0.845   0.823
	recall (micro=0.471, macro=0.471):
		    C     FA    GA      B    Start    Stub
		-----  -----  ----  -----  -------  ------
		0.433  0.552   0.5  0.284    0.373   0.687
	!recall (micro=0.894, macro=0.894):
		    C     FA     GA      B    Start    Stub
		-----  -----  -----  -----  -------  ------
		0.877  0.886  0.913  0.874    0.889   0.925
	precision (micro=0.467, macro=0.467):
		    C     FA     GA      B    Start    Stub
		-----  -----  -----  -----  -------  ------
		0.414  0.493  0.532  0.311    0.403   0.648
	!precision (micro=0.894, macro=0.895):
		    C     FA     GA      B    Start    Stub
		-----  -----  -----  -----  -------  ------
		0.885  0.908  0.903  0.859    0.876   0.936
	f1 (micro=0.468, macro=0.469):
		    C     FA     GA      B    Start    Stub
		-----  -----  -----  -----  -------  ------
		0.423  0.521  0.516  0.297    0.388   0.667
	!f1 (micro=0.894, macro=0.894):
		    C     FA     GA      B    Start    Stub
		-----  -----  -----  -----  -------  ------
		0.881  0.897  0.908  0.866    0.883   0.931
	accuracy (micro=0.824, macro=0.824):
		    C    FA     GA      B    Start    Stub
		-----  ----  -----  -----  -------  ------
		0.803  0.83  0.845  0.776    0.803   0.885
	fpr (micro=0.106, macro=0.106):
		    C     FA     GA      B    Start    Stub
		-----  -----  -----  -----  -------  ------
		0.123  0.114  0.087  0.126    0.111   0.075
	roc_auc (micro=0.806, macro=0.806):
		    C     FA    GA      B    Start    Stub
		-----  -----  ----  -----  -------  ------
		0.743  0.842  0.82  0.715    0.775   0.943
	pr_auc (micro=0.466, macro=0.466):
		    C    FA     GA      B    Start    Stub
		-----  ----  -----  -----  -------  ------
		0.373  0.48  0.524  0.309    0.385   0.725
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'prediction': {'type': 'string', 'description': 'The most likely label predicted by the estimator'}, 'probability': {'type': 'object', 'description': 'A mapping of probabilities onto each of the potential output labels', 'properties': {'C': {'type': 'number'}, 'FA': {'type': 'number'}, 'GA': {'type': 'number'}, 'B': {'type': 'number'}, 'Start': {'type': 'number'}, 'Stub': {'type': 'number'}}}}}

