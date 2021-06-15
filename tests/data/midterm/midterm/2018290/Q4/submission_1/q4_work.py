
    
    
def determinant(matrix):
    newmatrix=[]
    newrow=[]
    length=len(matrix[0])
    det=0
    if len(matrix)==1:
        det+=int(matrix[0][0])
    elif len(matrix[0])!=len(matrix[1]):
        return None
    elif len(matrix)==2:
        det+=int(matrix[0][0])*int(matrix[1][1])-int(matrix[0][1])*int(matrix[1][0])
    else:
        
        
        for i in range(length):
            for i in range(1,length):
                newrow.append(matrix[i][:i:1])
                newrow.append(matrix[i][:i:-1])
                newmatrix.append(newrow)
            det+=(-1)**(i)*int(matrix[0][i])*determinant(newmatrix)
    return det