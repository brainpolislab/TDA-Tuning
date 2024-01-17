import numpy as np
import pandas as pd
import random

# Graph distance metrics
import netcomp as nc
from netrd.distance import NetSimile
import networkx as nx

def get_bootstrap_sample(data, n_bootstrap : int, sample_ratio = 0.7):
    """
    Generates a collection of bootstrap samples from a given dataset.

    Parameters:
    - data (pd.DataFrame): The input dataset.
    - n_bootstrap (int): The number of bootstrap samples to generate.
    - sample_ratio (float, optional): The ratio of samples to be drawn from the dataset for each bootstrap iteration. Defaults to 0.7.

    Returns:
    - List: A list containing numpy arrays representing the bootstrap samples.

    The function performs random sampling with replacement to create multiple bootstrap samples from the input dataset.
    For each bootstrap iteration, a subset of the dataset is selected, and the process is repeated 'n_bootstrap' times.
    The resulting list contains numpy arrays, each representing a bootstrap sample.

    Note:
    - The 'sample_ratio' parameter controls the proportion of data to be included in each bootstrap sample.
      It ranges from 0 to 1, where 1 corresponds to including the entire dataset in each sample.
    """
    data_index = data.index.tolist()
    dicts_index_bootstrap = {}
    list_bootstrap_data = []

    for i in range(n_bootstrap):
        y = random.sample(data_index, round(len(data_index)*sample_ratio))
        dicts_index_bootstrap[i] = y
        dicts_index_bootstrap_df = pd.DataFrame(dicts_index_bootstrap)

        current_index = dicts_index_bootstrap_df.iloc[:,i].to_list()
        all_data = data.iloc[current_index,:]
        list_bootstrap_data.append(all_data)

    X_arrays = [array.to_numpy() for array in list_bootstrap_data]
    return X_arrays

def graph_distance_metric(graph_list : list, metric : str):
    """
    Computes the average distance between graphs based on specified distance metrics.

    Parameters:
    - graph_list (list): A list of NetworkX graphs to compute distances between.
    - metric (str): The distance metric to use ('lambda' or 'netsimile').

    Returns:
    - float: The average distance between graphs based on the chosen metric.

    This function computes the average distance between graphs in the given list using either the 'lambda' or 'netsimile'
    metric. For the 'lambda' metric, it calculates the distance between each pair of graphs based on adjacency matrices,
    considering both jk and kj distances. For the 'netsimile' metric, it utilizes the NetSimile library to compute
    pairwise graph distances.

    Parameters:
    - graph_list (list): A list of NetworkX graphs to compute distances between.
    - metric (str): The distance metric to use ('lambda' or 'netsimile').

    Returns:
    - float: The average distance between graphs based on the chosen metric.

    Note:
    - Ensure that the necessary libraries, such as NetworkX and NetSimile, are installed before using this function.
    - The 'lambda' metric uses adjacency matrices and the NetSimile library is utilized for the 'netsimile' metric.
    - The function raises a ValueError if the 'metric' parameter is neither 'lambda' nor 'netsimile'.
    """
    lambda_distance = {}
    netsimile_distance = {}

    num_graphs = len(graph_list)

    # Compute the average distance for each metric                
    def compute_average_distance(distance_dict):
        dist_values = list(distance_dict.values())
        return sum(dist_values) / len(dist_values)

    # Compute Lambda metric
    if metric == 'lambda':
        for j in range(num_graphs):
            for k in range(j+1, num_graphs):
                A_j = nx.adjacency_matrix(graph_list[j])
                A_k = nx.adjacency_matrix(graph_list[k])

                # jk distance
                dist_key_jk = f'd{j+1}{k+1}'
                dist_jk_lambda = nc.lambda_dist(A_j, A_k, kind = 'adjacency', k = 10)

                # kj distance
                dist_key_kj = f'd{k+1}{j+1}'
                dist_kj_lambda = nc.lambda_dist(A_k, A_j, kind = 'adjacency', k = 10)

                if dist_jk_lambda == dist_kj_lambda:
                    lambda_distance[dist_key_jk] = dist_jk_lambda
                else:
                    lambda_distance[dist_key_jk] = dist_jk_lambda
                    lambda_distance[dist_key_kj] = dist_kj_lambda

                return compute_average_distance(lambda_distance) 
    
    # Compute NetSimile metric
    elif metric == 'netsimile':
        netsimile_test = NetSimile()
        for j in range(num_graphs):
            for k in range(j+1, num_graphs):

                # jk distance
                dist_key_jk = f'd{j+1}{k+1}'
                dist_jk_netsimile = netsimile_test.dist(graph_list[j], graph_list[k])

                # kj distance
                dist_key_kj = f'd{k+1}{j+1}'
                dist_kj_netsimile = netsimile_test.dist(graph_list[k], graph_list[j])

                if dist_jk_netsimile == dist_kj_netsimile:
                    netsimile_distance[dist_key_jk] = dist_jk_netsimile
                else:
                    netsimile_distance[dist_key_jk] = dist_jk_netsimile
                    netsimile_distance[dist_key_kj] = dist_kj_netsimile

                return compute_average_distance(netsimile_distance)
    else:
        raise ValueError('The metric parameter must be "lambda" or "netsimile"')
