"""
Define a class named StudentDatabase 
with one class attribute named student_list. 
Initially, it should be an empty list. 
Create a class method add_student() to insert an object
 of the Student class into student_list.
"""

class StudentDatabase:

    student_list = []   

    @classmethod
    def add_student(cls, student_id, name, department, is_enrolled):
        s = Student(student_id, name, department, is_enrolled)
        cls.student_list.append(s)

