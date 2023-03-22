#list []  is mutable
#tuple () is immutable

data =("apple", "banana", "cherry", "apple", "cherry")
print(data[0])
print(data.count("apple"))

for i in data:
    print(i)
    
class1 =("raj","jay","ram","sam")
class2 =("suchi","sita","gita","rita")
class3 = class1 + class2
class3[0]="mmm"
