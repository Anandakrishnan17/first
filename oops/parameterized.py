class Student:
    def __init__(self,name,adress):
        self.name1=name
        self.address1=adress
    def open(self):
        print("hi",self.name1,"school is open") 

obj=Student("Anandakrishnan","alp")  
obj.open()   
obj.name1="ammu"     
obj.open() 
obj1=Student("achu","kozhikode")
obj1.open()