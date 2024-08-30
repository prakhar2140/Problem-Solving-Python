#Wap to add a two number without using any arithmetic Operator

x=int(input("Enter the first number"))
y=int(input("Enter the second number"))
while(y!=0):
    carry = x & y
    x= x ^ y
    y= carry<<1
print(x)    

print(x.__add__(y))

for i in range(y):
    x+=1

print(x)


