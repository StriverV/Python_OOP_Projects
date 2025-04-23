class StudentDatabase:

    student_list = []    

    @classmethod
    def add_student(cls, student_id, name, department, is_enrolled):
        s = Student(student_id, name, department, is_enrolled)
        cls.student_list.append(s)

    
class Student:

    def __init__(self,student_id, name, department, is_enrolled):
   
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = is_enrolled

    def enroll_student(self):
        if not self.__is_enrolled:     #if (self.is_enrolled == Fals):
            self.__is_enrolled = True
            return f'-> {self.__name} is now enrolled'
        else:
            return f'-> {self.__name} is already enrolled'
            

    def drop_student(self):
        if self.__is_enrolled:     #if (self.is_enrolled == True):
            self.__is_enrolled = False
            return f'-> {self.__name} has dropped out'
        else:
            return f'-> {self.__name} has not dropped out'


    def __repr__(self):
        return f'{self.__student_id}, {self.__name}, {self.__department}, {self.__is_enrolled}'
    

    def view_student_info(self):
        student_info = f'------ ID:{self.__student_id}, Name:{self.__name}, dept:{self.__department}, Enrollment status:{self.__is_enrolled} ------'
        return student_info


StudentDatabase.add_student(1, "Mr. abc", "CSE", True)
StudentDatabase.add_student(2, "Mr. xyz", "EEE", True)
StudentDatabase.add_student(3, "Mr. uvw", "CSE", False)
StudentDatabase.add_student(4, "Mr. ABC", "EEE", False)
StudentDatabase.add_student(5, "Mr. UVW", "CSE", True)
 

# Replica System
while True:
                        
    print("Options:\n")
    print("1. View All Students")
    print("2. Enroll Student")
    print("3. Drop Student")
    print("4. Exit")
             
             
    ch=int(input("\nEnter Option:"))
             
    if ch==1:
        print("-------Students info------") 
        for student in StudentDatabase.student_list:
            print(student.view_student_info()) 
                 
    elif ch==2:
        print("-------Students Enrollment status ------") 
        for student in StudentDatabase.student_list:
            print(student.enroll_student()) 
            
    elif ch==3:
        print("-------Students drop out status ------") 
        for student in StudentDatabase.student_list:
            print(student.drop_student())
             
    elif ch==4:
        print('Exit')
        break
                
    else:
        print("\n\t---> !!! Choose Valid Option\n")
                  
       
