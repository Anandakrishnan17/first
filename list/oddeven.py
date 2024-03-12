list1=[]
listeven=[]
listodd=[]
limit=int(input("Enter the limit:"))
for i in range(limit):
    ele=int(input("Enter the element:"))
    list1.append(ele)
    if ele%2==0:
        listeven.append(ele)
    else:
        listodd.append(ele)
print("List is",list1)         
print("Even:",listeven)  
print("Odd:",listodd)         
