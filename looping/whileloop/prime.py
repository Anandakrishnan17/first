num=int(input("Enter a number:"))
i=2
while i<num:
    if num%i==0:
        print("Not prime")
        break
    i=i+1
else:
    print("prime")    
