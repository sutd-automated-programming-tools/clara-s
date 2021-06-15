import copy
def detof1by1(matrix):
    det = matrix[0][0]
    return det

def detof2by2(matrix):
    det = matrix[0][0]*matrix[1][1] - matrix[1][0]*matrix[0][1]
    return det
    
def detof3by3(matrix):
    first_matrix = copy.deepcopy(matrix)
    del first_matrix[0] 
    del first_matrix[0][0]
    del first_matrix[1][0]
    first_term = matrix[0][0] * detof2by2(first_matrix)
    
    second_matrix = copy.deepcopy(matrix)
    del second_matrix[0]
    del second_matrix[0][1]
    del second_matrix[1][1]
    second_term = -1 * matrix[0][1] * detof2by2(second_matrix)
    
    third_matrix = copy.deepcopy(matrix)
    del third_matrix[0]
    del third_matrix[0][2]
    del third_matrix[1][2]
    third_term = matrix[0][2] * detof2by2(third_matrix)
    
    total= first_term + second_term + third_term
    return total

def determinant(matrix):
    for row in matrix:
        if len(row) != len(matrix):
            return None    
    if len(matrix) > 3:
        return None
    elif len(matrix) == 1 :
        return detof1by1(matrix)
    elif len(matrix) == 2:
        return detof2by2(matrix)
    elif len(matrix) == 3:
        return detof3by3(matrix)
