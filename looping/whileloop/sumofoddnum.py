n=329
sum=0
while n!=0:
    d=n%10
    if d%2==1:
        sum=sum+d
    n//=10    
print("Sum is",sum)        
    