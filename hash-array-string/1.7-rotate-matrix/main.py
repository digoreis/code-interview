# Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a 
# method to rotate the image by 90 degrees. Can you do this in place?

matrix = [[0,0,0,0],[1,1,1,1],[2,2,2,2],[3,3,3,3]]

def rotate( matrix ):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0])-1,-1,-1)]

print(rotate(matrix))