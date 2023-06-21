#map....
users = ["raj","parth","jay","amit","harish"]
filuser = list(map(lambda x:x.upper(),users))
# for i in users:
#     filuser.append(i.upper())


numbers = [100,200,300,400,500]
def add(inc):
    return list(map(lambda x: x+inc,numbers))



numbers = add(1)
print(numbers)