
def printData(no):
    
    if no >0:
        printData(no-1)
        print(no)
    

printData(10)    