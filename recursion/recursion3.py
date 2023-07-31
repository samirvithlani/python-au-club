

def printNo(no):
    # 10 == 0 false
    
    if no ==0:
        return
    
    printNo(no-1)
    print(no)


printNo(10)    
    
    