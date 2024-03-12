bs=int(input("Enter basic salary:"))
if bs>10000:
    hra=bs*2/100
    pf=bs*3/100
    da=bs*5/100
    ns=bs+hra+da-pf
else:
    hra=bs*5/100
    pf=bs*7/100
    da=bs*9/100
    ns=bs+hra+da-pf
print("Net salary",ns)    

