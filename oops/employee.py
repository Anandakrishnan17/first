class Employee:
    def __init__(self,name,code,basicsalary):
        self.name=name
        self.code=code
        self.basicsalary=basicsalary
    def calculate(self):
        da=0.10*self.basicsalary
        hra=0.15*self.basicsalary
        pf=0.03*self.basicsalary 
        ns=self.basicsalary+hra+da-pf
        print("Name         :",self.name)
        print("Empcode      :",self.code)
        print("Basic salary :",self.basicsalary)
        print("DA           :",da)
        print("HRA          :",hra)
        print("PF           :",pf)
        print("Net salary   :",ns) 
        
emp1name=input("Enter the name of first employee  :")
emp1code=int(input("Enter the code of first employee  :"))
emp1bs=int(input("Enter the basic salary of first employee  :")) 
emp2name=input("Enter the name of second employee  :")
emp2code=int(input("Enter the code of second employee  :"))
emp2bs=int(input("Enter the basic salary of second employee  :"))

obj1=Employee(emp1name,emp1code,emp1bs)
obj2=Employee(emp2name,emp2code,emp2bs)
obj1.calculate()
print("---------------------------")
obj2.calculate()


      
