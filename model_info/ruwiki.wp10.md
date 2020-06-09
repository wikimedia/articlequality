Model Information:
	 - type: GradientBoosting
	 - version: 0.8.0
	 - params: {'random_state': None, 'presort': 'deprecated', 'ccp_alpha': 0.0, 'population_rates': None, 'criterion': 'friedman_mse', 'max_depth': 5, 'min_impurity_decrease': 0.0, 'tol': 0.0001, 'max_features': 'log2', 'multilabel': False, 'min_samples_split': 2, 'loss': 'deviance', 'init': None, 'warm_start': False, 'validation_fraction': 0.1, 'labels': ['IV', 'III', 'II', 'I', 'ХС', 'ДС', 'ИС'], 'min_weight_fraction_leaf': 0.0, 'verbose': 0, 'n_estimators': 300, 'min_samples_leaf': 1, 'max_leaf_nodes': None, 'subsample': 1.0, 'scale': True, 'center': True, 'learning_rate': 0.01, 'label_weights': None, 'n_iter_no_change': None, 'min_impurity_split': None}
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
	counts (n=10282):
		label       n         ~IV    ~III    ~II    ~I    ~ХС    ~ДС    ~ИС
		-------  ----  ---  -----  ------  -----  ----  -----  -----  -----
		'IV'     1465  -->   1078     291     55     6      4     26      5
		'III'    1465  -->    402     625    275    28     15    108     12
		'II'     1461  -->     97     286    511   154    119    257     37
		'I'      1458  -->     51     104    252   247    357    273    174
		'ХС'     1469  -->     11      15     33   119    913    114    264
		'ДС'     1488  -->      2      59     55    34    110   1215     13
		'ИС'     1476  -->     13      18     15    51    280     55   1044
	rates:
		              'IV'    'III'    'II'    'I'    'ХС'    'ДС'    'ИС'
		----------  ------  -------  ------  -----  ------  ------  ------
		sample       0.142    0.142   0.142  0.142   0.143   0.145   0.144
		population   0.487    0.363   0.093  0.029   0.011   0.009   0.007
	match_rate (micro=0.281, macro=0.146):
		   IV    III     II      I     ХС     ДС     ИС
		-----  -----  -----  -----  -----  -----  -----
		0.392  0.211  0.103  0.048  0.106  0.101  0.062
	filter_rate (micro=0.719, macro=0.854):
		   IV    III     II      I     ХС     ДС     ИС
		-----  -----  -----  -----  -----  -----  -----
		0.608  0.789  0.897  0.952  0.894  0.899  0.938
	recall (micro=0.571, macro=0.547):
		   IV    III    II      I     ХС     ДС     ИС
		-----  -----  ----  -----  -----  -----  -----
		0.736  0.427  0.35  0.169  0.622  0.817  0.707
	!recall (micro=0.925, macro=0.925):
		   IV    III     II      I    ХС     ДС     ИС
		-----  -----  -----  -----  ----  -----  -----
		0.935  0.912  0.922  0.956   0.9  0.905  0.943
	precision (micro=0.746, macro=0.328):
		   IV    III     II      I     ХС     ДС     ИС
		-----  -----  -----  -----  -----  -----  -----
		0.915  0.735  0.316  0.102  0.067  0.075  0.085
	!precision (micro=0.794, macro=0.918):
		   IV    III     II      I     ХС     ДС     ИС
		-----  -----  -----  -----  -----  -----  -----
		0.788  0.737  0.933  0.975  0.995  0.998  0.998
	f1 (micro=0.631, macro=0.318):
		   IV    III     II      I    ХС     ДС     ИС
		-----  -----  -----  -----  ----  -----  -----
		0.816   0.54  0.332  0.128  0.12  0.137  0.152
	!f1 (micro=0.853, macro=0.918):
		   IV    III     II      I     ХС     ДС     ИС
		-----  -----  -----  -----  -----  -----  -----
		0.855  0.815  0.927  0.965  0.945  0.949  0.969
	accuracy (micro=0.809, macro=0.874):
		   IV    III     II      I     ХС     ДС     ИС
		-----  -----  -----  -----  -----  -----  -----
		0.838  0.736  0.869  0.933  0.896  0.904  0.941
	fpr (micro=0.075, macro=0.075):
		   IV    III     II      I    ХС     ДС     ИС
		-----  -----  -----  -----  ----  -----  -----
		0.065  0.088  0.078  0.044   0.1  0.095  0.057
	roc_auc (micro=0.889, macro=0.871):
		   IV    III     II      I     ХС     ДС     ИС
		-----  -----  -----  -----  -----  -----  -----
		0.941  0.854  0.792  0.737  0.897  0.941  0.937
	pr_auc (micro=0.748, macro=0.357):
		   IV    III     II      I     ХС     ДС     ИС
		-----  -----  -----  -----  -----  -----  -----
		0.924  0.736  0.266  0.088  0.085  0.127  0.272
	
	 - score_schema: {'properties': {'probability': {'properties': {'IV': {'type': 'number'}, 'III': {'type': 'number'}, 'II': {'type': 'number'}, 'ДС': {'type': 'number'}, 'I': {'type': 'number'}, 'ХС': {'type': 'number'}, 'ИС': {'type': 'number'}}, 'description': 'A mapping of probabilities onto each of the potential output labels', 'type': 'object'}, 'prediction': {'description': 'The most likely label predicted by the estimator', 'type': 'string'}}, 'type': 'object', 'title': 'Scikit learn-based classifier score with probability'}

