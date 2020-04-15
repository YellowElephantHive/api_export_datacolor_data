#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 09:37:56 2020

@author: laiyuchun
"""

import pandas as pd
import numpy as np
from functools import reduce


df = pd.read_csv('/Users/laiyuchun/Desktop/all_20200302.csv', encoding='big5')

col_names = df.columns
df_modify = df.dropna()
df_modify = df_modify.reset_index(drop=True)
df_modify = df_modify.drop(index=[17, 27])
df_modify = df_modify.reset_index(drop=True)

new_col = []
for i in range(1, 5):
    col_name = ['染料_' + str(i), '濃度_' + str(i)]
    new_col.append(col_name)
    
new_col = np.asarray(new_col).reshape(8).tolist()


solubility = []
for i in range(len(df_modify['Drug Solubility'])):
    solubility.append(df_modify['Drug Solubility'][i].split(' '))
pre_solubility = []
for i in range(len(solubility)):
    gg = []
    for j in range(len(solubility[i])):
        s = solubility[i][j].split(',')
        gg.append(s)
    pre_solubility.append(gg)


conn_pre_solubility = []
for i in range(len(pre_solubility)):
    conn = reduce(lambda a, b: a + b, pre_solubility[i])
    conn = list(filter(None, conn))
    conn_pre_solubility.append(conn)
    
df_modify['abort'] = 0
df_modify['revised'] = 0

df_hong = pd.read_excel('/Users/laiyuchun/Desktop/hong_make_all_revised.xlsx', encoding='big5')

final = []
for i in conn_pre_solubility:
    if len(i) < 6:
        i = i + [" ", " ", " ", " "]
        final.append(i)
    else:
        i = i + [" ", " "]
        final.append(i)
        

conc = pd.DataFrame(final, columns=new_col)
c = df_hong.groupby(['單色光', '布號']).groups
light_map = dict((v, k) for k, v in c)
df_modify['布號'].map(light_map)
df_modify['單色光'] = df_modify['布號'].map(light_map)
df_modify.to_excel('/Users/laiyuchun/Desktop/df_modify.xlsx')
    
    
    



        
