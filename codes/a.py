"""
Program to add all the numbers in the list using function
"""


def sum_list(num):
    """
    Function to print all the numbers in the list
    """
    value = 0
    for i in num:
        value = value + i
    return value


# Uncomment to run
# add = [24, 23, 21, 20, 22]
# print(f'Sum of list given is::', sum_list(add))
