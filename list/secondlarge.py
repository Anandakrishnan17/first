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
print("Largest:",largest)  
i=0
while(1):
    if list1[i]!=largest:
        seclarge=list1[i]
        break
    i=i+1
for i in range(i+1,limit):
    if list1[i]<largest and list1[i]>seclarge:
        seclarge=list1[i]
print("Second largest:",seclarge)           

    
