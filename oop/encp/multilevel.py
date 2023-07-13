class Gov():
    tax =10.10

class State(Gov):
    grant = 1000
    
    def manageTax(self):
        print("Tax: ", self.tax)
        print("Grant: ", self.grant)


class City(State):
    amount =100
    
    def manageGrant(self):
        print("Tax: ", self.tax)
        print("Grant: ", self.grant)
        print("Amount: ", self.amount)
        


city = City()
city.manageGrant()
city.manageTax()        

state = State()
state.manageTax()
#state.manageGrant() error