#list mutable..
#list allows duplicate values..
#list follows insertion order..
#list is ordered..
#list is indexed..
#list using backedn data structure is dynamic array..
#is list is contiguous?

data =["hindi","english","maths","science","social","english","social"]
print(data)

data.append("computer")
data.extend(["physics","chemistry"])
#data.extend("biology")
#data.append(1,"biology")
data.insert(1,"biology")
data.remove("english")
x = data.pop(2)
print("removing...",x)

ind = data.index("social")
print("index of social is",ind)

cnt = data.count("social")
print("count of social is",cnt)

data.sort()
data.reverse()



for i in data:
    print(i)
    

