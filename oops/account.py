class Account:
    def __init__(self,acc_holder,acc_number):
        self.account_holder=acc_holder
        self.account_number=acc_number
        self.amount=0
    def deposite_money(self):
        amount=int(input("Enter the amount to deposit:"))
        self.amount=self.amount+amount
        print("Deposited successfully")
    def withdraw_money(self):
        withdraw=int(input("Enter the amount to withdraw:")) 
        if withdraw > self.amount:
            print("Not enough balance") 
        else:    
            print("Amount withdrawed")
            balance=self.amount-withdraw
            self.amount=balance
    def view_balance(self):
        print("Balance is:",self.amount)   

name=input("Enter the account holder name:")
number=int(input("Enter the account number:"))
obj=Account(name,number)
while True:
    print("1.Deposit money")
    print("2.Withdraw money")
    print("3.View balance")
    print("4.Exit")
    choice=int(input("Enter the choice:"))
    if choice==1:
        obj.deposite_money()
    elif choice==2:
        obj.withdraw_money()  
    elif choice==3:
        obj.view_balance() 
    elif choice==4:
        print("Exiting!!")
        break         
    else:
        print("Invalid input")