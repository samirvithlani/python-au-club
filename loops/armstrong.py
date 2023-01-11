   #       3    3    3 
# 371 --> 3  + 7   +1  = 27 + 343 + 1 = 371

no = int(input("Enter a number:"))
temp = no
count =0
rem =0
sum =0
while no!=0:
    count+=1
    no = no//10

while temp!=0:
    rem = temp % 10
    sum = sum + rem**count
    temp = temp//10

print("Number of digits is:",count)    
print("Sum of digits is:",sum)