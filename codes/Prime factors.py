#!/usr/bin/env python
# coding: utf-8

# In[14]:


num = 15015
list_1 = []


for i in range(2, num + 1):
    if (num % i == 0):
        for j in range(2, i):
            if (i % j == 0):
                break
        else:
            list_1 = list_1 + [i]


# In[ ]:




