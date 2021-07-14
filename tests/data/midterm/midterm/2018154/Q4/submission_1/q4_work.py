a = matrix[0][0]
b = matrix[0][1]
c = matrix[0][2]
d = matrix[1][0]
e = matrix[1][1]
f = matrix[1][2]
g = matrix[2][0]
h = matrix[2][1]
i = matrix[2][2]

def determinant(matrix):
    if len(matrix[0]) != len(matrix):
        return None
    
    elif len(matrix[0]) == 1:
        det_m1 = matrix[0][0]
        
    elif len(matrix[0]) == 2:
        det_m2 = (matrix[0][0])*(matrix[1][1])-(matrix[0][1])*(matrix[1][0])
        
    elif len(matrix[0]) == 3:
        det_m3 = a*(e*i-f*h) - b*(d*i-f*g) - c*(d*h-e*g)
            
    return determinant(matrix)
        
print (determinant[[0,3,5],[5,5,2],[3,4,3]]))