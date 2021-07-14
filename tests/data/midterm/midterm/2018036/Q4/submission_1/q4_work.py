def sq_check(matrix):
    size = len(matrix)
    for i in matrix:
        if len(i) == size:
            valid = True
        else:
            valid = False
            break
    return valid,size
        
def determinant(matrix):
    valid2,size2 = sq_check(matrix)
    if valid2 == False:
        return None
    else:
        if size2 == 1:
            det = matrix[0][0]
        elif size2==2:
            det = matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
        elif size2==3:
            det = matrix[0][0]*(matrix[1][1]*matrix[2][2]-matrix[1][2]*matrix[2][1])-matrix[0][1]*(matrix[1][0]*matrix[2][2]-matrix[1][2]*matrix[2][0])+matrix[0][2]*(matrix[1][0]*matrix[2][1]-matrix[1][1]*matrix[2][0])
        return det