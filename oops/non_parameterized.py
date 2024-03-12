class Employee:
    def __init__(self):
        self.id=123
        self.name="Anandakrishnan"
    def display(self):
        print("hi",self.name)   

obj=Employee()
print(obj.id)         
obj.display()