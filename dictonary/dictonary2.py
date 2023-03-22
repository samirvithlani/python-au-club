users ={1:(1,2,3)}
user1 = {1:{1:"raj",2:"ram",3:"ravi",2:"rakesh"},2:{1:"rani"}}
print(user1)

for i,j in user1.items():
    print(i)
    for x,y in j.items():
        print(x,y)
    