"""
Add a method enroll_student() in the Student class 
that checks if the student is not already enrolled. 
If not, change is_enrolled to True.

"""

class Student:

    def __init__(self,student_id, name, department, is_enrolled):
   
        self.student_id = student_id
        self.name = name
        self.department = department
        self.is_enrolled = is_enrolled

    def enroll_student(self):
        if not self.is_enrolled:     #if (self.is_enrolled != True):
            self.is_enrolled = True
            return f'->{self.name} is now enrolled'
        else:
            return f'->{self.name} is already enrolled'
        

    def __repr__(self):
        return f'{self.student_id}, {self.name}, {self.department}, {self.is_enrolled}'
    

student = Student(1, "Mr. abc", "CSE", True)
student2 = Student(10, "Mr. xyx", "EEE", False)

print(student.enroll_student())  
print(student2.enroll_student())
