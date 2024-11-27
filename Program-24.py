# WAP to print smallest positive missing number from the list 

nums = [7,8,9,11,12]
n =len(nums)

i = 1
while True:
    found = False
    for x in nums:
        if x == i:
            found = True
            break
    if not found:
        max = i
        break
    i += 1
print(max)    
