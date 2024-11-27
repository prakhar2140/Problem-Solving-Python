# WAP to sort element of the list using Insertion sort
arr= [12,10,8,15,19,1,25,30]
n =len(arr)

for i in range(n):
    key = arr[i]
    j =i-1
    while(j>=0 and arr[j]>key):
        arr[j+1] = arr[j]
        j -=1
    arr[j+1] = key

print(arr)        