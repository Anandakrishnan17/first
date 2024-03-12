num = int(input("Enter the number:"))
st = str(num)
bignum = 0
for i in st:
    inum=int(i)
    if inum>bignum:
        bignum=inum
print("Biggest number is:",bignum)
    