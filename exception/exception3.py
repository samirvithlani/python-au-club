class InvalidAgeException(Exception):
    
    def __init__(self, message):
        super().__init__(message)



age = int(input("Enter age: "))

# try:
#     if age<18:
#         raise ValueError("Age is less than 18")

# except ValueError as e:
#     print(e)


try:
    if age<18:
        raise InvalidAgeException("Age is less than 18")

except InvalidAgeException as e:
    print(e)    