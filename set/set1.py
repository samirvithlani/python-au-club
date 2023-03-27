#list []
#tuple ()
#dicto{:}
#{} --> unorderd 

#blank set
users =set()
#users = {"a","b","c"}
users.add("a")
users.add("b")
users.add("c")
users.add("d")
users.add("d")
users.add("c")

#users.remove("aa")
#users.update(["x","y","z"])
#users.update(("p","q","r"))
#users.update("samir")

#users.discard("aa")

#users.clear()

friends1 ={"ram","raj","ravan","priya"}
friends2 ={"priya","priti","prakash"}

#mutual = friends1.union(friends2)

#mutual = friends1.intersection(friends2)
#mutual = friends1.difference(friends2)
#mutual = friends2.difference(friends1)
#friends1.difference_update(friends2)
#friends1.intersection_update(friends2)
#print(mutual)
#x = friends1.issubset(friends2)
#x = friends1.issuperset(friends2)
#x = friends1.pop()
mutual = friends1.symmetric_difference(friends2)
friends1.symmetric_difference_update(friends2)
#print(x)
print(mutual)






#print(users)