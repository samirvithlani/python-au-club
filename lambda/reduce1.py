#//reucee will return a single value

from functools import reduce

numbers = [1,2,3,4,5,6,7,8,9,10]

ans = reduce(lambda x,y: x+y,numbers)
print(ans)