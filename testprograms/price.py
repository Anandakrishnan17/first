item = int(input("Enter the total items:"))
if item<=10:
    price=item*12
    print("Total items:",item)
    print("Price is:",price)
elif item<=99:
    price=item*10
    print("Total items:",item)
    print("Price is:",price)
elif item>=100:
    price=item*7
    print("Total items:",item)
    print("Price is:",price)