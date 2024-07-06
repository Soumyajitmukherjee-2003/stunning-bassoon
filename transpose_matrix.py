'''                             TRANSPOSE MATRIX
You're given a 2D array of integers matrix. Write a function that returns the transpose
of the matrix. 
The transpose of a matrix is a flipped version of the original matrix across its main diagonal 
(which runs from top-left to bottom-right); it switches the row and column indices of the original
matrix.
You can assume the input matrix always has at least 1 value; however its width and height are not necessarily
the same.
'''


def transposeMatrix(matrix):
    transposed_matrix=[list(row) for row in zip(*matrix)]
    return transposed_matrix


'''
    SAMPLE INPUT
matrix= [
[1,2],   
]

    SAMPLE OUTPUT
[
   [1],
   [2]
]    
'''
