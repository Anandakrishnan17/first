list1=[]
reverse=[]
limit=int(input("Enter the limit:"))
for i in range(limit):
    elem=int(input("Enter the number:"))
    list1.append(elem)
for i in list1:   
    reverse.insert(0,i)
    if list1==reverse:
        print("Palindrome")
        break
else:
    print("Not palindrome")    

    
