# Write an algorithm such that if an element in MxN matrix is 0, it's entire row and column are set to 0.
def rowZero(matrix, row):
    for i in range(len(matrix[row])):
        matrix[row][i] = 0

def columnZero(matrix, column):
    for i in range(len(matrix)):
        matrix[i][column] = 0


def matrixZero(matrix):
    points = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                points.append((i,j))
    
    for p in points:
        rowZero(matrix, p[0])
        columnZero(matrix, p[1])
            


matrix = [[1,1,1,1],[1,1,1,1],[1,1,0,1],[1,1,1,1],[1,1,1,0]]

matrixZero(matrix)

print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix]))