#keyword argument

def empData(sal,name,email,age):
    print("Name: ",name)
    print("Email: ",email)
    print("Age: ",age)


#empData("ram","ram@gmail.com",25)    
#empData(25,"ram","ram@gmail.com")    
#empData(email="ram@gmail.com",age=25,name="ram",89) compile time error
empData(56789,email="ram@gmail.com",age=25,name="ram") 
