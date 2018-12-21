Model Information:
	 - type: GradientBoosting
	 - version: 0.3.0
	 - params: {'warm_start': False, 'verbose': 0, 'max_leaf_nodes': None, 'subsample': 1.0, 'labels': ['validated', 'not_proofread', 'proofread', 'without_text'], 'presort': 'auto', 'max_features': 'log2', 'random_state': None, 'learning_rate': 0.01, 'scale': True, 'min_samples_split': 2, 'multilabel': False, 'max_depth': 7, 'min_impurity_decrease': 0.0, 'criterion': 'friedman_mse', 'loss': 'deviance', 'center': True, 'init': None, 'min_impurity_split': None, 'n_estimators': 700, 'min_weight_fraction_leaf': 0.0, 'population_rates': None, 'min_samples_leaf': 1, 'label_weights': None}
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
	counts (n=20000):
		label               n         ~validated    ~not_proofread    ~proofread    ~without_text
		---------------  ----  ---  ------------  ----------------  ------------  ---------------
		'validated'      5000  -->          3284               537          1159               20
		'not_proofread'  5000  -->           820              3517           598               65
		'proofread'      5000  -->          1595               607          2786               12
		'without_text'   5000  -->            76               148            14             4762
	rates:
		              'validated'    'not_proofread'    'proofread'    'without_text'
		----------  -------------  -----------------  -------------  ----------------
		sample              0.25               0.25           0.25              0.25
		population          0.173              0.499          0.296             0.032
	match_rate (micro=0.315, macro=0.232):
		  validated    without_text    proofread    not_proofread
		-----------  --------------  -----------  ---------------
		      0.251           0.036        0.248            0.394
	filter_rate (micro=0.685, macro=0.768):
		  validated    without_text    proofread    not_proofread
		-----------  --------------  -----------  ---------------
		      0.749           0.964        0.752            0.606
	recall (micro=0.66, macro=0.717):
		  validated    without_text    proofread    not_proofread
		-----------  --------------  -----------  ---------------
		      0.657           0.952        0.557            0.703
	!recall (micro=0.893, macro=0.906):
		  validated    without_text    proofread    not_proofread
		-----------  --------------  -----------  ---------------
		      0.834           0.994        0.882            0.914
	precision (micro=0.746, macro=0.709):
		  validated    without_text    proofread    not_proofread
		-----------  --------------  -----------  ---------------
		      0.452           0.828        0.665            0.891
	!precision (micro=0.813, macro=0.875):
		  validated    without_text    proofread    not_proofread
		-----------  --------------  -----------  ---------------
		      0.921           0.998        0.825            0.755
	f1 (micro=0.693, macro=0.704):
		  validated    without_text    proofread    not_proofread
		-----------  --------------  -----------  ---------------
		      0.536           0.886        0.606            0.786
	!f1 (micro=0.848, macro=0.888):
		  validated    without_text    proofread    not_proofread
		-----------  --------------  -----------  ---------------
		      0.875           0.996        0.853            0.827
	accuracy (micro=0.807, macro=0.848):
		  validated    without_text    proofread    not_proofread
		-----------  --------------  -----------  ---------------
		      0.803           0.992        0.786            0.809
	fpr (micro=0.107, macro=0.094):
		  validated    without_text    proofread    not_proofread
		-----------  --------------  -----------  ---------------
		      0.166           0.006        0.118            0.086
	roc_auc (micro=0.889, macro=0.904):
		  validated    without_text    proofread    not_proofread
		-----------  --------------  -----------  ---------------
		      0.861           0.989        0.852            0.913
	pr_auc (micro=0.79, macro=0.776):
		  validated    without_text    proofread    not_proofread
		-----------  --------------  -----------  ---------------
		      0.517            0.95        0.722            0.915
	
	 - score_schema: {'title': 'Scikit learn-based classifier score with probability', 'type': 'object', 'properties': {'prediction': {'description': 'The most likely label predicted by the estimator', 'type': 'string'}, 'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object', 'properties': {'validated': {'type': 'number'}, 'without_text': {'type': 'number'}, 'proofread': {'type': 'number'}, 'not_proofread': {'type': 'number'}}}}}

