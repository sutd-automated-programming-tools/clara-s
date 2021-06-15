

def determinant(matrix):
	if len(matrix) == 1:
		try:
			len(matrix[0])
			return matrix[0][0]
		except:
			return matrix[0][0]
	
	for i in matrix:
		if len(i) == len(matrix):
			print("ok")
		else:
			return None

	if len(matrix) == 2:
		return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
	else:
		return (matrix[0][0] * ((matrix[1][1] * matrix[2][2]) - (matrix[1][2] * matrix[2][1]))) - (matrix[0][1] * ((matrix[1][0] * matrix[2][2]) - (matrix[1][2] * matrix[2][0]))) + (matrix[0][2] * ((matrix[1][0] * matrix[2][1]) - (matrix[1][1] * matrix[2][0])))
