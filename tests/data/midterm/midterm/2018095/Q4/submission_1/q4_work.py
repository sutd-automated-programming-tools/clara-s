
def determinant(A):
    if len(A) != len(A[0]):
        return None
    if len(A) == 1:
        return A[0][0]
    elif len(A)==2:
        val = A[0][0]*A[1][1] - A[0][1]*A[1][0]
        return val
    else:
        val = A[0][0]*(A[2][2]*A[1][1] - A[1][2]*A[2][1]) -A[0][1]*(A[1][0]*A[2][2] - A[1][2]*A[2][0])+A[0][2]*(A[1][0]*A[2][1] - A[1][1]*A[2][0])
        return val