# Replace all occurence of the largest prime digit in the given number with zero and second largest with 1 and third largest with 2 and so on..
'''
Input:- 134368
Output:- 1034068
Input:- 98767310
Output:- 98060110
'''
num=int(input("Enter number "))
digits=[]
while(num>0):
    rem=num%10
    num=num//10
    digits.insert(0,rem)
prime=[7,5,3,2]
prime_list=[]
for next_digit in digits:
    for element in prime:
        if(next_digit==element):
            prime_list.insert(0,element)
prime_list.sort()
prime_list.reverse()
print(prime_list)  
l=len(prime_list)
ans=0   
print(digits)
for next_digit in digits:
    if next_digit in prime_list:
        for i in range(0,l):
            if(next_digit == prime_list[i]):
                ans= ans*10 + i
    else:
        ans=ans*10 + next_digit 
print(ans)      
