def determinant(matrix):
    if len(matrix) != 1 or len(matrix) !=4 or len(matrix) != 9: #checking if it is square matrix within n range 
        return None 
    elif len(matrix) == 1: 
        det = matrix [0] #det is the only element inside the lst 
        return det
    
    elif len(matrix) ==4:
        
        det = (matrix[0] *matrix[3]) -( matrix[1]*matrix[2]) #det for 2x2 matrix 
        return det 
    
    elif len(matrix) ==9: 
        
        det = ((matrix[0]* ((matrix[4] *matrix[8]) -( matrix[5]*matrix[7])) - (matrix[1]* ((matrix[3] *matrix[8]) -( matrix[5]*matrix[6])) + (matrix[2] * ((matrix[3] *matrix[7]) -( matrix[4]*matrix[6])))
        return det     
	
  #syntax error for last return line, test cases for n=1 and n=2 work! 
                                                                               
                                                                               