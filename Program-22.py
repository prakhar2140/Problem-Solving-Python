#WAP to find median of the two sorted array 
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums3 = nums1 + nums2
        nums3.sort()
        n = len(nums3)
        
        if n % 2 == 0:
            return (nums3[n//2 - 1] + nums3[n//2]) / 2
        else:
            return nums3[n//2]
            
solution = Solution()
nums1 = [1,2]
nums2 = [3,4]
result = solution.findMedianSortedArrays(nums1,nums2)
print(result)            
             
                
                 
                 