#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
from numpy.random import randn
import pandas as pd
from pandas import Series, DataFrame 

import matplotlib.pyplot as plt
from matplotlib import rcParams


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')
rcParams['figure.figsize']=5,4


# In[3]:


x = range(1,10)
y= [1,2,3,4,0,4,3,2,1]

fig = plt.figure()
ax = fig.add_axes([.1,.1,1,1])
ax.plot(x,y)


# In[5]:


fig = plt.figure()
ax = fig.add_axes([.1,.1,1,1])

#setting the limits of our axes
ax.set_xlim([1,9])
ax.set_ylim([0,5])

#setting the markers of our ticks
ax.set_xticks([0,1,2,4,5,6,8,9,10])
ax.set_yticks([0,1,2,3,4,5])

ax.plot(x,y)


# In[7]:


fig = plt.figure()
ax = fig.add_axes([.1,.1,1,1])

#setting the limits of our axes
ax.set_xlim([1,9])
ax.set_ylim([0,5])

#adding a grid
ax.grid()

#actually plotting the graph 
ax.plot(x,y)


# In[8]:


fig = plt.figure()
fig, (ax1, ax2) = plt.subplots(1,2) 

ax1.plot(x)
ax2.plot(x,y)


# In[ ]:




