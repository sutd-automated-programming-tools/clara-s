def determinant(matrix):
    m = matrix
    Lmatrix = []
    
    for x in range(len(m)):
        n=len(x)

    if n=1:
        return matrix[0]
    
    if n=2:
        a = (m[0][0])*(m[1][1])
        b = (m[0][1])*(m[1][0])
        c = a-b
        return c
     
    