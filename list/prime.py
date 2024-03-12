l1 = []
p = []
limit=int(input("enter the limit : "))
for i in range(limit):
    ele=int(input("enter the elements : "))
    l1.append(ele)
for num in l1:
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            p.append(num)

print("Prime numbers in the list are:", p)