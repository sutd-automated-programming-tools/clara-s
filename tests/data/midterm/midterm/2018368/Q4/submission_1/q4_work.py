def determinant(matrix):
    
    if len(matrix)!=len(matrix[0]):
        return None
    
    else:
        i=len(matrix)
        if i == 1:
            k=matrix[0][0]
    
        elif i==2:
            k=determinant2(matrix)
    
        elif i==3:
            print("what")
            k=determinant3(matrix)



        return k
    
    
def determinant2(matrix):
    m=matrix        
    j=m[0][0]*m[1][1]-m[0][1]*m[1][0]
    return j

def determinant3(matrix):
    a=matrix[0][0]
    b=-matrix[0][1]
    c=matrix[0][2]
    deta=[[matrix[1][1],matrix[1][2]],[matrix[2][1],matrix[2][2]]]
    detb=[[matrix[1][0],matrix[1][2]],[matrix[2][0],matrix[2][2]]]
    detc=[[matrix[1][0],matrix[1][1]],[matrix[2][0],matrix[2][1]]]
        
    j= a*determinant2(deta)+b*determinant2(detb)+c*determinant2(detc)
    return j
