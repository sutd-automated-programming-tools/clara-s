def find_2ndet(matrix):
    det = ((matrix[0][0])*(matrix[1][1]))-((matrix[0][1])*(matrix[1][0]))
    return det
#print(find_2ndet([[2,4],[3,4]]))
    
def determinant(matrix):
    rows_matrix = len(matrix)
    det = 0
    for col in matrix:
        col_matrix = len(col)
        if col_matrix != rows_matrix:
            return None
        elif col_matrix ==1:
            det = matrix[0][0]
        else:
            if col_matrix ==2:
                det = find_2ndet(matrix)
            elif col_matrix ==3:
                new_ls = []
                for sub_matrices in matrix:
                    new_ls.append(matrix[1])
                    new_ls.append(matrix[2])
                    return new_ls
                    matrix1 = []
                    matrix2 = []
                    matrix3 = []
                    matrix1.append(new_ls[0])
                    del matrix1[0][0]
                    matrix1.append(new_ls[1])
                    del matrix1[1][0]
                    matrix2.append(new_ls[0])
                    del matrix2[0][1]
                    matrix2.append(new_ls[1])
                    del matrix2[1][1]
                    matrix3.append(new_ls[0])
                    del matrix3[0][2]
                    matrix3.append(new_ls[1])
                    del matrix3[1][2]
                    det1 = find_2ndet(matrix1)
                    det2 = find_2ndet(matrix2)
                    det3 = find_2ndet(matrix3)
                    det = (matrix[0][0]*det1) - (matrix[0][1]*det2) + (matrix[0][2]*det3)
    return det
print(determinant([[1,2,3],[4,5,6],[7,8,9]]))          
                