num=234
lrg=0
while num!=0:
    d=num%10
    if lrg<=d:
        lrg=d
    num//=10
print(lrg)    
    
