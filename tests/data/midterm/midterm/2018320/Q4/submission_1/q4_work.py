def determinant(matrix):
    l=len(str(matrix))
    
    if l==1:
        det=matrix[0][0]
        return det
        
    elif l==2:
        for i in range(l):
            l1=len(str(i))
            for j in range(l1):
                det=matrix[i][j]*matrix[i+1][j+1]-(matrix[i][j+1]*matrix[i+1][j])
    
        return det                                                                                                       
        
	