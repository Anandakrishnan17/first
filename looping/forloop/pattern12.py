n = 6
for i in range(n,0,-1):
    for j in range(n,i-1,-1):
        print(j,end=" ")
    print("")

for i in range(n-1,0,-1):
    for j in range(n,n-i,-1):
        print(j,end=" ")
    print("")