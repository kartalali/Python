count = 0
for i in range(1, 10):  # even numbers
    if i % 2 == 0:
        count += 1
        print(i)
print(f"We have {count} even numbers from 1 to 10")

count = 0
for j in range(1, 10):  # odd numbers
    if j % 2 != 0:
        count += 1
        print(j)
print(f"We have {count} odd numbers from 1 to 10")
