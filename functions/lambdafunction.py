#lambda - anonymous function

def sqr(x):
    return x*x
res = sqr(5)
print(res)

res1 = lambda x: x*x
print(res1(15))

#lambda function with multiple arguments
res2 = lambda a,b: a+b
x = res2(1,23)
print(x)

data = lambda *args: args[1]**2
print(data(1,2,3,4,5))

#lambda with string

upperName = lambda name: name.upper()

print(upperName("sachin"))
#lambda with if else

x1 = lambda a,b : a if a>b else b
print(x1(10,20))

#lambda with kwargs
x2 = lambda **kwargs: kwargs
print(x2(a=1,b=2,c=3))


