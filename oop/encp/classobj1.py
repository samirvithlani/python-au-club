class Vehicle():
    print("This is a Vehicle class")
    makeyear = 2019 #class variable , #instance variable
    
    def getVehData(self,name):    
        print(self)
        print("This is a Vehicle data",self.makeyear) 
        print("This is a Vehicle data",name)



veh = Vehicle()
print(veh.makeyear)
#obejct
veh.getVehData("Honda")

veh1 = Vehicle()
veh2 = Vehicle()

veh1.getVehData("Honda")
veh2.getVehData("Audi")

    