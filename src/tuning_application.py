import pandas as pd
import numpy as np
import warnings

from tda_cover_parameters_tuning import CoverTuning
from umap.umap_ import UMAP
from sklearn.manifold import TSNE  

warnings.filterwarnings("ignore")

## LOAD DATA ####################################################################################################################################
data_dir = 'your data directory here'

data_1 = pd.read_csv(data_dir + 'file_name')
data_2 = pd.read_csv(data_dir + 'file_name')

# Define Cover parameters ranges
res_range = [0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65, 0.70, 0.75]
gain_range = [10,15,20,25,30,35,40,45,50]

## COVER PARAMETERS TUNING #####################################################################################################################
# Data 1
cover_tuning_umap_1 = CoverTuning(data=data_1, projector=UMAP, 
                           res_range=res_range, gain_range=gain_range, 
                           n_bootstrap=5, seed_value=42)

cover_tuning_tsne_1 = CoverTuning(data=data_1, projector=TSNE, 
                           res_range=res_range, gain_range=gain_range, 
                           n_bootstrap=5, seed_value=42)

matrix_distance_results_umap_1 = cover_tuning_umap_1.grid_search()
matrix_distance_results_tsne_1 = cover_tuning_tsne_1.grid_search()

# Data 2
cover_tuning_umap_2 = CoverTuning(data=data_2, projector=UMAP, 
                           res_range=res_range, gain_range=gain_range, 
                           n_bootstrap=5, seed_value=42)

cover_tuning_tsne_2 = CoverTuning(data=data_2, projector=TSNE,
                            res_range=res_range, gain_range=gain_range, 
                            n_bootstrap=5, seed_value=42)

matrix_distance_results_umap_2 = cover_tuning_umap_2.grid_search()
matrix_distance_results_tsne_2 = cover_tuning_tsne_2.grid_search()

## SAVE RESULTS ################################################################################################################################
np.savetxt('matrix_netsimile_umap.csv', matrix_distance_results_umap_1, delimiter=',')
np.savetxt('matrix_netsimile_tsne.csv', matrix_distance_results_tsne_1, delimiter=',')
np.savetxt('matrix_netsimile_umap.csv', matrix_distance_results_umap_2, delimiter=',')
np.savetxt('matrix_netsimile_tsne.csv', matrix_distance_results_tsne_2, delimiter=',')


