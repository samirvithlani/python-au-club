
#this function will ac as decorators....
def orderPizza(func): # 3 func = throwParty
    #throwparty
    
    def inner(person): #5
        print(person)
        print("Ordering Pizza")#6
        return func(person*2)#7
    
    return inner #4



@orderPizza
def throwParty(pizza):
    print(pizza)
    print("Throwing a party")

#100 person * 2 =200
throwParty(100) #1    