# Replace all the occurence of a digit with another given digit in a number 
num = int(input("Enter the Number "))
n = int(input("Enter the first digit "))
k = int(input("Enter the second digit "))
list1 = []
while num > 0:
    rem = num%10
    num = num//10
    list1.insert(0,rem)
sum =0 
for i in list1:
    if i is n :
        sum = sum*10 + k
    else:
        sum = sum*10 + i   

print(sum)               


