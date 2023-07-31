#5
def fact(no):
    
    if no ==0 or no ==1:
        return 1
    
    return no * fact(no-1)
    # 5 * fact(4)
    # 4 * fact(3)
    # 3 * fact(2)
    # 2 * fact(1)
    # 1 * fact(0)
    

print(fact(5))
