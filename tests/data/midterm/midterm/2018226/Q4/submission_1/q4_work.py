def determinant(matrix):
	if not len(matrix) == len(matrix[0]):
		return None
	else:
		if len(matrix) == 1:
			var1 = matrix[0][0]
			return var1
		elif len(matrix) == 2:
			return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
		elif len(matrix) == 3:
			a,b,c = matrix[0][0],matrix[0][1],matrix[0][2]
			d,e,f = matrix[1][0],matrix[1][1],matrix[1][2]
			g,h,i = matrix[2][0],matrix[2][1],matrix[2][2]
			list1 = [[e,f],[h,i]]
			list2 = [[d,f],[g,i]]
			list3 = [[d,e],[g,h]]
			return a*determinant(list1)-b*determinant(list2)+c*determinant(list3)
		else:
			return None