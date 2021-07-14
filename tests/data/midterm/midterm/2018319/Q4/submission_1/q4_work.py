def determinant(matrix):
	if len(matrix) == 1:
		return matrix[0]
	if len(matrix)!=len(matrix[0]):
		return None
	if len(matrix)==2:
		return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
	if len(matrix)==3:
		x = matrix[0][0]*det([[matrix[1][1], matrix[1][2]],[matrix[2][1]],matrix[2][2] ])
		y = matrix[0][1]*det([[matrix[1][0], matrix[1][2]],[matrix[2][0]],matrix[2][2] ])
		z = matrix[0][2]*det([[matrix[1][0], matrix[1][1]],[matrix[2][0]],matrix[2][1] ])
		return x-y+z