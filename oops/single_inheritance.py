class School:
    def open(self):
        print("Opening date 12/2/2024")

class Student(School):
    def hai(self):
        print("Hai")

obj=Student()
obj.open()
obj.hai()