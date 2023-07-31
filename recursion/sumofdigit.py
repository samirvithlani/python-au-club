#123
def sumofdigit(no):
    #123 == 0   
    if no == 0:
        return 0
    
    return no %10 + sumofdigit(no//10)
    # 123 % 10 = 3 + sumofdigit(123//10)
    # 12 % 10 = 2 + sumofdigit(12//10)
    # 1 % 10 = 1 + sumofdigit(1//10)


x = sumofdigit(123)
print(x)