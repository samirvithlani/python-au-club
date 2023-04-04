amount =[12,22,33,44,67,89,7]

data = ["raj","ram","Neha","Preeti","kabir","malayalam","ramesh","ramnik"]
sqamount = list(map(lambda x:x**2,amount))
updateddata = list(map(lambda x:x.upper(),data))
#condition map


updateList = list(map(lambda x:x.upper() if x[0] =='r' else x.lower(),data))
print(updateList)

#3 len name store --> upper


print(updateddata)
print(sqamount)
