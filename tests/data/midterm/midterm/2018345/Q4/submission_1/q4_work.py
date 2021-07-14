def determinant(matrix):
    det=0
    for lst in range(len(matrix)):
        for item in range(len(lst)):
            if len(matrix)!= len(matrix[item]):
                return None
            else:
                if len(matrix)==1 and len(matrix[item])==1:
                    return matrix[item]
                elif len(matrix)==2:
                    det=(matrix[0][0]*matrix[1][2])-(matrix[0][2]-matrix[1][1])
                elif len(matrix)==3:
                    det= matrix[0][0]*((matrix[1][1]*matrix[2][2])-(matrix[1][2]*matrix[2][1]))-(matrix[0][1]*(matrix[1][0]*matrix[2][2]-matrix[2][0]*matrix[1][2]))+(matrix[0][2]*(matrix[1][0]*matrix[2][1]-matrix[2][0]*matrix[1][1]))
    return det