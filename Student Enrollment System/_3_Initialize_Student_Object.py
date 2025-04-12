"""
In the constructor of the Student class,initialize the attributes.
Insert the Student object into student_list using
the method add_student(). This part will be done manually, i.e., 
no need for a menu option.
"""
    
class StudentDatabase:

    student_list = []   

    @classmethod
    def add_student(cls, student_id, name, department, is_enrolled):
        s = Student(student_id, name, department, is_enrolled)
        cls.student_list.append(s)


class Student:

    def __init__(self,student_id, name, department, is_enrolled):
   
        self.student_id = student_id
        self.name = name
        self.department = department
        self.is_enrolled = is_enrolled

    def __repr__(self):
        return f'{self.student_id}, {self.name}, {self.department}, {self.is_enrolled}'
    


StudentDatabase.add_student(1, "Mr. abc", "CSE", True)
StudentDatabase.add_student(2, "Mr. xyz", "CSE", True)
 
print(StudentDatabase.student_list)


