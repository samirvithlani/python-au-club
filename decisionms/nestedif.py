age = int(input("Enter your age: "))


if age>=18:
    print("You are eligible to vote")
    
    if age>=21:
        print("You are eligible to marrige")
    
    else:
        print("You are not eligible to marrige")

else:
    print("You are not eligible to vote")        
    
    if age>=15:
        print("You are eligible to school")
    else:
       print("You are not eligible to school")    