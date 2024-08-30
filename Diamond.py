n = int(input("Enter the number of rows"))

# Print the upper half of the diamond
m = n - 1
for i in range(0, n):
    for j in range(0, m):
        print(end=" ")
    m = m - 1
    for j in range(0, i + 1):
        print("* ", end="")
    print("")

# Print the lower half of the diamond
m = 1
for i in range(n - 2, -1, -1):
    for j in range(0, m):
        print(end=" ")
    m = m + 1
    for j in range(0, i + 1):
        print("* ", end="")
    print("")