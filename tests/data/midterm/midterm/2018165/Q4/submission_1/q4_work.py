def determinant(matrix):
    if range(len(matrix)) != range(len(determinant)):
        return none
    
    
#determine index count of the matrix
#if index count of matrix == i, number of list in matrix == i, else return none
#for n = 1, det(i) = det
#for n = 2, det(j) = (M[j]+M[j+3])-(M[j+1]+M[j+2])
#for n = 3, det(k) = (M[k]*det(k)-(M[k+1]*det(k+1))+(M[k+2]*det(k+2))
