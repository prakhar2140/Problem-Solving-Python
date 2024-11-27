# WAP a python code to implement the Merge Sort algorithm 
def mergeSorting(arr):
    n = len(arr)
    mid = int(n/2)
    if n < 2:
        return arr
    left = []
    right = []
    for i in range(mid):
        left.append(arr[i])  # Use append instead of left[i] = arr[i]
    for i in range(mid, n):
        right.append(arr[i])  # Use append instead of right[i-mid] = arr[i]

    left = mergeSorting(left)
    right = mergeSorting(right)
    return merge(left, right, arr)

def merge(left, right, arr):
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            k += 1
            i += 1       
        else:
            arr[k] = right[j]
            k += 1
            j += 1
    while i < len(left):
        arr[k] = left[i]
        k += 1
        i += 1
    while j < len(right):
        arr[k] = right[j]
        k += 1
        j += 1        
    return arr

arr = [12, 10, 8, 15, 19, 1, 25, 30]
arr = mergeSorting(arr)
print(arr)