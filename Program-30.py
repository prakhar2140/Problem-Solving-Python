# Given a number replace all occurence of the smallest digits with the largest digit in the number .You must not convert the no into string at any point 
'''
Taking input from user 
Separate digit 
Min no and Max no 
Join the digit as a number 
'''
num = int(input("Enter a number "))
list1 = []
# Now separate digit 
while num>0:
    rem = num % 10
    num = num //10
    list1.insert(0,rem)
maxi = max(list1)
mini = min(list1)
sum =0
for next_digit in list1:
    if next_digit == mini:
        sum = sum * 10 + maxi
    else:
        sum = sum * 10 + next_digit       

print(sum)    
