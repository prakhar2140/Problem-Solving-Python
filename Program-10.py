Row = int(input("Enter the number of rows"))
col = int(input("Enter the number of columns"))
matrix =[]
print("Enter the entries of the matrix row wise")

for row in range(Row):
    a=[]
    for column in range(col):
        a.append(int(input()))
    matrix.append(a)

# print("Given matrix")    

# for row in range(Row):
#     for column in range(col):
#         print(matrix[row][column],end="  ")
#     print()   

for row in range(Row):
    for column in range(col):
        if (matrix[row][column]==0):
            matrix[row]=0
            matrix[column]=0
        else:
            for row in range(Row):
                for column in range(col):
                    print(matrix[row][column],end="  ")
            print()
            