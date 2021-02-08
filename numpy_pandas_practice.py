# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 00:41:28 2021

@author: dav
"""

import numpy as np 
import pandas as pd 

from pandas import Series, DataFrame

series_obj = Series(np.arange(8), index=['row 1', 'row 2', 'row 3','row 4', 'row 5', 'row 6','row 7', 'row 8'])
#print(series_obj)

np.random.seed(25)
Df_obj = DataFrame(np.random.rand(36).reshape((6,6)),
                   index=['row 1', 'row 2', 'row 3','row 4', 'row 5', 'row 6'],
                   columns=['column 1', 'column 2','column 3', 'column 4', 'column 5', 'column 6'])
print(Df_obj)
#print(Df_obj.loc[['row 2', 'row 5'], ['column 2', 'column 5']])
print(series_obj['row 3': 'row 7'])

print(Df_obj < .2)

print(series_obj[series_obj > 6])

series_obj['row 1', 'row 5', 'row 8']= 13
print(series_obj)