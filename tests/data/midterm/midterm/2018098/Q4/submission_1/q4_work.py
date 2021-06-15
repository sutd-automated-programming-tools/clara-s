
def det1(mat):
    return mat[0][0]

def det2(mat):
    ad = mat[0][0] * mat[1][1]
    bc = mat[0][1] * mat[1][0]
    ans = ad - bc
    return ans

def det3(mat):
    temp_mat2 = []
    temp_mat3 = []
    
    temp1 = [mat[1][1], mat[1][2]]
    temp2 = [mat[2][1], mat[2][2]]
    temp_mat1 = [temp1, temp2]
    temp_mat1_det = det2(temp_mat1)
    
    temp3 = [mat[0][1], mat[0][2]]
    temp4 = [mat[2][1], mat[2][2]]
    temp_mat2 = [temp3, temp4]
    temp_mat2_det = det2(temp_mat2)
    
    temp5 = [mat[0][1], mat[0][2]]
    temp6 = [mat[1][1], mat[1][2]]
    temp_mat3 = [temp5, temp6]
    temp_mat3_det = det2(temp_mat3)
    
    ans = mat[0][0] * temp_mat1_det - mat[1][0] * temp_mat2_det + mat[2][0] * temp_mat3_det
    return ans
#    temp_mat1.append()

def determinant(mat):
    sizey = len (mat[0])
    sizex = len (mat)
    if sizey != sizex:
        return None
    if sizey == 1:
        return det1(mat)
    if sizey == 2:
        return det2(mat)
    if sizey == 3:
        return det3(mat)
    return None