# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 13:52:46 2021

@author: dav
"""


import numpy as np 
import pandas as pd 

from pandas import Series, DataFrame 

Df_obj = DataFrame(np.arange(36).reshape(6,6))
print(Df_obj)

Df_obj_2 = pd.DataFrame(np.arange(15).reshape(5,3))
print(Df_obj_2)

print(pd.concat([Df_obj, Df_obj_2], axis=1))
print(pd.concat([Df_obj, Df_obj_2]))
      

print(Df_obj.drop([0,2]))
print(Df_obj.drop([0,2], axis=1))

#adding data

series_obj = Series(np.arange(6))
series_obj.name = 'added_variable'
print(series_obj)

variable_added_DF = DataFrame.join(Df_obj, series_obj)
print(variable_added_DF)

added_datatable = variable_added_DF.append(variable_added_DF, ignore_index=True)
print(added_datatable)

#sorting data 
Df_sorted = Df_obj.sort_values(by=(5), ascending=[False])
print(Df_sorted)