class Employee:
    def __init__(self,name,code,bs):
        self.name=name
        self.code=code
        self.bs=bs
    def calculate(self):
        if self.bs < 10000:
            self.da=0.2*self.bs
            self.hra=0.25*self.bs
            self.pf=0.05*self.bs 
        else:
            self.da=0.1*self.bs
            self.hra=0.15*self.bs
            self.pf=0.03*self.bs 
        self.ns=self.bs+self.hra+self.da-self.pf       
    def display(self):
        print("Name         :",self.name)
        print("Empcode      :",self.code)
        print("Basic salary :",self.bs)
        print("DA           :",self.da)
        print("HRA          :",self.hra)
        print("PF           :",self.pf)
        print("Net salary   :",self.ns)  

class Teacher(Employee):
    def __init__(self, name, code, bs,dept):
        super().__init__(name, code, bs)
        self.department=dept
        self.student=[]
    def mark_attendance(self, n):
      self.count = n
      print("Enter the attendance roll number wise (1-present/0-absent)")
      for i in range(0, n):
        att = int(input())
        self.student.append(att)
      self.calculate()
    def display_attendance(self):
        print("List of present students")   
        for i in range(0,self.count):
            if self.student[i]==1:
                i+=1
                print("      ",i)
        print("List of absent students") 
        for i in range(0,self.count):
            if self.student[i]==0:
                print(i+1)          

    def display(self):
        print("Name         :",self.name)
        print("Empcode      :",self.code)
        print("Department    :",self.department)
        print("Basic salary :",self.bs)
        print("DA           :",self.da)
        print("HRA          :",self.hra)
        print("PF           :",self.pf)
        print("Net salary   :",self.ns) 
teacher_list=[]
m=int(input("Enter the number of teachers:"))  
for i in range(0,m):
    name=input("Enter the name of the teacher:")
    code=int(input("Enter the code:"))
    basicsalary=int(input("Enter the basic salary:"))
    department=input("Enter the department:")
    no_std=int(input("Enter the number of students:"))
    tec=Teacher(name,code,basicsalary,department)
    tec.mark_attendance(no_std)
    tec.calculate()
    teacher_list.append(tec)
for i in range(0,m):
    print("-----------------------------------")
    teacher_list[i].display()
    teacher_list[i].display_attendance()
