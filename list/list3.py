numbers = [11,25,36,98,75,63,69]
evnlist =[]

# for i in numbers:
#     if i %2 ==0:
#         evnlist.append(i)


evnlist = [i for i in numbers if i%2==0]
print(evnlist)      
  
  