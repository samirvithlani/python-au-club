def star(func):
    print(".....",func.__name__)
    def inner(*args,**kwargs):
        print("*" * 15)
        func(*args,**kwargs)
        print("*" * 15)
    return inner   

def percent(func):
    print("////",func.__name__)
    def inner(*args,**kwargs):
        print("%" * 15)
        func(*args,**kwargs)
        print("%" * 15)
    return inner    
        

@star
@percent
def printing(msg):
    print(msg)        
    
    

printing("Hello")    