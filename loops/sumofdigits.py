no = int(input("Enter a number:"))
rem = 0
sum = 0
#987  789
while no!=0:
    #789  78  7
    #rem = 9  8
    rem = no % 10
    
    #0 = 0 * 10 +7 = 7
    #7 = 7 * 10 +8 = 78
    #78 = 78 * 10 +9 = 789
    sum = sum *10 + rem
    
    no = no//10
    #98
    
print("Sum of digits is:",sum)    
    