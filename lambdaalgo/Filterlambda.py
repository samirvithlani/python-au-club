data = [6,7,9,34,23,45,66,78,9]
finalList = list(filter(lambda x: x %2 ==0, data))
print(finalList)

users = ["raj","ram","Neha","Preeti","kabir","malayalam","ramesh","ramnik"]
#userList = list(filter(lambda x:len(x)>4,users))
#userList = list(filter(lambda x:x[0] =='r',users))
#userList = list(filter(lambda x :x[0]=='r' and len(x)>4 and x[-1]=='k',users))
name  = "naman"
#reverse using lambda
#revname = lambda x:x[::-1]
revname = (lambda x,y:y==x[::-1])
revname1 = (lambda x,y:y==x[::-1] if "palindrome" else "not palindrome")

print(revname1(name,"naman"))

if revname(name,"naman"):
    print("palindrome")
else:
    print("not palindrome")    
#print(userList)



# for i in data:
#     if i % 2 == 0:
#         finalList.append(i)

# print(finalList)    
