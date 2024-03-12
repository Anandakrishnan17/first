num=int(input("Enter a number:"))
n=num
sum=0
while num!=0:
    d=num%10
    fact=1
    while d>1:
        fact=fact*d
        d+=1
    sum=sum+fact
    n//=10
if sum==n:
    print("Strong number")   
else:
    print("Not strong number")     