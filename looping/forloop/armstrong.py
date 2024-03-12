num=int(input("Enter a number:"))
number=num
st=str(num)
l=len(st)
sum=0
for i in range(l):
    d=int(st[i])
    sum=sum+d**l
if number==sum:
    print("Armstrong")
else:
    print("Not Armstrong")

