list1=[1,2,3,4,5,6,7,8,9,10]
lim=len(list1)
sublist=[]
limit=int(input("Enter the limit:"))
for i in range(limit):
    ele=int(input("Enter the element:"))
    sublist.append(ele)
for i in range(0,lim-limit+1):
    if list1[i:i+limit]==sublist:
        print("Yes exists")
        break
else:
    print("Not exists")