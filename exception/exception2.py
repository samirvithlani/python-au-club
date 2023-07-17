name = input("Enter your name: ")

try:
    x = name[5]

except :
    print("Something went wrong")    
    
else:
    print("Nothing went wrong")
    print(x)    

finally:
    print("Finally block is always executed")    
