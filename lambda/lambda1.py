demo = lambda a:print("hello this is lambda",a)
demo(10)

demo1 = lambda a,b:print("hello this is lambda",a,b)
demo1(10,20)

demo2 = lambda x: x**x
print(demo2(3))
x = demo2(4)
print(x)

larger = lambda a,b :a if a>b else b
print(larger(10,20))

containg_a =  lambda str: True if 'a' in str else False
print(containg_a("hella"))

nested = lambda a,b: print("a is greated") if a>b else (print("b is greater") if b>a else print("both are equal"))
nested(10,10)

x = lambda str: True if str == str[::-1] else False
print(x("madama"))