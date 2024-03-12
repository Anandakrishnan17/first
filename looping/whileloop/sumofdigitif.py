n=98
sum=0
while n!=0:
    d=n%10
    sum=sum+d
    n//=10
    if n==0 and sum>9:
        n=sum
        sum=0
print("Sum is:",sum)    
