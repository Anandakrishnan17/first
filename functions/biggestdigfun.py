def biggest(n):
    st = str(n)
    bignum = 0
    for i in st:
        inum=int(i)
        if inum>bignum:
            bignum=inum
    print("Biggest number is:",bignum)
num = int(input("Enter the number:"))
biggest(num)