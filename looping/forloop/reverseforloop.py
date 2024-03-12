num=int(input("Enter a number:"))
temp=str(num)
rev=0
l=len(temp)
for i in range(l-1,-1,-1):
    d=int(temp[i])
    rev=(rev*10)+d
print(rev)    

