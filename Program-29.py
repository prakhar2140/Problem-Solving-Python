# WAP to convert 2D array into 1D

arr2d = [[1,2,3],[4,5,6],[7,8,9]]

arr1d = []
for i in arr2d:
    for j in i:
        arr1d.append(j)

print(arr1d)        #Output [1,2,3,4,5,6,7,8,9]
'''
Input: original = [1,2,3,4], m = 2, n = 2
Output: [[1,2],[3,4]]
Explanation: The constructed 2D array should contain 2 rows and 2 columns.
The first group of n=2 elements in original, [1,2], becomes the first row in the constructed 2D array.
The second group of n=2 elements in original, [3,4], becomes the second row in the constructed 2D array.
'''
# WAP to convert 1D array into 2D

arr = [1,2,3,4]
index = 0
list1 =[]
m=2
n=2
for i in range(0,2):
    for j in range(0,2):
        list[i][j].append(arr[index])
        index+=1

print(list1)         