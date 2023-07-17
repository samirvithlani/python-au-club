
try:
    no1 = int(input("Enter no1: "))
    no2 = int(input("Enter no2: "))
    ans = no1 / no2
    print("Division is: ", ans)
    name ="raj"
    name[6]
    
    
except ZeroDivisionError as e:
    #print("Division by zero is not possible")    
    print(e)
except ValueError as e:
    print("Invalid input") 
       
except:
    print("Something went wrong")

print("End of program")    