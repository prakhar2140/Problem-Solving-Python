#WAP to find the square root of givrn number without using any inbuilt function

start =0
n= int(input("Enter the number"))
end = n
mid= 1
while(1):
    mid =(start+end)/2
    if(start >= end or mid == start or mid == end):
        break
    if((mid *mid)>n):
        break
    if((mid*mid)>n):
        end = mid
    else:
        start = mid
