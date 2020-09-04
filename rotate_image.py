matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] 
#[[7,4,1],[8,5,2],[9,6,3]]
#90degrees
#in-place
def rotate(matrix):
    matrix.reverse()
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

print(rotate(matrix))
