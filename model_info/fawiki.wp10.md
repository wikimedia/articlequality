Model Information:
	 - type: GradientBoosting
	 - version: 0.8.0
	 - params: {'n_iter_no_change': None, 'min_samples_leaf': 1, 'label_weights': None, 'min_impurity_decrease': 0.0, 'min_samples_split': 2, 'scale': True, 'min_weight_fraction_leaf': 0.0, 'presort': 'auto', 'learning_rate': 0.5, 'verbose': 0, 'multilabel': False, 'warm_start': False, 'random_state': None, 'labels': ['Stub', 'Start', 'C', 'B', 'GA', 'FA'], 'min_impurity_split': None, 'tol': 0.0001, 'validation_fraction': 0.1, 'n_estimators': 100, 'subsample': 1.0, 'center': True, 'criterion': 'friedman_mse', 'max_leaf_nodes': None, 'loss': 'deviance', 'init': None, 'max_features': 'log2', 'max_depth': 7, 'population_rates': None}
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
	counts (n=1235):
		label      n         ~Stub    ~Start    ~C    ~B    ~GA    ~FA
		-------  ---  ---  -------  --------  ----  ----  -----  -----
		'Stub'   226  -->      168        16    28    13      1      0
		'Start'   94  -->       29        18    33    14      0      0
		'C'      152  -->       26        18    54    39     10      5
		'B'      200  -->       13        10    27    66     56     28
		'GA'     300  -->        2         3     8    31    171     85
		'FA'     263  -->        2         0     1    15     79    166
	rates:
		              'Stub'    'Start'    'C'    'B'    'GA'    'FA'
		----------  --------  ---------  -----  -----  ------  ------
		sample         0.183      0.076  0.123  0.162   0.243   0.213
		population     0.182      0.076  0.123  0.162   0.242   0.212
	match_rate (micro=0.189, macro=0.166):
		    B    Stub    FA      C     GA    Start
		-----  ------  ----  -----  -----  -------
		0.144   0.193  0.23  0.122  0.256    0.053
	filter_rate (micro=0.811, macro=0.834):
		    B    Stub    FA      C     GA    Start
		-----  ------  ----  -----  -----  -------
		0.856   0.807  0.77  0.878  0.744    0.947
	recall (micro=0.52, macro=0.47):
		   B    Stub     FA      C    GA    Start
		----  ------  -----  -----  ----  -------
		0.33   0.743  0.631  0.355  0.57    0.191
	!recall (micro=0.891, macro=0.902):
		    B    Stub     FA     C     GA    Start
		-----  ------  -----  ----  -----  -------
		0.892   0.929  0.879  0.91  0.844    0.959
	precision (micro=0.508, macro=0.471):
		   B    Stub     FA      C     GA    Start
		----  ------  -----  -----  -----  -------
		0.37   0.698  0.584  0.357  0.539    0.276
	!precision (micro=0.897, macro=0.903):
		    B    Stub     FA     C    GA    Start
		-----  ------  -----  ----  ----  -------
		0.874   0.942  0.898  0.91  0.86    0.935
	f1 (micro=0.513, macro=0.469):
		    B    Stub     FA      C     GA    Start
		-----  ------  -----  -----  -----  -------
		0.349    0.72  0.607  0.356  0.554    0.226
	!f1 (micro=0.894, macro=0.903):
		    B    Stub     FA     C     GA    Start
		-----  ------  -----  ----  -----  -------
		0.883   0.935  0.888  0.91  0.852    0.947
	accuracy (micro=0.83, macro=0.84):
		    B    Stub     FA      C     GA    Start
		-----  ------  -----  -----  -----  -------
		0.801   0.895  0.826  0.842  0.777    0.901
	fpr (micro=0.109, macro=0.098):
		    B    Stub     FA     C     GA    Start
		-----  ------  -----  ----  -----  -------
		0.108   0.071  0.121  0.09  0.156    0.041
	roc_auc (micro=0.807, macro=0.802):
		    B    Stub     FA     C     GA    Start
		-----  ------  -----  ----  -----  -------
		0.701   0.936  0.835  0.78  0.781    0.775
	pr_auc (micro=0.494, macro=0.455):
		    B    Stub     FA      C     GA    Start
		-----  ------  -----  -----  -----  -------
		0.312   0.763  0.556  0.344  0.514     0.24
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'properties': {'probability': {'properties': {'B': {'type': 'number'}, 'Stub': {'type': 'number'}, 'FA': {'type': 'number'}, 'C': {'type': 'number'}, 'GA': {'type': 'number'}, 'Start': {'type': 'number'}}, 'type': 'object', 'description': 'A mapping of probabilities onto each of the potential output labels'}, 'prediction': {'type': 'string', 'description': 'The most likely label predicted by the estimator'}}, 'type': 'object'}

