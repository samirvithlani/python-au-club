List =[[1,2,3],[4,5,17,3,18,0,20],[8,90,78]]

sortedList = lambda x:(sorted(i) for i in x)
print(list(sortedList(List)))