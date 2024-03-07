import pandas as pd
import numpy as np
import warnings

from tda_cover_parameters_tuning import CoverTuning
from umap.umap_ import UMAP
from sklearn.manifold import TSNE  

warnings.filterwarnings("ignore")

## LOAD DATA ####################################################################################################################################
data_dir = 'your data directory here'

data = pd.read_csv(data_dir + 'file_name')
x = ...
y = ...

# Define Cover parameters ranges
res_range = [0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65, 0.70, 0.75]
gain_range = [10,15,20,25,30,35,40,45,50]

## COVER PARAMETERS TUNING #####################################################################################################################
cover_tuning_umap = CoverTuning(data=x, projector=UMAP, 
                           res_range=res_range, gain_range=gain_range, 
                           n_bootstrap=5, seed_value=42)

cover_tuning_tsne = CoverTuning(data=x, projector=TSNE, 
                           res_range=res_range, gain_range=gain_range, 
                           n_bootstrap=5, seed_value=42)

matrix_distance_results_umap = cover_tuning_umap.grid_search()
matrix_distance_results_tsne = cover_tuning_tsne.grid_search()

## SAVE RESULTS ################################################################################################################################
np.savetxt('matrix_netsimile_umap.csv', matrix_distance_results_umap, delimiter=',')
np.savetxt('matrix_netsimile_tsne.csv', matrix_distance_results_tsne, delimiter=',')


