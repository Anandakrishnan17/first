list1=[]
list2=[]
limit=int(input("Enter the limit:"))
for i in range(limit):
    elem=int(input("Enter the element:"))
    list1.append(elem)
index=int(input("Enter the index:"))    
for i in list1:
    if i not in list2:
        list2.append(i)
for i in list2:
    c=0
    for j in list1:
        if i==j:
            c+=1
    print(i,"in",c,"times")                    