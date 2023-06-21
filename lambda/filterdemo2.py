users = ["tom","harvy","mike","donna","rachel","mala","naman","madam"]

filusers = list(filter(lambda x: len(x)>3,users))
filusers = list(filter(lambda x: x == x[::-1],users))

print(filusers)

# for i in users:
#     if i.startswith("h"):
#         filusers.append(i.upper())

        