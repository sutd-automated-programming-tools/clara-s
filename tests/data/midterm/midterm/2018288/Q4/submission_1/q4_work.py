def det2(matrix):
    output = (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
    return output

def determinant(matrix):
    check = len(matrix)
    
    for i in matrix:
        if len(i) != check:
            return None
    
    
    
    if check==1:
        return matrix[0][0]
    elif check==2:
        return det2(matrix)
    elif check==3:
        part0a = matrix[0][0]
        part0b = [[matrix[1][1],matrix[1][2]],[matrix[2][1],matrix[2][2]]]
        
        part1a = matrix[0][1]
        part1b = [[matrix[1][0],matrix[1][2]],[matrix[2][0],matrix[2][2]]]
        
        part2a = matrix[0][2]
        part2b = [[matrix[1][0],matrix[1][1]],[matrix[2][0],matrix[2][1]]]
        
        output = part0a*det2(part0b) - part1a*det2(part1b) + part2a*det2(part2b)
    else:
        return None
    return output