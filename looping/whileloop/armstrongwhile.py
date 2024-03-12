num=input("Enter a number:")
l=len(num)
n=int(num)
number=n
s=0
while n!=0:
    d=n%10
    s=s+d**l
    n//=10
if  number==s:
    print("Armstrong")
else:
    print("Not armstrong")      