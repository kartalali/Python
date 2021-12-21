def greet(first_name, last_name):
    print(f"Hello {first_name} {last_name}")
    print("Welcome on board")


greet("Ali", "Kartal")


# we have 2 type of functions in python
# 1-Perform a task
# 2-return a value

def greet(name):
    print(f"Hi {name}")


def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("Ali")  # we create a file extension with .txt and print in it "Hi Ali" message
file = open("content.txt", "w")
file.write(message)

print(message)  # just write a message
