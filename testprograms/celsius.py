temp=float(input("Enter the temperature in celsius:"))
if temp< -273.5:
    print("Temparature is invalid!")
elif temp==-273.5:
    print("Temparature is absolute zero")
elif temp>-273.5 and temp<0:
    print("Temperature is below freezing")
elif temp==0:
    print("Temparature is at freezing point")
elif temp>0 and temp<100:
    print("Temperature is in the normal range")   
elif temp==100:
    print("Temperature is at boiling point")
elif temp>100:
    print("Temparature is above the boiling point!")
else:
    print("Invalid entry")                        