numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


res = list(map(lambda x: list(map(lambda y: y**2,x)),numbers))
print(res)


users = [["ram",1],["shyam",2],["amit",3],["hari",4]]

res1 = list(map(lambda x: list(map(lambda y: y.upper() if type(y) == str else y*2,x)),users))
print(res1)




# for i in users:
#     for j in i:
#         print(j)
#     print()        