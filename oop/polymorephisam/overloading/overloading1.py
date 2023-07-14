
from multipledispatch import dispatch
#function with same name but different parameters
#real time example :  

#search(name)
#search(name,age)
#search(name,age,city)
#search(name,age,city,phone)
#search(name,company)
#search(name,company,city)

#teacher(subject)
#teacher(subject,exp)
#teacher(subject,exp,age)
#teacher(subject,exp,age)


#acopen(name)
#acopen(name,joingac)
#acopen(name,check?)
#acopen(name,joingac,check?)


class Shape():

    @dispatch(int)
    def getArea(self,h):
        print("Area of square is ",h*h)
    @dispatch(int,int)    
    def getArea(self,l,b):
        print("Area of rectangle is ",l*b)
    @dispatch(float)    
    def getArea(self,r):
        print("Area of circle is ",3.14*r*r)


s = Shape()
s.getArea(10.2)            
s.getArea(10,20)
s.getArea(10)
        