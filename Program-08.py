#WAP to find length of the digit given by the user

n = int(input("Enter the number:--"))
count = 0

if (n == 0):
    print("The length of the given Number is 1")
elif (n<0):
    n= -1*n
    while(n!=0):
        n = n//10
        count +=1
    print("The length of digit is",count)

else:
    while(n!=0):
        n = n//10
        count +=1
    print("The length of digit is",count)     



    