list1=[]
reverse=[]
limit=int(input("Enter the limit:"))
for i in range(limit):
    elem=int(input("Enter the numbers:"))
    list1.append(elem)
for i in list1:   
    reverse.insert(0,i)
print("Reverse:",reverse)    

