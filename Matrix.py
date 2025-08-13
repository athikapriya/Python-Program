# matrix is a two dimensional list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0][2])
print(matrix[2][1])

# print with nested loop
for row in matrix:
    for col in row:
        print("All values : ", col)

matrix[0][2] = 10 # changing value
print(matrix[0][2])