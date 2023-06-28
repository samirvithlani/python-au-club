#char array index, immutable

name = "royal techno"
# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])

# for i in name:
#     print(i)
    
    
# for i in range(len(name)):
#     print(name[i])



name = name.upper()
print(name)
name = name.lower()
print(name)
name = name.capitalize()
print(name)
name = name.title()
print(name)
name = name.swapcase()
print(name)
name ="Royal techno"
name = name.replace("o","0",3)
print(name)

email =" samir@gmail.com"
print(len(email))

#email = email.strip()
#email  = email.lstrip()
email = email.rstrip("o")
print(len(email))
print(email)

users = "raj,jay,part,neha,priya,patel"
#delimeter
userList = users.split(" ")
print(userList)





