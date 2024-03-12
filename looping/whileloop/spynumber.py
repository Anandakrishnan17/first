num=input("Enter a number:")
l=len(num)
n=int(num)
s=0
p=1
while n!=0:
    d=n%10
    s=s+d
    p=p*d
    n//=10
if p==s:
    print("Spy")    
else:
    print("Not spy")    