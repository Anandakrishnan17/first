num = int(input("Enter the number:"))
for i in range(num,0,-1):
    for j in range(1,i+1):
        print(2*j,end=" ")
    print("")