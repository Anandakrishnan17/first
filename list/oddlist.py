list1=[]
list2=[]
limit=int(input("Enter a limit:"))
for i in range(limit):
    elem=int(input("Enter the element:"))
    list1.append(elem)
lim=int(input("Enter the limit2:"))
for i in range(lim):
    ele=int(input("Enter the element:"))
    list2.append(ele)  
list1.extend(list2)
list2.clear()
for i in list1:
    if i%2==0:
        list1.append(i)
    else:
        list2.append(i)
        list1.remove(i)
print("Even list:",list1)
print("Odd list:",list2)

