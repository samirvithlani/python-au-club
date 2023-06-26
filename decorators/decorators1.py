
#this function will ac as decorators....
def orderPizza(func): # 3 func = throwParty
    #throwparty
    
    def inner(): #5
        print("Ordering Pizza")#6
        func()#7
    
    return inner #4



@orderPizza#2
def throwParty():
    print("Throwing a party")

throwParty() #1    