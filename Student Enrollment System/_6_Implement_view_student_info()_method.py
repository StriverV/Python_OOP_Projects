"""
Add a method view_student_info() in the Student class
to display the details of the student including 
student_id, name, department, and enrollment status.
"""


class Student:

    def __init__(self,student_id, name, department, is_enrolled):
   
        self.student_id = student_id
        self.name = name
        self.department = department
        self.is_enrolled = is_enrolled

    def enroll_student(self):
        if not self.is_enrolled:     
            self.is_enrolled = True
            return f'-> {self.name} is now enrolled'
        else:
            return f'-> {self.name} is already enrolled'
            

    def drop_student(self):
        if self.is_enrolled:    
            self.is_enrolled = False
            return f'-> {self.name} has dropped out'
        else:
            return f'-> {self.name} has not dropped out'


    def __repr__(self):
        return f'{self.student_id}, {self.name}, {self.department}, {self.is_enrolled}'
    

    def view_student_info(self):
        student_info = f'------ ID:{self.student_id}, Name:{self.name}, dept:{self.department}, Enrollment status:{self.is_enrolled} ------'
        return student_info


student = Student(1, "Mr. abc", "CSE", True)
student2 = Student(10, "Mr. xyx", "EEE", False)

print(student.view_student_info())  
print(student2.view_student_info())
