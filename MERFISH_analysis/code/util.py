# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 10:04:33 2022

@author: zfang38
"""

import numpy as np
import pandas as pd

def gene_count_df(df, gene_name):
    genes = np.unique(df[gene_name].tolist())
    counts = {}
    groups = df.groupby(gene_name)
    for gene in genes:
        counts[gene] = [groups.get_group(gene).shape[0]]
    return pd.DataFrame(counts)

def counting(df, count_by, gene_name):
    counts_l = []
    groups = df.groupby(count_by)
    for item in np.unique(df[count_by].tolist()):
        group_counts = gene_count_df(groups.get_group(item), gene_name)
        counts_l.append(group_counts)
    exp = pd.concat(counts_l, axis=0, join="outer", ignore_index=True)
    exp = exp.fillna(0)
    return exp

colors = colors = ['#ffffff','#c34fff','#01a5ca','#ec9d00',
          '#ff7598','#edb7ff','#fff585','#92b853',
          '#abd4ff','#ff5401','#edb7ff','#8a6800',
          '#92b853','#e700b9'
         ]

def get_complementary_colors(color = colors):
    comps = []
    for c in color:
        c = c[1:]
        c = int(c, 16)
        comp_color = 0xFFFFFF ^ c
        comp_color = '#%06X' % comp_color
        comps.append(comp_color)
    return comps
