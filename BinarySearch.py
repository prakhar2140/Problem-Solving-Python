#WAP to implement binary search using Python programming
def binarySearching(arr,target):
    n =len(arr)
    start =0
    end = n-1
    while(start<=end):
        mid =int (start +(end-start)/2)
        if (arr[mid]==target):
            ans = mid
            return mid
        elif (arr[mid]<target):
            start = mid+1
        else:
            end = mid-1

arr= [10,12,15,16,48,52,55]
index = binarySearching(arr,48)
print(index)

    