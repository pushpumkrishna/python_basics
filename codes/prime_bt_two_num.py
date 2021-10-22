#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("<<<< Program to print Prime Numbers in given range >>>> ")

#start of program

number_1 = int(input("Enter the first number:: "))
number_2 = int(input("Enter the second number:: "))

#message to print before the list
print("Prime Numbers in given range are :: ")

#for loop execution
for num in range(number_1, number_2 + 1):
    for i in range(2, num):
        if num % i ==0:
            break
    else:
        print(num)


# In[ ]:





# In[ ]:




