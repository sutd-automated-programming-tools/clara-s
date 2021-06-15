def determinant(matrix):
    for i in matrix: #calling the list in matrix
        if i > 3 or i < 1: #if the matrix has n < 1 or n>3
            return None #return None
        elif i == 2: #if matrix has n = 2
            det = ( matrix[1][1] * matrix [2][2] ) - (matrix[1][2] * matrix[2][1])
            #det calculation stating the first value of matrix 1 multiply by second value of matrix 2 - vice versa to get the det value
        elif i == 1:
            det = matrix[1][1]
            #det for matrix with just one is just its value it the matrix eg [10] = 10
        elif i == 3:
            #create a code here for det for n =3 
            
    return det #return the value of the determinant