key =[1,2,3,4,5]
value =["raj","ram","ravi","rakesh","rani"]
data ={}

# for i in key:

#     for j in value:
#         data[i]=j


data = {i:j for i,j in zip(key,value)}
print(data)        