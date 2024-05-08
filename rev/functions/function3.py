#args,kwrgs,keywds

def printUsers(*args):
    print(type(args))
    print(args)


printUsers(100,20,45,67,89,90)    


def printUsers1(*args,x):
    print(type(args))
    print(args)
    print("x=",x)


printUsers1(100,20,30,x=40)    