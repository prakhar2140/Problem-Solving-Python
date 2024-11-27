# Take a number user input from the user replace the even digit with 0 and odd digit with 1
num = int(input("Enter the number "))
list1 = []
while num >0:
    rem = num %10
    num =num //10
    list1.insert(0,rem)
sum =0
for i in list1:
    if i%2==0:
        sum = sum*10 + 0
    else:
        sum = sum*10 + 1
print(sum)        

    