# WAP to reverse the element of the list
arr = [10,20,30,40,50]
n =len(arr)
for i in range(n//2):
    temp = arr[i]
    arr[i] = arr[n-1-i]
    arr[n-1-i] = temp
print(arr)
