#functions...
#def keyword is used to define a function in python

def test():
    print("This is a test function")
    #without return statemenrt without arguments


test() 

def test1(a,b)->int:
    print("This is a test1 function")   
    
    return a+b


ans = test1(100.20,20.70)
print(ans)