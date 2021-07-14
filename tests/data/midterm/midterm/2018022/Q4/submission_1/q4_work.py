def determinant(matrix): 
	column = len(matrix[0])
	row = len(matrix)
	if row > 3 or row != column: 
		return None
	elif row == 1:
		ans = matrix[0][0]
		return ans 
	elif row == 2: 
		return two_by_two(matrix)
	else: 
		return three_by_three(matrix)

def two_by_two(mat): 
	first_set = mat[0][0] * mat[1][1]
	second_set = mat[0][1] * mat[1][0]
	det = first_set - second_set
	return det		

def three_by_three(mat):
	first_det = ( mat[1][1] * mat[2][2] ) - (mat[1][2] * mat[2][1]) 
	one = mat[0][0] * first_det
	second_det = (mat[1][0] * mat[2][2]) - (mat[2][0] * mat[1][2])
	second = mat[0][1] * second_det
	third_det = (mat[1][0] * mat[2][1] - mat[2][0] * mat[1][1])
	third = mat[0][2] * third_det
	final_ans = one - second + third
	return final_ans