credit = int(input("Enter the credits you have:"))
if credit<=23:
    print("credit is",credit)
    print("You are a Fresher")
elif credit<=53:
    print("credit is",credit)
    print("You are Sophomore")
elif credit<=83:
    print("credit is",credit)
    print("You are Junior")
elif credit>83:
    print("credit is",credit)
    print("You are Senior")