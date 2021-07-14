# Q4: Square Matrix
def determinant(matrix):
    size = len(matrix)
    # We check the rows to make sure it's square
    for row in matrix:
        if len(row) != size:
            return None
    # Now that that's okay, we perform computation
    if size == 1:
        return matrix[0][0]
    elif size == 2:
        ad = matrix[0][0] * matrix[1][1]
        bc = matrix[0][1] * matrix[1][0]
        return (ad - bc)
    else:
        det = 0
        for i in range(len(matrix[0])):
            coeff = (-1) ** i * matrix[0][i]
            submatrix = []
            for j in range(1,len(matrix)):
                subline = matrix[j][0:i]+matrix[j][i+1:]
                submatrix.append(subline)
            det += coeff * determinant(submatrix)
    return det