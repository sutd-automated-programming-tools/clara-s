def is_square(matrix):
    n = len(matrix)
    for row in matrix:
        if len(row) != n:
            return False
    return True

def cofactor(matrix, i, j):
    new_matrix = matrix[:i] + matrix[i+1:]
    new_matrix = [row[:j]+row[j+1:] for row in new_matrix]
    return determinant(new_matrix)*(-1)**(i+j)

def determinant(matrix):
    if not is_square(matrix):
        return None

    n = len(matrix)

    if matrix == []:    # recursion base case
        return 1
    else:               # perform cofactor expansion
        return sum(matrix[i][0]*cofactor(matrix, i, 0) for i in range(n))
