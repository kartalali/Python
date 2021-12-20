weight = int(input("Weight: "))
prefer = input("(K)gs or (L)bs: " )
if prefer.upper() == "L":
    print("Weight in Kgs: " + str(weight*0.45))
else:
    print("Weight in Lbs: " + str(weight/0.45))
