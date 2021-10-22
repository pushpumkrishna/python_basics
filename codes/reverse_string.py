#!/usr/bin/env python
# coding: utf-8

# In[8]:


def reverse(line): 
        """
        Function to reverse a string
        """
        words = line.split()
        words = list(reversed(words))
        output = (" ".join(words))
        return(output)

string = input("Enter the string :: ")
print(f"Output string: ", reverse(string))


# In[ ]:




