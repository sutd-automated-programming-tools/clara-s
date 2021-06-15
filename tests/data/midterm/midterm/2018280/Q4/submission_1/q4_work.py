def determinant(matrix):
    
    def single_matrix(m):
        return m[0][0]
    
    def double_matrix(l):
        return l[0][0] * l[1][1] - l[0][1] * l[1][0]
    
    def triple_matrix(x):
        det_first = [[x[1][1], x[1][2]],[x[2][1], x[2][2]]]
        first = x[0][0] * double_matrix(det_first)
        det_second = [[x[1][0], x[1][2]], [x[2][0], x[2][2]]]
        second = x[0][1] * double_matrix(det_second)
        det_third = [[x[1][0], x[1][1]],[x[2][0], x[2][1]]]
        third = x[0][2] * double_matrix(det_third)
        return first - second + third
    
    if len(matrix) == 1:
        return single_matrix(matrix)
        
    elif len(matrix) == 2 and len(matrix[0]) == 2 and len(matrix[1]) == 2:
        return double_matrix(matrix)
        
    elif len(matrix) == 3 and len(matrix[0]) == 3 and len(matrix[1]) == 3 and len(matrix[2]) == 3:
        return triple_matrix(matrix)
        
    else:
        return None