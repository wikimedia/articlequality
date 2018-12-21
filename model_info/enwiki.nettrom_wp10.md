Model Information:
	 - type: GradientBoosting
	 - version: 0.8.1
	 - params: {'random_state': None, 'learning_rate': 0.01, 'max_features': 'log2', 'scale': True, 'presort': 'auto', 'verbose': 0, 'criterion': 'friedman_mse', 'center': True, 'min_impurity_decrease': 0.0, 'multilabel': False, 'min_impurity_split': None, 'warm_start': False, 'subsample': 1.0, 'init': None, 'population_rates': None, 'max_depth': 3, 'max_leaf_nodes': None, 'loss': 'deviance', 'min_weight_fraction_leaf': 0.0, 'label_weights': None, 'n_estimators': 100, 'labels': ['Stub', 'Start', 'C', 'B', 'GA', 'FA'], 'min_samples_split': 2, 'min_samples_leaf': 1}
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
	counts (n=32416):
		label       n         ~Stub    ~Start    ~C    ~B    ~GA    ~FA
		-------  ----  ---  -------  --------  ----  ----  -----  -----
		'Stub'   5483  -->     4723       720    13    26      1      0
		'Start'  5473  -->      854      3601   439   438    130     11
		'C'      5483  -->       95      1516  1447  1199    960    266
		'B'      5486  -->       45       996   899  1832   1018    696
		'GA'     5495  -->        3       149   305   240   3224   1574
		'FA'     4996  -->        1         4    37   222   1000   3732
	rates:
		              'Stub'    'Start'    'C'    'B'    'GA'    'FA'
		----------  --------  ---------  -----  -----  ------  ------
		sample         0.169      0.169  0.169  0.169    0.17   0.154
		population     0.576      0.322  0.054  0.035    0.01   0.003
	match_rate (micro=0.399, macro=0.198):
		    B    GA      C    Start    Stub     FA
		-----  ----  -----  -------  ------  -----
		0.088  0.12  0.074    0.297   0.512  0.095
	filter_rate (micro=0.601, macro=0.802):
		    B    GA      C    Start    Stub     FA
		-----  ----  -----  -------  ------  -----
		0.912  0.88  0.926    0.703   0.488  0.905
	recall (micro=0.742, macro=0.575):
		    B     GA      C    Start    Stub     FA
		-----  -----  -----  -------  ------  -----
		0.334  0.587  0.264    0.658   0.861  0.747
	!recall (micro=0.931, macro=0.915):
		    B     GA      C    Start    Stub     FA
		-----  -----  -----  -------  ------  -----
		0.921  0.885  0.937    0.874   0.963  0.907
	precision (micro=0.804, macro=0.346):
		    B     GA      C    Start    Stub     FA
		-----  -----  -----  -------  ------  -----
		0.131  0.048  0.195    0.713   0.969  0.021
	!precision (micro=0.852, macro=0.934):
		    B     GA      C    Start    Stub     FA
		-----  -----  -----  -------  ------  -----
		0.975  0.995  0.957    0.843   0.836  0.999
	f1 (micro=0.766, macro=0.356):
		    B     GA      C    Start    Stub     FA
		-----  -----  -----  -------  ------  -----
		0.189  0.089  0.224    0.685   0.912  0.041
	!f1 (micro=0.889, macro=0.923):
		    B     GA      C    Start    Stub     FA
		-----  -----  -----  -------  ------  -----
		0.947  0.937  0.947    0.858   0.895  0.951
	accuracy (micro=0.872, macro=0.883):
		    B     GA    C    Start    Stub     FA
		-----  -----  ---  -------  ------  -----
		0.901  0.882  0.9    0.805   0.904  0.907
	fpr (micro=0.069, macro=0.085):
		    B     GA      C    Start    Stub     FA
		-----  -----  -----  -------  ------  -----
		0.079  0.115  0.063    0.126   0.037  0.093
	roc_auc (micro=0.93, macro=0.879):
		    B     GA      C    Start    Stub     FA
		-----  -----  -----  -------  ------  -----
		0.791  0.878  0.811    0.886   0.976  0.934
	pr_auc (micro=0.821, macro=0.358):
		    B     GA      C    Start    Stub     FA
		-----  -----  -----  -------  ------  -----
		0.136  0.062  0.174    0.748    0.98  0.048
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'prediction': {'description': 'The most likely label predicted by the estimator', 'type': 'string'}, 'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object', 'properties': {'B': {'type': 'number'}, 'GA': {'type': 'number'}, 'C': {'type': 'number'}, 'Start': {'type': 'number'}, 'Stub': {'type': 'number'}, 'FA': {'type': 'number'}}}}}

