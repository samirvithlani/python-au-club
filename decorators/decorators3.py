def division(func):
    
    def inner(a,b):
        if b==0:
            print("Can't divide by zero")
            return
        
        return func(a,b)
    return inner

@division
def divide(a,b):
    print(a/b)
    

divide(10,2)    