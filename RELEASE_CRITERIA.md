This repository/package/projects uses semantic versioning.  See https://semver.org

# When to make a new release
Any substantial change to either the code of the package or the install requirements that 
may affect code execution -- e.g. a change in the version of `revscoring` -- should 
cause a version increment.  

Adding a new feature_list should require a minor-level increment.  Fixing a bug in feature 
extraction or including new features (that otherwise already exist) requites a patch-level 
increment.  A minor change to revscoring requirement requires a patch-level increment but a
major-level change will require at least a minor-level increment. 

# When you don't need to make a new release
* Re-training a model 
* Adding a model (without changing features) 
