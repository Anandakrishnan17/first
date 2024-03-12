list1=[]
list2=[]
limit=int(input("Enter the limit:"))
for i in range(limit):
    elem=int(input("Enter the element:"))
    list1.append(elem)
for i in list1:
    if i not in list2:
        list2.append(i)
print("Old list:",list1)  
print("New list:",list2)      
