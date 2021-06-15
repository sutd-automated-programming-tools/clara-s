def determinant(matrix):
    
    width = len(matrix);
    height = len(matrix[0]);
    
    if(width!=height):
        return None;
    
    
    if(width == 1):
        return matrix[0][0];
    
    if(width == 2):
        
        return (matrix[0][0]*matrix[1][1]) - (matrix[0][1]*matrix[1][0]);
    
    if(width == 3):
        
        return (matrix[0][0] * determinant([[matrix[1][1],matrix[1][2]],[matrix[2][1],matrix[2][2]]]))-(matrix[0][1] * determinant([[matrix[1][0],matrix[1][2]],[matrix[2][0],matrix[2][2]]]))+(matrix[0][2] * determinant([[matrix[1][0],matrix[2][0]],[matrix[1][1],matrix[2][1]]]));