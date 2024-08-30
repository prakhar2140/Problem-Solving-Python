n =int(input("Enter the no rows"))

for i in range(1,n):
    for j in range(1,n-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()    
print("")    
# for j in  range(1,i):
#     print("*",end=" ")
# print()    

