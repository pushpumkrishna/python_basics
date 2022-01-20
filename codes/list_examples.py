#!/usr/bin/env python
# coding: utf-8

list1 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

list1[0:3] = ["Hey", "Dost", "Hey"]  # type 2: to replace a series of elements in a list1
print(list1)

# type 3: to add a item in a list1
list1.append("11")
list1.append("12")
print(list1)

# type 4: to add items in a list1
print(list1 + ["11", "12", "13"])

# type 5: to remove a  SPECIFIED item in a list1
list1.remove("1")
list1.remove("2")
print(list1)

# type 6: to remove a item at PARTICULAR PLACE in a list1
list1.pop(2)
print(list1)

# type 7: to remove LAST item in a list1
list1.pop()

# type 7: to clear a list1
print(f"No output see:: {list1.clear()}")

# type 7: to know the position of a item in a list1
print(list1.index("8"))

# type 7: to count the occurence of a itme in a list1
print(list1.count("8"))

# type 7: to sort a list1 in ascending order
list1.sort()
print(list1)

# type 7: to reverse a list1 in descending order
list1.reverse()
print(list1)


print('2' in list1)  # type :to check whether particular element is present or  not
print('14' not in list1)  # type :to check whether particular element is not present or  not

# type 7: to create a list1 of 2 ki power upto 10 places
pow2 = [2 ** x for x in range(10)]
print(pow2)
# Output: [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

pow2 = [2 ** x for x in range(10) if x > 5]
odd = [x for x in range(20) if x % 2 == 1]
print(pow2)
print(odd)

output = [x + y for x in ['Python ', 'C'] for y in ['Language', 'Programming']]
print(output)
# output : ['Python Language', 'Python Programming', 'C Language', 'C Programming']

# Python program to convert a list1 to string using list1 comprehension
s = ['I', 'want', 4, 'apples', 'and', 18, 'bananas']
listToStr = ' '.join([str(elem) for elem in s])
print(listToStr)

# Python Program to Copy a String
str1 = input("Please Enter Your Own String : ")
str2 = str1
str3 = str1[:]
print("The Final String : Str2  = ", str2)
print("The Final String : Str3  = = ", str3)
