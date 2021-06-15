from copy import deepcopy as d
def determinant(matrix):
    m = d(matrix)
    n = len(matrix)
    boo= False
    if 1<=n and n <= 3:
        for mat in matrix:
            if len(mat) == len(matrix):
                boo = True
            while boo:    
                if n == 1:
                    ans = m[0][0]
                elif n == 2:
                    ans = m[0][0]* m[1][1] - m[0][1]*m[1][0]
                else:
                    ans = m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])-m[0][1]*(m[1][0]*m[2][2]-m[1][2*m[2][0]])+ m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0])
                return ans
        else:
            return None
    else:
        return None