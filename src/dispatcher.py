# Create all the models and parameter
# List down all the models
from sklearn import ensemble

MODELS = {
    "rf": ensemble.RandomForestClassifier(n_estimators = 200, n_jobs = -1, verbose = 2),
    
    "et": ensemble.ExtraTreesClassifier(n_estimators = 200, n_jobs = -1, verbose = 2) 

}
