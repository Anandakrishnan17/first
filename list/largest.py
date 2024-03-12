list1=[]
largest=[]
limit=int(input("Enter the limit:"))
for i in range(0,limit):
    ele=int(input("Enter the element:"))
    list1.append(ele)
largest=list1[0]
for i in range(1,limit):
    if list1[i]>largest:
        largest=list1[i]    

print("Largest",largest)        
    
