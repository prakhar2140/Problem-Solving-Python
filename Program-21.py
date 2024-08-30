#Wap to print the sum of two number such that the sum is equal to the targeted or the the input value 
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]: 
        list1 = []
        for i in range (0,len(nums)):
            for j in range(i+1,len(nums)-1):
                if (nums[i]+nums[j]== target):
                    return [i,j]
        return []        

solution = Solution()
nums = [2, 2, 3, 2]
target = 4
result = solution.twoSum(nums,target)
print(result)                    