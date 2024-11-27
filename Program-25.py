'''Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.'''

nums = [0,0,1,1,1,2,2,3,3,4]
result = []
n = len(nums)

for i in range(0,n):
    for j in range(n-1,0,-1):
        if (nums[i] == nums[j]):
            result.append(nums[i])
    result.append('_')    

print(result)            
