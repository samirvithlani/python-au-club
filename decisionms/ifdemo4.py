no = int(input("Enter a number: "))
'''
    and  or
    no %2==0 and no>=20
    T   T   T
    F    -   F
    T  F   F
    no %2==0 or no>=20
    
    T - T t
    F - T t
    F - F f
    '''


if no %2==0 or no>=20:
    print("Even and greater than 20")
else:
    print("Odd or less than 20")    