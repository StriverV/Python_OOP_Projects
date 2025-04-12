"""
Define a class Student with the following instance attributes:
- student_id: Unique identifier for the student.
- name: Full name of the student.
- department: The department of the student.
- is_enrolled: A boolean indicating if the student is currentlyenrolled.
"""

class Student:

    def __init__(self,student_id, name, department, is_enrolled):
   
        self.student_id = student_id
        self.name = name
        self.department = department
        self.is_enrolled = is_enrolled
 

    