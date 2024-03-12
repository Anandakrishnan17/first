def prime(n):
    for i in range(2,n):
        if n%i==0:
            print("not prime")
            break
    else:
        print("Prime number")
num = int(input("Enter the number:"))
prime(num)            