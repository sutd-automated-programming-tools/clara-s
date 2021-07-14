def determinant(matrix):
    M = matrix
    
    for n in range(len(M)):
        
        if n == 1:
            det = M[0][0]
            return det

        if n == 2:
            det = (M[n-2][n-2]) *  (M[n-1][n-1]) - (M[n-2][n-1]) * (M[n-1][n-2])
            return det
        if M == 3:
            det = M[0][0] * ((M[n-2][n-2]) *  (M[n-1][n-1]) - (M[n-2][n-1]) * (M[n-1][n-2])) - M[n-3][n-2]
        if len(M[0]) != len(M[n]):
            return None 
        if n <1 and n>3:
            return None
