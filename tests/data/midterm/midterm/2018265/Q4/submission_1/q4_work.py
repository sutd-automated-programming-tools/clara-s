def determinant(matrix):
    number_of_rows = len(matrix)
    number_of_columns = len(matrix[0])
    
    if number_of_rows == number_of_columns:
        if number_of_rows == 1:
            determinant = matrix[0][0]
            return determinant 
        elif number_of_rows == 2:
            determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
            return determinant 
        elif number_of_rows == 3:
            n00 = matrix[0][0]
            n01 = matrix[0][1]
            n02 = matrix[0][2]
            n10 = matrix[1][0]
            n11 = matrix[1][1]
            n12 = matrix[1][2]
            n20 = matrix[2][0]
            n21 = matrix[2][1]
            n22 = matrix[2][2]
            determinant = n00*(n11*n22 - n12*n21) - n01*(n10*n22 - n12*n20) + n02*(n10*n21 - n11*n20)
            return determinant
    else:
        return None 