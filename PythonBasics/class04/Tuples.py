thistuple = ("apple", "banana", "cherry")
print(thistuple)
print(thistuple[0])
print(len(thistuple))
print("*********************************************************")

tuple1 = ("apple", "banana", "cherry")  # string type of tuple
tuple2 = (1, 5, 7, 9, 3)  # int type of tuple
tuple3 = (True, False, False)  # bool type of tuple
print(tuple1)
print(tuple2)
print(tuple3)
print("*********************************************************")
print(tuple1[0:3])  # print tuple elements between index 0 and 2
print("*********************************************************")

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
print("*********************************************************")

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
print("*********************************************************")

thistuple1 = ("apple", "banana", "cherry")
for x in thistuple1:
    print(x)
print("*********************************************************")
