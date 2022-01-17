"""
Sets are used to store multiple items in a single variable.
Set is one of 4 built-in data types in Python used to store collections of data,
the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
A set is a collection which is unordered, unchangeable*, and unindexed.
"""
thisset = {"apple", "banana", "cherry"}
print(thisset)
print("******************************")

#Duplicate values will be ignored:
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
print("******************************")

#Get the number of items in a set:
thisset = {"apple", "banana", "cherry"}
print(len(thisset))
print("******************************")

#A set can contain different data types:
set1 = {"abc", 34, True, 40, "male"}
print(set1)
print("******************************")