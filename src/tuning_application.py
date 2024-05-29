import pandas as pd
import numpy as np
import warnings

from tda_cover_parameters_tuning import CoverTuning
from umap.umap_ import UMAP
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA

warnings.filterwarnings("ignore")
seed_value = 27

## LOAD DATA ####################################################################################################################################
data_dir = 'your data directory here'

data = pd.read_csv(data_dir + 'file_name')

# Define Cover parameters ranges
gain_range = [0.30, 0.40, 0.50, 0.60, 0.70, 0.80]
res_range = [10, 20, 30, 40, 50, 60]

# Define number of bootstrap samples
n_bootstrap = 5

## COVER PARAMETERS TUNING #####################################################################################################################
cover_tuning_umap = CoverTuning(data=data, projector=UMAP, 
                           res_range=res_range, gain_range=gain_range, 
                           n_bootstrap=n_bootstrap, seed_value=seed_value)

cover_tuning_pca = CoverTuning(data=data, projector=PCA, 
                           res_range=res_range, gain_range=gain_range, 
                           n_bootstrap=n_bootstrap, seed_value=seed_value)

# NetSimile metric
matrix_distance_results_umap_netsimile = cover_tuning_umap.grid_search(metric='netsimile')
matrix_distance_results_pca_netsimile = cover_tuning_pca.grid_search(metric='netsimile')

# Clustering metric
matrix_avg_clustering_umap = cover_tuning_umap.grid_search(metric='clustering')
matrix_avg_clustering_pca = cover_tuning_pca.grid_search(metric='clustering')

## SAVE RESULTS ################################################################################################################################
np.savetxt('matrix_netsimile_umap.csv', matrix_distance_results_umap_netsimile, delimiter=',')
np.savetxt('matrix_netsimile_pca.csv', matrix_distance_results_pca_netsimile, delimiter=',')

np.savetxt('matrix_clustering_umap.csv', matrix_avg_clustering_umap, delimiter=',')
np.savetxt('matrix_clustering_pca.csv', matrix_avg_clustering_pca, delimiter=',')
