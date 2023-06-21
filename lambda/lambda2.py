sqr = lambda x: x**2
ans = lambda fun,x: fun(x)
print(ans(sqr,10))

cube = lambda x: x**3
ans1 = lambda a: sqr(a) if a %2 == 0 else cube(a)
print(ans1(4))


# def outer(a,b):
#     def inner(c):
#         return a+b+c
    
#     inner(10)

# outer(10,20)    

#nested lambda

x = lambda a,b: lambda c: a+b+c
print(x(10,20)(40))


x1 = lambda str:lambda str1: str.upper() + str1.title()
print(x1("hello")("world java"))
