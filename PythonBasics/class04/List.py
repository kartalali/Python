fruits = ["apple", "banana", "cherry"]
print(fruits)
print("***************")

fruits.append("orange")  # Adds an element at the end of the list
print(fruits)
print("***************")

fruits = ['apple', 'banana', 'cherry']
fruits.clear()  # Removes all the elements from the list
print(fruits)
print("***************")

fruits.insert(0, "Apple")  # inserts specific index specificic element
fruits.insert(1, "banana")
fruits.insert(2, "cherry")
print(fruits)
print("***************")

fruits.reverse()  # reverse the elements of list
print(fruits)
print("***************")

fruits.sort()  # sorts elements of list
print(fruits)
print("***************")

print(fruits[-1])  # we can use negative index in python --->output will be cherry
