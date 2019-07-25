Model Information:
	 - type: GradientBoosting
	 - version: 0.8.2
	 - params: {'max_depth': 7, 'presort': 'auto', 'multilabel': False, 'min_impurity_split': None, 'subsample': 1.0, 'max_features': 'log2', 'init': None, 'min_samples_split': 2, 'population_rates': None, 'random_state': None, 'max_leaf_nodes': None, 'verbose': 0, 'warm_start': False, 'min_impurity_decrease': 0.0, 'loss': 'deviance', 'learning_rate': 0.01, 'min_samples_leaf': 1, 'scale': True, 'label_weights': None, 'center': True, 'criterion': 'friedman_mse', 'n_estimators': 700, 'min_weight_fraction_leaf': 0.0, 'labels': ['Stub', 'Start', 'C', 'B', 'GA', 'FA']}
	Environment:
	 - revscoring_version: '2.4.0'
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
	counts (n=32402):
		label       n         ~Stub    ~Start    ~C    ~B    ~GA    ~FA
		-------  ----  ---  -------  --------  ----  ----  -----  -----
		'Stub'   5477  -->     4670       769    23    14      1      0
		'Start'  5469  -->      700      3512   866   329     60      2
		'C'      5480  -->       66      1002  2717  1082    524     89
		'B'      5485  -->       34       655  1411  2190    853    342
		'GA'     5495  -->        3        34   332   346   3514   1266
		'FA'     4996  -->        0         3    24   233    944   3792
	rates:
		              'Stub'    'Start'    'C'    'B'    'GA'    'FA'
		----------  --------  ---------  -----  -----  ------  ------
		sample         0.169      0.169  0.169  0.169    0.17   0.154
		population     0.576      0.322  0.054  0.035    0.01   0.003
	match_rate (micro=0.388, macro=0.189):
		   GA    Stub     C      B    Start     FA
		-----  ------  ----  -----  -------  -----
		0.094   0.504  0.12  0.086    0.269  0.064
	filter_rate (micro=0.612, macro=0.811):
		   GA    Stub     C      B    Start     FA
		-----  ------  ----  -----  -------  -----
		0.906   0.496  0.88  0.914    0.731  0.936
	recall (micro=0.747, macro=0.631):
		   GA    Stub      C      B    Start     FA
		-----  ------  -----  -----  -------  -----
		0.639   0.853  0.496  0.399    0.642  0.759
	!recall (micro=0.944, macro=0.926):
		   GA    Stub      C      B    Start     FA
		-----  ------  -----  -----  -------  -----
		0.911    0.97  0.901  0.926    0.909  0.938
	precision (micro=0.828, macro=0.371):
		   GA    Stub      C      B    Start     FA
		-----  ------  -----  -----  -------  -----
		0.067   0.975  0.225  0.161     0.77  0.031
	!precision (micro=0.848, macro=0.935):
		   GA    Stub      C      B    Start     FA
		-----  ------  -----  -----  -------  -----
		0.996   0.829  0.969  0.977    0.842  0.999
	f1 (micro=0.776, macro=0.388):
		   GA    Stub      C      B    Start    FA
		-----  ------  -----  -----  -------  ----
		0.121    0.91  0.309  0.229      0.7  0.06
	!f1 (micro=0.892, macro=0.929):
		   GA    Stub      C      B    Start     FA
		-----  ------  -----  -----  -------  -----
		0.952   0.894  0.934  0.951    0.874  0.968
	accuracy (micro=0.876, macro=0.893):
		   GA    Stub      C      B    Start     FA
		-----  ------  -----  -----  -------  -----
		0.909   0.902  0.879  0.907    0.823  0.938
	fpr (micro=0.056, macro=0.074):
		   GA    Stub      C      B    Start     FA
		-----  ------  -----  -----  -------  -----
		0.089    0.03  0.099  0.074    0.091  0.062
	roc_auc (micro=0.942, macro=0.906):
		   GA    Stub      C      B    Start     FA
		-----  ------  -----  -----  -------  -----
		0.912   0.978  0.857  0.833    0.904  0.955
	pr_auc (micro=0.841, macro=0.401):
		   GA    Stub     C      B    Start     FA
		-----  ------  ----  -----  -------  -----
		0.137   0.983  0.25  0.173    0.787  0.077
	
	 - score_schema: {'properties': {'prediction': {'description': 'The most likely label predicted by the estimator', 'type': 'string'}, 'probability': {'type': 'object', 'description': 'A mapping of probabilities onto each of the potential output labels', 'properties': {'GA': {'type': 'number'}, 'Stub': {'type': 'number'}, 'C': {'type': 'number'}, 'B': {'type': 'number'}, 'Start': {'type': 'number'}, 'FA': {'type': 'number'}}}}, 'type': 'object', 'title': 'Scikit learn-based classifier score with probability'}

