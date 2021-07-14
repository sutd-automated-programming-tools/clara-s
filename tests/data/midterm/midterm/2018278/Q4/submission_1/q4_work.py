
def determinant(matrix):
    n = len(matrix)

    if n == 1:
        res = matrix[0][0]
       
    elif n == 2:
        res = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        
    elif n == 3:
        x = matrix[1][1] * matrix[2][2] - matrix[2][1] * matrix[1][2]
        y = matrix[1][0] * matrix[2][2] - matrix[2][0] * matrix[1][2]
        z = matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]
        a = matrix[0][0]
        b = matrix[0][1]
        c = matrix[0][2]
        res = a*x - b*y + c*z
    else: 
        res = None
    
    return res