num=int(input("Enter a number:"))
number=num
rev=0
while num!=0:
    d=num%10
    rev=(rev*10)+d
    num//=10
if rev==number:
    print("Palindrome")
else:
    print("Not palindrome")    


