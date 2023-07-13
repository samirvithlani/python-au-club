def isActive(func):
    
    def inner(*args):
        print("inner")
        print(args)
        for i in args:
            if i == True:
                return func()
        else:
            print("You are not active")
            return
    return inner


@isActive
def get():
    print("get")
    
get(10,10,True)    
        
        
            
    