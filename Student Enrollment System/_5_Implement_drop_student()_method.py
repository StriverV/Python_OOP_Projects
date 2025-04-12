"""
Add a method drop_student() in the Student class 
that changes is_enrolled to False 
to indicate the student has dropped out.
"""

class Student:

    def __init__(self,student_id, name, department, is_enrolled):
   
        self.student_id = student_id
        self.name = name
        self.department = department
        self.is_enrolled = is_enrolled

    def enroll_student(self):
        if not self.is_enrolled:     #if (self.is_enrolled == False):
            self.is_enrolled = True
            return f'-> {self.name} is now enrolled'
        else:
            return f'-> {self.name} is already enrolled'
            

    def drop_student(self):
        if self.is_enrolled:     #if (self.is_enrolled == True):
            self.is_enrolled = False
            return f'-> {self.name} has dropped out'
        else:
            return f'-> {self.name} has not dropped out'



    def __repr__(self):
        return f'{self.student_id}, {self.name}, {self.department}, {self.is_enrolled}'
    

student = Student(1, "Mr. abc", "CSE", True)
student2 = Student(10, "Mr. xyx", "EEE", False)

print(student.drop_student())  
print(student2.drop_student())
