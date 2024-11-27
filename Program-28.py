# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

nums = [-1,0,1,2,-1,-4]

nums.sort()
n = len(nums)
list1= [] 
for i in range(0,n-2):
    # Skip duplicates for the first element
    if i > 0 and nums[i] == nums[i - 1]:
        continue
    left = i+1
    right = n-1

    while left <right:
        sum = nums[i] + nums [left] + nums [right] 

        if sum == 0:
            list1.append([nums[i], nums [left] , nums [right]])
            left += 1
            right -= 1
            # Skip the repeated element from left side  
            while left < right and nums[left] == nums[left+1]:
                left += 1 
            # Skip the repeated element from right side  
            while left < right and nums [right] == nums[right-1]:
                right -= 1   
        elif sum <= 0:
            left += 1 
        else:
            right -= 1
                    
print(list1)        
        