def sum1(a):
    sum=0
    while a!=0:
        d=a%10
        sum=sum+d
        a//=10
    print(sum)
num=int(input("Enter the number:"))
sum1(num)