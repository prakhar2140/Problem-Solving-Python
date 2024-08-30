# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
a = [0,1,0,3,12]
t =0
n =len(a)
for i in range(0,n):
    for j in range(0,n-1):
        if (a[j]==0 and a[j+1]!=0):
            t = a[j]
            a[j]= a[j+1]
            a[j+1]= t
print(a)            