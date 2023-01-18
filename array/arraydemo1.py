import array as arr
# typecode 'i' for signed integer
a = arr.array('i',[12,25,74,45,67,25])


# for i in range(0,len(a)):
#     print(a[i])
    

#a.append(100)
#removedelm = a.pop(15)
#print("removing...",removedelm)
#a.remove(25)

# a.extend([25,63,96])
# a.insert(1,75)
#print("a[100]",a[100])
 
#print(a.count(256))
#print(a.index(25))
a.reverse()

    
for i in a:
     print(i)    

