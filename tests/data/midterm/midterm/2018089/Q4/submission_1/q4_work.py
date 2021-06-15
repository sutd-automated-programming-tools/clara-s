def determinant (matrix):
    if len(matrix) >3:
        return None
    elif len(matrix) == 1:
        if len(matrix[0]) == 1:
            return matrix[0][0]
    elif len(matrix) == 2:
        if len(matrix[0]) == 1:
            return None
        else:
            deter2 = (matrix[0][0])*(matrix[1][1])- (matrix[0][1])*(matrix[1][0])
            return deter2
    else:
        deter3 = ((matrix[0][0])*((matrix[1][1])*(matrix[2][2])- (matrix[2][1])*(matrix[1][2]))) - ((matrix[0][1])*((matrix[1][0])*(matrix[2][2])- (matrix[1][2])*(matrix[2][0]))) + ((matrix[0][2])*((matrix[1][0])*(matrix[2][1])- (matrix[1][1])*(matrix[2][0])))
        return deter3