# []
# ()
# {}
# {}

data ={1:"raj",2:"ram",3:"ravi",2:"rakesh"}
print(data)

data.update({1:"rani"})
data[11]="neel"

#rmelm = data.pop(1)
#print(rmelm)

elm = data.get(111)
print(elm)

print(data.values())
print(data.keys())

#data.copy()
x= data.popitem()
print(x)

data.clear()

for i,j in data.items():
    print(i,j)
    

    