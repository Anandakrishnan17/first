num = int(input("Enter the number:"))
divsum = 0
for i in range(1,num//2+1):
    if num%i==0:
     divsum+=i
if divsum==num:
   print("Perfect number")
else:
   print("not perfect")