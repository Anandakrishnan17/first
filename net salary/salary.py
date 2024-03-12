ctc=int(input("Cost to company[CTC]: "))
bs=ctc*50/100
hra=bs*20/100
da=bs*50/100
pf=bs*12/100+da
gs=bs+hra+da-pf

print("Basic salary:",bs)
print("HRA:",hra)
print("DA:",da)
print("PF:",pf)
print("Gross salary:",gs)