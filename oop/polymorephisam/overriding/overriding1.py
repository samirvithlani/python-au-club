#overriding ??
'''
    parent clas function created in child class called method overriding    
    same signature
    function name return type parameter list
'''

#Cg road crossword cg road ---> parent croswrd ahmedabad
# cg --> ABC --> 
# getBook():

#  jb cgroad --> hojb
#   vadpav()
#   vadpav()

# RBI
# withdraw()
# HDFC BANK AC -->
    # hdfcithdraw()
# SBI BANK ATM -->
   #sbwithdraw()
   
   
#TRAI
#call()
#msg()
# JIO 
    #call():
        #logic indonesia
 #jiocall
# Airtel 
    #call
     #singapore
#airtelcall  

class Parent():
    
    def getData(self):
        print("Parent class function")

class Child(Parent):
    def getData(self):
        print("Child class function")        
        super().getData()


c = Child()
c.getData()        

