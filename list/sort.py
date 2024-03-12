a = []
limit=int(input("enter the limit : "))
for i in range(limit):
    ele=int(input("enter the elements : "))
    a.append(ele)
temp = 0
for i in range(0, len(a)):
    for j in range(i+1, len(a)):
        if a[i] > a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
print("Sorted list:", a)
