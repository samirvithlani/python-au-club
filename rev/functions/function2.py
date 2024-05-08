def userData(users):
    
    if type(users)==list or type(users)==tuple:
        for user in users:
            print(user)
    else:
        print("Invalid data type")


#userData("John")                
userData(["John","Doe","Jane","Doe"])