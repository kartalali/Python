def multiply(x, y):
    return x * y


print(multiply(2, 3))  # same result

result = multiply(4, 5)  # same result
print(result)


def multiply(*numbers):
    total = 1
    for number in (numbers):
        total *= number
    return total


print(multiply(2, 3, 4, 5))


def save_user(**user):
    # print(user)
    print(user ["name"])
    print(user["mail"])
    print(user["age"])

save_user(name="Ali", age=34, mail="kartalalii@gmail.com", id=4616)
