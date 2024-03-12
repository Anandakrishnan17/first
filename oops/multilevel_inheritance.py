class School:
    def open(self):
        print("Opening date 12/2/2024")

class Student(School):
    def hai(self):
        print("Hai")

class All(Student):
    def hello(self):
        print("Hello")

obj=All()
obj.open()
obj.hai()
obj.hello()