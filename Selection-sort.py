a = [5,3,4,8,1]
t=0
len1 = len(a)
for i in range(0,len1):
    for j in range(i+1,len1):
        if(a[i]>a[j]):
            t=a[i]
            a[i]=a[j]
            a[j]=t
print("Sorted array is ",a)             