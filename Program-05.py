'''Example Given an integer array nums, return an array
answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
Input: nums = [1,2,3,4]
Output:[24,12,8,6]'''


def product_except_self(nums):
   
    n = len(nums)
    answer = [1] * n

    # Calculate the product of all elements to the left of each element
    left_product = 1
    for i in range(n):
        answer[i] *= left_product
        left_product *= nums[i]

    # Calculate the product of all elements to the right of each element
    right_product = 1
    for i in range(n-1, -1, -1):
        answer[i] *= right_product
        right_product *= nums[i]

    return answer


nums = [1, 2, 3, 4]
result = product_except_self(nums)
print(result)  # [24, 12, 8, 6]