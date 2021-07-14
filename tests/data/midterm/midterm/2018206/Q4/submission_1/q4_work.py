def determinant(matrix):
    
    
    if len(matrix) == 1:
        return matrix[0][0]
    
    elif len(matrix)==2:
        for i in matrix:
            if len(i) != len(matrix):
                return None
        def det_2x2_matrix(matrix):
        
            return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
        return det_2x2_matrix(matrix)
        
    elif len(matrix) ==3:
        t = []
        t.append(matrix[1][1])
        t.append((matrix[1][2]))
        t.append(matrix[2][1])
        t.append(matrix[2][2])
        part1 = matrix[0][0]*(t[0]*t[3]-t[1]*t[2])
        
        u = []
        u.append(matrix[1][0])
        u.append((matrix[1][2]))
        u.append(matrix[2][0])
        u.append(matrix[2][2])
        part2 = matrix [0][1]*(u[0]*u[3]-u[1]*u[2])
        
        
        s = []
        s.append(matrix[1][0])
        s.append((matrix[1][1]))
        s.append(matrix[2][0])
        s.append(matrix[2][1])
        part3 = matrix[0][2]*(s[0]*s[3]-s[1]*s[2])
        
        print (t)
        print (u)
        print (s)
        
        return part1 - part2 + part3