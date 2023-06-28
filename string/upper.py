def toUpperCase(name):
    ch = ''
    for i in range(len(name)):
        if(ord(name[i]) >= 97 and ord(name[i]) <= 122):
            ch = ch + chr(ord(name[i]) - 32)
        
        
    return ch
            
            
            

name = toUpperCase('naman')
print(name)