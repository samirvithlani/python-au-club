def store():
    return 100
    return 200
    return 200

print(store())

def storing():
    yield 100
    yield 200
    yield 300
    yield 400
    

for i in storing():
    print(i)