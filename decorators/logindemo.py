
user ={"username":"joe","password":"1234"}
def loginRequired(func):
    
    def inner(username,password):
        if username == user["username"] and password == user["password"]:
            print("login success")
            return func(username,password,"success")
        else:
            return func(username,password,"fail")    
    
    return inner


@loginRequired
def getData(user,passsword,code):
    if(code == "success"):
        print("get data success")
    else:
        print("get data fail")
         

getData("joe","12345")            

    
        
    