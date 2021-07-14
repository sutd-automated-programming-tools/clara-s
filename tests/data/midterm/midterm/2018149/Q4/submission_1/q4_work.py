def determinant(mat):
    n = len(mat)
    m = len(mat[0])
    #print(n,m)
    
    
    if n != m:
        return None
    
    if n == 1:
        det = mat[0][0]
        
    if n == 2:
        det = mat[0][0]*mat[1][1] - mat[1][0]*mat[0][1]
        
    if n == 3:
        #print(mat[1][1])
        a  = mat[0][0]* (mat[1][1]*mat[2][2] - mat[1][2]*mat[2][1])
        print(a)
        b  = mat[0][1]* (mat[1][0]*mat[2][2] - mat[1][2]*mat[2][0])
        c  = mat[0][2]* (mat[1][0]*mat[2][1] - mat[1][1]*mat[2][0])
        det = a - b + c
    return det