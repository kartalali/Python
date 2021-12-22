age = 22
if age >= 18:
    print("Eligible")
else:
    print("Not eligible")

message = "Eligible" if age >= 18 else "Not eligible"  # same result
print(message)

if 10 == "10":
    print("a")
elif "bag" > "apple" and "bag" > "cat":
    print("b")
else:
    print("c")
