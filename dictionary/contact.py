cont={}
while True:
  print("1.Add contact")
  print("2.Delete a contact")
  print("3.Edit a contact")
  print("4.Search contact")
  print("5.List all contacts")
  print("6.Exit")

  choice = int(input("Enter the choice:"))
  if choice==1:
    name = input("Enter your name:")
    number = int(input("Enter your number:"))
    cont[name]=number
    print("Contact added succesfully")
  elif choice==2:
    if cont:
        name = input("Enter the name to be delete:")
        if name in cont:
            del cont[name]
            print("Contact deleted succesfully")
        else:
            print("Not found")
  elif choice==3:
    if cont:
        name = input("Enter the name for edit:")
        if name in cont:
            newnum = int(input("Enter new number:"))
            cont[name]=newnum
            print("Edited succesfully")
        else:
            print("Failed")
  elif choice==4:
    if cont:
        sname = input("Enter the name for searching:")
        if sname in cont:
            print("Contact found {cont[sname]}")
        else:
            print("Not found")
  elif choice==5:
     print(cont)
  elif choice==6:
     print("Exiting")
     break
  else:
     print("Error,Please enter correctly")