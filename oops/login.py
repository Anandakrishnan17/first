class User:
    def __init__(self,password):
        self.pass1=password
    def login(self):
        ps=input("Enter the password:")
        if self.pass1==ps:
            print("Login succesful")
        else:
            print("Invalid password")
    def resetpassword(self):
        newpass=input("Enter new password:")
        self.pass1=newpass
        print("Password reset successfully") 
                           
password1=input("Enter the password:")
obj=User(password1)
while True:
  print("1.Login")
  print("2.Reset password")
  print("3.Exit")
  choice=int(input("Enter your choice:"))
  if choice==1:
    obj.login()
  elif choice==2:
    obj.resetpassword()
  elif choice==3:
    print("Exiting..")
    break
  else:
     print("Invalid entry")        