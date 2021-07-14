def determinant(matrix):
    n = len(matrix)
    if n<1 or n>3 : #also if the the length of each sublist don't tally,return None
        return None

    else:
        if n ==1:
            det = matrix[0][0]
        
        elif n==2:
            x =  matrix[0][0]*matrix[1][1]
            y = matrix[0][1]*matrix[1][0]
            det = x-y
        
        elif n==3:
            a = matrix[0][0]
            b = matrix[0][1]
            c = matrix[0][2]
            x = matrix[1][1]*matrix[2][2]-matrix[2][1]*matrix[1][2]
            y = matrix[1][0]*matrix[2][2]-matrix[2][0]*matrix[1][2]
            z = matrix[1][0]*matrix[2][1]-matrix[1][1]*matrix[2][0]
            det =  a*x-b*y+c*z
            
        return det
    

          
           