def perfect(n):
   divsum = 0
   for i in range(1,n//2+1):
     if n%i==0:
      divsum+=i
   if divsum==n:
      print("Perfect number")
   else:
      print("not perfect")
num = int(input("Enter the number:"))   
perfect(num)