def determinant(matrix):
	if len (matrix)!=len(matrix[0]) or len(matrix)<1 or len(matrix)>3:
		return None
	else:
		if len(matrix)==1:
			return matrix[0]
		elif len(matrix)==2:
			return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
		elif len (matrix)==3:
			total=[]
			detA=matrix[1][1]*matrix[2][2]-matrix[1][2]*matrix[2][1]
			total.append(matrix[0][0]*detA)
			detB=matrix[1][0]*matrix[2][2]-matrix[1][2]*matrix[2][0]
			total.append(-matrix[0][1]*detB)
			detC=matrix[1][0]*matrix[2][1]-matrix[1][1]*matrix[2][0]
			total.append(matrix[0][2]*detC)
		out=sum(total)
	return out
