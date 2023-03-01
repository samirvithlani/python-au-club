#empty list
#data =[]
data =["ram","raj","hari","shyam","sita"]
#print(data[0])


# for i in range(0,len(data)):
#     print(data[i])

data.append("gita")
data.extend(["sita","radha"])
#data.extend("jay")

data.insert(2,"jaya")

removedelm = data.pop(1)
print("removing...",removedelm)


ind = data.index("sita")
print("index of sita is ",ind)

data.remove("sita")


for i in data:
    print(i)



c = data.count("sita")
print("count of sita is ",c)

#data.sort()
data.reverse()

data[0] = "amit"
print(data)


#list slicing
#print(data[::-2])    