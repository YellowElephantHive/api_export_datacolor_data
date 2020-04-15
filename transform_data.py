#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 09:37:56 2020

@author: laiyuchun
"""

import os
import sys
import pandas as pd
import numpy as np
from functools import reduce


df = pd.read_csv('/Users/laiyuchun/Desktop/all_20200302.csv', encoding='big5')
ColNames = df.columns
DataFrameWithoutNa = df.dropna()
DataFrameResetIndex = DataFrameWithoutNa.reset_index(drop=True)

NewCols = []
for i in range(1, 5):
    ColNames = ['染料_' + str(i), '濃度_' + str(i)]
    NewCols.append(ColNames)

NewCols = np.asarray(NewCols).reshape(8).tolist()

SplitSolubilityString = []
for i in range(len(DataFrameResetIndex['Drug Solubility'])):
    SplitSolubilityString.append(DataFrameResetIndex['Drug Solubility'][i].split(' '))
SpiteStringWithComma = []
for i in range(len(SplitSolubilityString)):
    FixLengthOfSolubility = []
    for j in range(len(SplitSolubilityString[i])):
        SpitedString = SplitSolubilityString[i][j].split(',')
        FixLengthOfSolubility.append(SpitedString)
    SpiteStringWithComma.append(FixLengthOfSolubility)

MergeSolubilityList = []
for i in range(len(SpiteStringWithComma)):
    MergeFragmentList = reduce(lambda list_1, list_2: list_1 + list_2, SpiteStringWithComma[i])
    ListWithoutNone = list(filter(None, MergeFragmentList))
    MergeSolubilityList.append(ListWithoutNone)

CleanOutput = []
LogAbnormalData = []
for i in MergeSolubilityList:
    if len(i) > 8:
        LogAbnormalData.append(i)

    else:
        CleanOutput.append(i)

'''
df_modify['abort'] = 0
df_modify['revised'] = 0
'''

TrainingData = pd.read_excel('/Users/laiyuchun/Desktop/hong_make_all_revised.xlsx', encoding='big5')

'''
this scope is to complement value because solubility requires
four kinds of dyestuff and concentration of four dyestuff. That
is to say there are totally eight columns. These columns would
be merged with NewCols to form a new dataframe
'''
ComplementaryValue = []
for i in CleanOutput:
    if len(i) < 6:
        i = i + [" ", " ", " ", " "]
        ComplementaryValue.append(i)
    else:
        i = i + [" ", " "]
        ComplementaryValue.append(i)
        

# 單色光: light 布號: Device
DfSolubility = pd.DataFrame(ComplementaryValue, columns=NewCols)
LightDeviceGroup = TrainingData.groupby(['單色光', '布號']).groups
DeviceToLight = dict((v, k) for k, v in LightDeviceGroup)
DataFrameResetIndex['布號'].map(DeviceToLight)
DataFrameResetIndex['單色光'] = DataFrameResetIndex['布號'].map(DeviceToLight)
DataFrameResetIndex.to_excel('/Users/laiyuchun/Desktop/df_modify_2.xlsx')

    
    
    



        
