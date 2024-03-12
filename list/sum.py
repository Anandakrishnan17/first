list1 = []
list2 = []
sumlist = []
limit = int(input("Enter the limit:"))
for i in range(0,limit):
    elem=int(input("Enter the numbers:"))
    list1.append(elem)
    elem1=int(input("Enter the numbers"))
    list2.append(elem1)
print("First list:",list1)
print("Second list:",list2)
for i in range(0,limit):
    sumlist.append(list1[i]+list2[i])
print("sum:",sumlist)