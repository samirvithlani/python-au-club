#123
#12
#1
#0
def sumofdigit(no):
    
    #123 ==0 false
    #12 ==0 false
    #1 ==0 false
    #0 ==0 true
    if no == 0:
        return 0
    
    return no%10 + sumofdigit(no//10)
    # 3 + sumofdigit(12)
    # 3 + 2 + sumofdigit(1)
    # 3 + 2 + 1 + sumofdigit(0)



x = sumofdigit(123)
print(x)

#revers no usinf recursion
#factorial using recursion 