import numpy as np
import pandas as pd
import networkx as nx
import random
import kmapper as km
import netrd

from kmapper import KeplerMapper, Cover
from sklearn.cluster import DBSCAN

class CoverTuning:
    """
    A class for tuning Cover parameters in TDA Mapper using NetSimile as graph distance metric.
    
    Attributes:
    - data (pd.DataFrame): The input dataset
    - projector (class): The dimensionality reduction technique to use for the TDA Mapper
    - res_range (list): The range of resolution values to test
    - gain_range (list): The range of gain values to test
    - n_bootstrap (int): The number of bootstrap samples to generate
    - seed_value (int): The seed value for reproducibility
    """
    def __init__(self, data, projector, res_range, gain_range, n_bootstrap, seed_value):
        """Initializes the CoverTuning class with the specified parameters."""
        super().__init__()
        self.data = data
        self.projector = projector
        self.mapper = KeplerMapper(verbose=0)
        self.res_range = res_range
        self.gain_range = gain_range
        self.n_bootstrap = n_bootstrap
        self.seed_value = seed_value

    def create_tda_graph(self, x, perc_overlap, n_cubes):
        """
        Creates a TDA Mapper graph based on the input dataset and specified Cover parameters.

        Parameters:
        - x (np.ndarray): The input dataset
        - perc_overlap (float): The percentage overlap for the Cover
        - n_cubes (int): The number of cubes for the Cover

        Returns:
        - nx.Graph: A NetworkX graph representing the TDA Mapper output
        """
        lens = self.mapper.fit_transform(x, self.projector(n_components=2, random_state=self.seed_value))
        graph = self.mapper.map(
            lens, X=x,
            cover=Cover(perc_overlap=perc_overlap, n_cubes=n_cubes),
            clusterer=DBSCAN(metric='euclidean', min_samples=5, eps=2)
        )

        return km.adapter.to_nx(graph)
    
    def get_bootstrap_sample(self, sample_ratio=0.7):
        """
        Generates a collection of bootstrap samples from the input dataset.

        Parameters:
        - sample_ratio (float, optional): The ratio of samples to be drawn from the dataset 
        for each bootstrap iteration. Defaults to 0.7

        Returns:
        - List: A list containing numpy arrays representing the bootstrap samples
        """
        data_idx = self.data.index.tolist()
        idx_bootstrap = {}
        bootstrap_data = []

        random.seed(self.seed_value)

        for i in range(0, self.n_bootstrap):
            y = random.sample(data_idx, round(len(data_idx)*sample_ratio))
            idx_bootstrap[i] = y
            idx_bootstrap_df = pd.DataFrame(idx_bootstrap)

            current_idx = idx_bootstrap_df.iloc[:,i].to_list()
            all_data = self.data.iloc[current_idx,:]
            bootstrap_data.append(all_data)

        X_arrays = [array.to_numpy() for array in bootstrap_data]
        return X_arrays
    
    def graph_distance_metric(self, graph_list):
        """
        Computes the average distance between graphs based on NetSimile.

        Parameters:
        - graph_list (list): A list of NetworkX graphs to compute distances between

        Returns:
        - float: The average distance between graphs based on NetSimile
        """        
        distance = []
        n_graphs = len(graph_list)

        for i in range(0, n_graphs):
            for j in range(i+1, n_graphs):
                distance.append(netrd.distance.NetSimile().dist(graph_list[i], graph_list[j]))

        distance = np.array(distance)
        return np.mean(distance)
    
    def clustering_metric(self, graph_list):
        """
        Computes the average clustering coefficient of the input graphs.

        Parameters:
        - graph_list (list): A list of NetworkX graphs to compute clustering coefficients for

        Returns:
        - float: The average clustering coefficient of the input graphs
        """
        clustering_coefficients = []
        for graph in graph_list:
            clustering_coefficients.append(nx.average_clustering(graph))

        return np.mean(clustering_coefficients)
    
    def grid_search(self, metric):
        """
        Conducts a grid search over the specified Cover parameter ranges and computes the average graph distance
        between the resulting TDA Mapper graphs using NetSimile.

        Returns:
        - np.ndarray: A matrix containing the average graph distances for each combination of Cover parameters
        """
        matrix = np.zeros((len(self.res_range), len(self.gain_range)))
        bootstrap_samples = self.get_bootstrap_sample()

        for i in range(0, len(self.res_range)):
            res_current = self.res_range[i]
            for j in range(0, len(self.gain_range)):
                print(f'ITERATION RES n.{i+1} out of {len(self.res_range)} TOT')
                print(f'ITERATION GAIN n.{j+1} out of {len(self.gain_range)} TOT')

                gain_current = self.gain_range[j]

                # Graph creation
                graph_list = []
                for k in range(0, len(bootstrap_samples)):
                    graph = self.create_tda_graph(bootstrap_samples[k], gain_current, res_current)
                    graph_list.append(graph)
                
                if metric == 'netsimile':

                    # Graph distance 
                    dist_ = self.graph_distance_metric(graph_list)

                    # Save results
                    matrix[i,j] = dist_
                
                elif metric == 'clustering':

                    # Clustering metric
                    clustering_ = self.clustering_metric(graph_list)

                    # Save results
                    matrix[i,j] = clustering_

        return matrix