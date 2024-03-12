num = int(input("Enter the number:"))
for i in range(num,0,-1):
    inum=2*num
    for j in range(num-i+1):
        print(inum,end=" ")
        inum-=2
    print("")