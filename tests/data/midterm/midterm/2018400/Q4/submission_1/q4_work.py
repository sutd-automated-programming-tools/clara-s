def minor(mat,i):
    mat=[]
    if i==0:
        r1=[mat[i+1][i+1],mat[i+1][i+2]]
        r2=[mat[i+2][i+1],mat[i+2][i+2]]
        mat.append(r1)
        mat.append(r2)
    elif i==
    
def determinant(mat):
    if len(mat) != 1 and len(mat) != 2 and len(mat) != 3:
        return None
    elif len(mat) != len(mat[0]):
        return None
    elif len(mat) == 1: 
        return mat[0][0]
    elif len(mat) == 2:
        a = mat[0][0]
        b = mat[0][1]
        c = mat[1][0]
        d = mat[1][1]
        return (a*d)-(b*c)
