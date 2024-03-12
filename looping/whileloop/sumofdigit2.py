num=555
sum=0
while num!=0:
    d=num%10
    sum=sum+d
    num//=10
while sum>10:
    newsum=0
    while sum>0:
        d=sum%10
        newsum=newsum+d
        sum//=10
    sum=newsum
print(sum)        
        


    
    
    





     
    
