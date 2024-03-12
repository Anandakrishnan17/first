class Student:
    def __init__(self,name,maths,science,english):
        self.name=name
        self.maths=maths
        self.science=science
        self.english=english
    def calculate_average(self):
        total_score=self.maths+self.english+self.science
        average_score=total_score/3
        return average_score
    def calculate_grade(self):
        average_score=self.calculate_average()
        if average_score >= 90:
            print("A")  
        elif 80 < average_score <90:
            print("B") 
        elif 70 < average_score <80:
            print("C") 
        elif 60 < average_score <70:
            print("D")
        else:
            print("Fail")   

std=Student("anandakrishnan",86,92,44) 
average_score=std.calculate_average()
print("Student:",std.name) 
print("Average score:",average_score)
std.calculate_grade()