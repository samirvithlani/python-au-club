from Util import InvalidNameException

try:
    name= input("Enter your name: ")
    for i in name:
        if i.isdigit():
            raise InvalidNameException("Name contains digit")

except InvalidNameException as e:
    print(e)
            