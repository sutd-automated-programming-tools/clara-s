def one_det(matrix):
    a = matrix[0][0]
    return a

def two_det(matrix):
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    d = matrix[1][1]
    det = (a*d)-(b*c)
    return det
    pass

def three_det(matrix):
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[0][2]
    d = matrix[1][0]
    e = matrix[1][1]
    f = matrix[1][2]
    g = matrix[2][0]
    h = matrix[2][1]
    i = matrix[2][2]
    
    sub_det1 = a * two_det([[e, f], [h, i]])
    sub_det2 = b * two_det([[d, f], [g, i]])
    sub_det3 = c * two_det([[d, e], [g, h]])
    
    det = sub_det1 - sub_det2 + sub_det3
    
    return det
    
    pass
    

def determinant(matrix):
    i = 0
    j = 0
    while i < len(matrix):
        sub_mat = matrix[i]
        
        if len(matrix) == 1:
            while j < len(sub_mat):
                if len(sub_mat) == 1:
                    return one_det(matrix)
                else:
                    return None
            j += 1
        
        elif len(matrix) == 2:
            while j < len(sub_mat):
                if len(sub_mat) == 2:
                    return two_det(matrix)
                else:
                    return None
            j += 1
            
        elif len(matrix) == 3:
            while j < len(sub_mat):
                if len(sub_mat) == 3:
                    return three_det(matrix)
                else:
                    return None
            j += 1
            
        else:
            return None
        i += 1
    pass