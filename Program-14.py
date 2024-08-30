#WAP to print a fibonacci series in python
import math
def isPerfectsquare(x):
    s = int(math.sqrt(x))
    return s*s ==x

def isPalindrome(n):
    return isPerfectsquare(5*n*n+4) or isPerfectsquare(5*n*n-4)

n = int(input("Enter the number of fibonacci you want to print"))
print(0)
print(1)
for i in range(1,n):
    if (isPalindrome(i)== True):
        print(i)
    # else:
    #     print(i,"is not palindrome number")    


