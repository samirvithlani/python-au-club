#read data word to word

file = open("./file/student.txt","r")

for i in file.read().split():
    print(i)
