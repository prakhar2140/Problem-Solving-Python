n = int(input("Enter no of rows"))

for i in range(n):
    for j in range(i+1,n):
        print("*",end=" ")
    print()   
for i in range(n-1):     
    for j in range(i+1):
        print("*",end=" ") 
    print()       
