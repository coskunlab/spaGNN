# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 10:28:48 2022

@author: zfang38
"""

import numpy as np
import pandas as pd
from sklearn.neighbors import NearestNeighbors
from numpy.random import shuffle
from joblib import Parallel, delayed

import sys

def find_neighborhoods(cluster_rna_df, n_neighbors, row_name, col_name):
    
    r = cluster_rna_df[row_name].tolist()
    c = cluster_rna_df[col_name].tolist()
    r_c = list(zip(r,c))
    
    if n_neighbors>len(r_c):
        return None
    
    neigh = NearestNeighbors(n_neighbors=n_neighbors)
    neigh.fit(r_c)
    dist, neighbors = neigh.kneighbors(r_c)
    return dist,neighbors

def count_neighbors(cluster_rna_df, neighbors, genes, markers_l):
    counts = np.zeros((cluster_rna_df.shape[0], len(markers_l)))
    for i in range(neighbors.shape[0]):
        for j in range(neighbors.shape[1]):
            neighbor = neighbors[i,j]
            idx = markers_l.index(genes[neighbor])
            counts[i,idx] = counts[i,idx] + 1
    df = pd.DataFrame(counts, columns=markers_l)
    return df

def proximity_network(cluster_rna_df, n_neighbors, row_name, col_name, marker_names):
    r = cluster_rna_df[row_name].tolist()
    c = cluster_rna_df[col_name].tolist()
    r_c = list(zip(r,c))
    
    if n_neighbors > len(r_c):
        return None
    
    neigh = NearestNeighbors(n_neighbors=n_neighbors)
    neigh.fit(r_c)
    dist, neighbors = neigh.kneighbors(r_c)
    
    genes = cluster_rna_df[marker_names].tolist()
    markers_l = list(np.unique(genes))
    df = count_neighbors(cluster_rna_df, neighbors, genes, markers_l)
    return df.corr(method='pearson')

def count_interactions(neighbor_counts_df, marker_names):
    # connectivity_counts = np.zeros(len(pairs))
    
    summed = neighbor_counts_df.groupby(marker_names).sum()
    return summed.values + summed.values.T

def permutation(cluster_rna_df, n_neighbors, row_name, col_name, marker_names, n_permutation):
    temp = find_neighborhoods(cluster_rna_df, n_neighbors, row_name, col_name)
    
    if temp is None:
        return None
    else:
        dist,neighbors = temp
    
    genes = cluster_rna_df[marker_names].tolist()
    markers_l = list(np.unique(genes))
    neighbor_counts_df = count_neighbors(cluster_rna_df, neighbors, genes, markers_l)
    neighbor_counts_df.insert(0,marker_names,cluster_rna_df[marker_names].tolist())
    
    interaction = count_interactions(neighbor_counts_df, marker_names)
    
    interaction_l = []

    for i in range(n_permutation):
        shuffle(genes)
        neighbor_counts_df = count_neighbors(cluster_rna_df, neighbors, genes, markers_l)
        neighbor_counts_df.insert(0,marker_names,genes)
        interaction_l.append(count_interactions(neighbor_counts_df,marker_names))
    
    (z_s, m, s) = permutation_z_score(interaction, interaction_l)
    
    z_df = pd.DataFrame(z_s, index=markers_l, columns=markers_l)
    z_df = z_df.fillna(0)
    return (z_df, m, s)

def permutation_z_score(interaction, interaction_l):
    arr = np.array(interaction_l)
    m = np.mean(arr, axis=0)
    s = np.std(arr, axis=0)
    with np.errstate(divide='ignore',invalid='ignore'):
        z = (interaction - m) / s
    return (z, m, s)
