def determinant(matrix):
    if( len(matrix) != len(matrix[0]) ):
        for i in matrix:
            if( matrix.count(list) % len(matrix[0]) != 0 ):
               return None
    else:
        for cube in matrix:
            if( len(matrix) == 1 ):
                det = matrix[0]
                return det
               
            elif( len(matrix) == 2 ):
                det = ( matrix[0][0] * matrix[1][1] ) - ( matrix[0][1] * matrix [1][0] )
                return det
                 
            elif( len(matrix) == 3 ):
                de1 = (  matrix[0][0] * ( matrix[1][1] * matrix[2][2] ) - ( matrix[1][2] * matrix [2][1] )  )
                de2 = (  matrix[0][1] * ( matrix[1][0] * matrix[2][2] ) - ( matrix[1][2] * matrix [2][0] )  )
                de3 = (  matrix[0][2] * ( matrix[1][0] * matrix[2][1] ) - ( matrix[1][1] * matrix [2][0] )  )
                det = de1 - de2 - de3
                return det 
        
        