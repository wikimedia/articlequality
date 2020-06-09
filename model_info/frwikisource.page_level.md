Model Information:
	 - type: GradientBoosting
	 - version: 0.3.0
	 - params: {'loss': 'deviance', 'label_weights': None, 'min_impurity_split': None, 'max_leaf_nodes': None, 'center': True, 'n_estimators': 700, 'presort': 'deprecated', 'learning_rate': 0.01, 'criterion': 'friedman_mse', 'max_depth': 7, 'tol': 0.0001, 'scale': True, 'max_features': 'log2', 'subsample': 1.0, 'min_weight_fraction_leaf': 0.0, 'min_impurity_decrease': 0.0, 'init': None, 'population_rates': None, 'validation_fraction': 0.1, 'min_samples_split': 2, 'n_iter_no_change': None, 'labels': ['validated', 'not_proofread', 'proofread', 'without_text'], 'multilabel': False, 'min_samples_leaf': 1, 'warm_start': False, 'verbose': 0, 'random_state': None, 'ccp_alpha': 0.0}
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
	counts (n=20000):
		label               n         ~validated    ~not_proofread    ~proofread    ~without_text
		---------------  ----  ---  ------------  ----------------  ------------  ---------------
		'validated'      5000  -->          3274               540          1167               19
		'not_proofread'  5000  -->           822              3521           588               69
		'proofread'      5000  -->          1615               612          2760               13
		'without_text'   5000  -->            58               144            16             4782
	rates:
		              'validated'    'not_proofread'    'proofread'    'without_text'
		----------  -------------  -----------------  -------------  ----------------
		sample              0.25               0.25           0.25              0.25
		population          0.173              0.499          0.296             0.032
	match_rate (micro=0.315, macro=0.232):
		  validated    not_proofread    proofread    without_text
		-----------  ---------------  -----------  --------------
		      0.251            0.395        0.247           0.037
	filter_rate (micro=0.685, macro=0.768):
		  validated    not_proofread    proofread    without_text
		-----------  ---------------  -----------  --------------
		      0.749            0.605        0.753           0.963
	recall (micro=0.659, macro=0.717):
		  validated    not_proofread    proofread    without_text
		-----------  ---------------  -----------  --------------
		      0.655            0.704        0.552           0.956
	!recall (micro=0.893, macro=0.906):
		  validated    not_proofread    proofread    without_text
		-----------  ---------------  -----------  --------------
		      0.834            0.914        0.882           0.993
	precision (micro=0.745, macro=0.707):
		  validated    not_proofread    proofread    without_text
		-----------  ---------------  -----------  --------------
		      0.451             0.89        0.663           0.823
	!precision (micro=0.812, macro=0.875):
		  validated    not_proofread    proofread    without_text
		-----------  ---------------  -----------  --------------
		       0.92            0.756        0.824           0.999
	f1 (micro=0.691, macro=0.702):
		  validated    not_proofread    proofread    without_text
		-----------  ---------------  -----------  --------------
		      0.534            0.786        0.602           0.885
	!f1 (micro=0.848, macro=0.888):
		  validated    not_proofread    proofread    without_text
		-----------  ---------------  -----------  --------------
		      0.875            0.827        0.852           0.996
	accuracy (micro=0.806, macro=0.847):
		  validated    not_proofread    proofread    without_text
		-----------  ---------------  -----------  --------------
		      0.803            0.809        0.784           0.992
	fpr (micro=0.107, macro=0.094):
		  validated    not_proofread    proofread    without_text
		-----------  ---------------  -----------  --------------
		      0.166            0.086        0.118           0.007
	roc_auc (micro=0.889, macro=0.904):
		  validated    not_proofread    proofread    without_text
		-----------  ---------------  -----------  --------------
		      0.861            0.914        0.851           0.989
	pr_auc (micro=0.79, macro=0.776):
		  validated    not_proofread    proofread    without_text
		-----------  ---------------  -----------  --------------
		      0.518            0.915        0.721           0.951
	
	 - score_schema: {'properties': {'prediction': {'description': 'The most likely label predicted by the estimator', 'type': 'string'}, 'probability': {'description': 'A mapping of probabilities onto each of the potential output labels', 'properties': {'without_text': {'type': 'number'}, 'not_proofread': {'type': 'number'}, 'validated': {'type': 'number'}, 'proofread': {'type': 'number'}}, 'type': 'object'}}, 'title': 'Scikit learn-based classifier score with probability', 'type': 'object'}

