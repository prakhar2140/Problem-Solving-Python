n = int(input("Enter the number how much you want to print"))
a=0
b=1
if n ==1:
    print(a)
elif n ==2:
    print(a)
    print(b)
else:
    print(a)
    print(b)
    for i in range(2,n+1):
        c=a+b
        a=b
        b=c
        print(b)        