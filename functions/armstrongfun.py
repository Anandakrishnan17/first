def armstrong(n):
    number=n
    st=str(n)
    l=len(st)
    sum=0
    for i in range(l):
       d=int(st[i])
       sum=sum+d**l
    if number==sum:
       print("Armstrong")
    else:
       print("Not Armstrong")
num=int(input("Enter a number:"))   
armstrong(num) 
