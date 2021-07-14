def determinant(matrix):
    if len(matrix)<1 or len(matrix)>3:
        return None
    else:
        for i in matrix:
            #print (i)
            if len(i)!=len(matrix):
                return None
            elif len(matrix)==1:
                return i[0]
            elif len(matrix)==2:
                return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
            elif len(matrix)==3:
                a = matrix[0][0]
                b = matrix[0][1]
                c = matrix[0][2]
                aa= a*matrix[1][1]*matrix[2][2]-matrix[2][1]*matrix[1][2]
                bb= b*matrix[1][0]*matrix[2][2]-matrix[2][0]*matrix[1][2]
                cc= c*matrix[1][0]*matrix[2][1]-matrix[2][0]*matrix[1][1]
                return aa-bb+cc