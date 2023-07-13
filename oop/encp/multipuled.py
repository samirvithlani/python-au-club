class Gov():
    tax =10.10
    amount =10

class State():
    grant = 1000
    amount =100


class City(State,Gov):
    
    def getData(self):
        print("Tax: ", self.tax)
        print("Grant: ", self.grant)
        print("Amount: ", self.amount)


city = City()
city.getData()        