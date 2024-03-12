def palindrome(number):
    n=number
    temp=str(number)
    rev=0
    l=len(temp)
    for i in range(l-1,-1,-1):
       d=int(temp[i])
       rev=(rev*10)+d
    if rev==n:
       print("Palindrome")
    else:
       print("Not palindrome") 
num=int(input("Enter a number:")) 
palindrome(num)     