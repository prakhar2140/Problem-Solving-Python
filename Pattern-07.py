n = 5

print("Pattern 1")

for i in range (0,n):
    for j in range (i):
        print("*", end="")
    print()

for i in range (n,0,-1):
    for j in range (i):
        print("*", end="")
    print()