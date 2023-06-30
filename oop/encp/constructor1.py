#constructor : constructor is a special funciton which has same name as class name...
# __init__(): is a constructor
# type of constructor.... default constructor, parameterized constructor, copy constructor
# what is the use of constructor?? to initialize the instance variable of class

class Student():
    
    rolno = 0
    
    def __init__(self,rolno):
        self.rolno = rolno
        print("This is a constructor",rolno)


stu = Student(101)  
print(stu.rolno)   
stu2 = Student(102)
print(stu2.rolno)   
    

