# Write a program to find the given number is Perfect number or not .

n = int(input("Enter the number that you want to check Perfect or not "))

sum=0
for i in range(1,n):
  if (n %i == 0):
    sum = sum+i
if (sum == n):
  print("Number is Perfect number ")
else:
    print("NUmber is not Perfect number ")
      
    
