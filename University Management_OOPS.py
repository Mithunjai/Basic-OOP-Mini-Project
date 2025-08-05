class Person:
    def __init__(self,name,age):
        self.__name = ""
        self.__age = ""
    
    def set_person(self,name,age):
        self.__name = name
        self.__age = age

    def display_person(self):
        print()
        print(f"Name = {self.__name}, Age = {self.__age}")

class Student(Person):
    def __init__(self):
        super.__init__("",0)
        self.__roll_no = 0
        self.__marks = 0

    def set_student(self,roll,marks):
        self.__roll_no = roll
        self.__marks = marks

    def display(self):
        print()
        print(f"Roll Number = {self.__roll_no}, Mark = {self.__marks}.")

    def calculate_grade(self):
        print()
        if(self.__marks>=90):
            return "A grade"
        elif(self.__marks>=75):
            return "B grade"
        elif(self.__marks>=60):
            return "C grade"
        else:
            return "D grade"
        
class Teacher(Person):
    def __init__(self):
        super.__init__("",0)
        self.__emp_id = ""
        self.__subject = ""

    def set_teacher(self,emp_id,sub):
        self.__emp_id = emp_id
        self.__subject = sub

    def display(self):
        print()
        print(f"Employee ID: {self.__emp_id}, Subject = {self.__subject}.")

def display_details(obj):
    obj.display_person()
    obj.display()