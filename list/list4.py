num = []
for i in range(1, 21):
    num.append(i)

obj=[]
# for i in num:
#     if i %2 ==0:
#         obj.append("evne")
#     else:
#         obj.append("odd")   

obj = ["even"  if i %2 ==0 else "odd" for i in range(1,21)]
print(obj)   

     
        
   