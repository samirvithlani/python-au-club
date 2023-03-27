#function is collection of statements
#use: to perform a specific task, to reuse the code
#boilerplate code: 20 line of code --> 10 files... 200 lines of code
#function 10 lines of code
#type of functions 2 ypes of functions
#1. built-in functions
#2. user defined functions

#4 types of user defined functions
#1. without arguments and without return value
#2. without arguments and with return value
#3. with arguments and without return value
#4. with arguments and with return value

#def keyword is used to define the function
#def function_name():
#    statements

def sum():
    a = 10
    b = 20
    c = a + b
    print(c)
    

sum()

def add():
    return 10 + 20

x = add()    
print(x)

def pow(b,p):
    return b ** p


p = pow(2,5)
print(p)


def getData():
    
    def getAge():
        return 20
    p = getAge()
    return p

a = getData()
print(a)