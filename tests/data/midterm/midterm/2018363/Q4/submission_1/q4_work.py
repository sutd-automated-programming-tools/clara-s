def determinant(matrix):
	while n>=1 and n<=3:
           if not matrix[n][n]:
                return None
           elif len(matrix)==1:
                return matrix[0]
           elif len(matrix)==2:
                return (matrix[0][0])*(matrix[1][1])-(matrix[0][1])*(matrix[1][0])
           elif len(matrix)==3:
                return (matrix[0][0])*([(matrix[1][1])*(matrix[2][2])-(matrix[1][2])*(matrix[2][1]))-(matrix[0][1])*([(matrix[1][0])*(matrix[2][2])-(matrix[1][2])*(matrix[2][0]))+(matrix[0][3])*([(matrix[1][0])*(matrix[2][1])-(matrix[1][1])*(matrix[2][0]))
       