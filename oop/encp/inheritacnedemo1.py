class Vehicle():
    makeYear = 0
    vehType =''
    
    def vehilceData(self):
        print("vehicle data")
    


class Car(Vehicle):
    
    def getCarData(self):
        self.vehilceData()
        self.makeYear = int(input("Enter the make year: "))
        self.vehType = input("Enter the vehicle type: ")
        
    
    def printCarData(self):
        self.vehilceData()
        print("Make year: ", self.makeYear)
        print("Vehicle type: ", self.vehType)


c = Car()
c.getCarData()
c.printCarData()         
            