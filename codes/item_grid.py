#!/usr/bin/env python
# coding: utf-8

# In[2]:


row = 4
column = 3
string = "| aaa | aaa | aaa |"

print("-" * 20)
def f(row, column, string):
    for i in range( 1, row + 1):
        for i in range(1, column + 1):
            if (i == 0 or i == 5):
                print(" ", end =" ")
            else:
                print("| aaa | aaa | aaa |")
                if i == 3 or i == 6 or i == 10:
                    print("-" * 20)
            
f(row, column, string)


# In[ ]:




