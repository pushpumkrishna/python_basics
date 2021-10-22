#!/usr/bin/env python
# coding: utf-8

# In[8]:


def z_value(x, mu, SEM):
    z = (x -mu) / SEM
    if z < 0:
        alpha = stats.norm.cdf(z)
    else:
        alpha = 1 - stats.norm.cdf(z)
    print(alpha)
    
x = 48.5
mu = 50
SEM = 0.79

z_value(x, mu, SEM)


# In[10]:


x = 51.5
mu = 50
SEM = 0.79
z_value(x, mu, SEM)


# In[17]:


import pandas as pd
import numpy as np
import math
from scipy import stats

def z_and_p(x1, x2, sigma1, sigma2, n1, n2):
    z = (x1-x2) / math.sqrt(((sigma1)**2)/n1 + ((sigma2)**2)/n2)    
    if z < 0:
        p = stats.norm.cdf(z)
    else:
        p = 1 - stats.norm.cdf(z)
    print(z,p)
    
z_and_p(121,112,8,8,10,10)
        
    


# In[19]:


#Calculating t value

stats.t.ppf(0.025, 13)


# In[21]:


metro = [3,7,25,10,15,6,12,25,15,7]
rural = [48,44,40,38,33,21,20,12,1,18]

stats.ttest_ind(metro,rural, equal_var = False)


# In[22]:





# In[ ]:




