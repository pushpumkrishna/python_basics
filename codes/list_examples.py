#!/usr/bin/env python
# coding: utf-8

# In[10]:


list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10" ]
list[6] = "Hello"                                               #type 1: to replace a item in a list
print(list)

list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10" ]
list[0:3] = ["Hey", "Dost", "Hey"]                              #type 2: to replace a series of elements in a list
print(list)

list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10" ]
list.append("11")                                               #type 3: to add a item in a list
list.append("12")
print(list)


list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10" ]
print(list + ["11", "12", "13"])                                #type 4: to add items in a list 

list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10" ]
list.remove("1")                                                #type 5: to remove a  SPECIFIED item in a list 
list.remove("2")
print(list)

list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10" ]
list.pop(2)                                                     #type 6: to remove a item at PARTICULAR PLACE in a list
print(list)

list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
list.pop()                                                      #type 7: to remove LAST item in a list


list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
print(f"No ouput see:: {list.clear()}")                         #type 7: to clear a list


list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
print(list.index("8"))                                          #type 7: to know the position of a item in a list


list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
print(list.count("8"))                                          #type 7: to count the occurence of a itme in a list

list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
list.sort()                                                     #type 7: to sort a list in ascending order
print(list)

list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
list.reverse()                                                  #type 7: to reverse a list in descending order
print(list)


list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
print(list)  


list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
print('2' in list)                                              # type :to check whether particular element is present or  not 
print('14' not in list)                                         # type :to check whether particular element is not present or  not

pow2 = [2 ** x for x in range(10)]
                                                                #type 7: to create a list of 2 ki power upto 10 places
# Output: [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
print(pow2)


pow2 = []
for x in range(10):                                             #type 7: to create a list of 2 ki power upto 10 places
   pow2.append(2 ** x)
print(pow2)


pow2 = [2 ** x for x in range(10) if x > 5]
odd = [x for x in range(20) if x % 2 == 1]
print(pow2)
print(odd)

[x+y for x in ['Python ', 'C'] for y in ['Language','Programming']]
# output : ['Python Language', 'Python Programming', 'C Language', 'C Programming']


for fruit in ['apple','banana','mango']:
    print("I like ",fruit)


# In[ ]:


Convert list into a string


 


# In[1]:


# Python program to convert a list 
# to string using list comprehension 
   
s = ['I', 'want', 4, 'apples', 'and', 18, 'bananas'] 
  
# using list comprehension 
listToStr = ' '.join([str(elem) for elem in s]) 
  
print(listToStr) 


# Python Program to Copy a String

# In[ ]:


str1 = input("Please Enter Your Own String : ")

str2 = str1
str3 = str1[:]

print("The Final String : Str2  = ", str2)
print("The Final String : Str3  = = ", str3)


# In[ ]:




