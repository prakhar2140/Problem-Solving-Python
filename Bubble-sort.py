a= []
n = int (input("Enter the no of element in list:-"))
print("Enter value:-")
for i in range(n):
    b = int (input())
    a.append(b)
print("Your list here:-",a)    
t=0
len1 = len(a)
for i in range(0,len1):
    for j in range(0,len1-1):
        if(a[j]>a[j+1]):
            t=a[j]
            a[j]=a[j+1]
            a[j+1]=t 
print("Sorted array is ",a) 
        