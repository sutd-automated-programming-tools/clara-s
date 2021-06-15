def determinant(matrix):
    det=0
    
    if len(matrix)>=4 or len(matrix)<=0:
        return None
    elif len(matrix[0])!=len(matrix[1]):
        return None
    elif len(matrix)==1:
        det=matrix[0][0]
        
    elif len(matrix)==2:
        det1=int(matrix[0][0])*int(matrix[1][1])
        det2=int(matrix[0][1])*int(matrix[1][0])
        det=det1-det2
    else:
        deta=int(matrix[1][1])*int(matrix[2][2])-int(matrix[2][1])*int(matrix[1][2])
        detb=int(matrix[0][1])*int(matrix[2][2])-int(matrix[2][1])*int(matrix[2][2])
        detc=int(matrix[0][1])*int(matrix[1][2])-int(matrix[1][1])*int(matrix[0][2])
              
        det=int(matrix[0][1])*deta-int(matrix[1][0])*detb+matrix[2][0]*detc
        
    return det        
        
