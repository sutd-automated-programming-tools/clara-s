def determinant(matrix):
    if len(matrix)>1:
        if len(matrix[1])!=len(matrix[0]):
            print(None)
            return None
        else:
            if (len(matrix[1])==2):
                det=matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
                print(det)
                return det
            elif (len(matrix[1])==3):
                det=(matrix[0][0]*((matrix[1][1]*matrix[2][2])-(matrix[1][2]*matrix[2][1])))-(matrix[0][1]*((matrix[1][0]*matrix[2][2])-(matrix[1][2]*matrix[2][0])))+(matrix[0][2]*((matrix[1][0]*matrix[2][1])-(matrix[1][1]*matrix[2][0])))
                print(det)
                return det
    else:
        det=matrix[0][0]
        print(det)
        return det