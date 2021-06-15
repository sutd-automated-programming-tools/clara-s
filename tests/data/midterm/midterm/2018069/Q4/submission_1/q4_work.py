def determinant(matrix):
	def determinant(matrix):
    '''lst= []
    for elements in matrix:
        lst.append(len(elements))
    return lst'''
    if len(matrix) == 1:
        M = matrix[0]
        
        return M
    elif len(matrix) ==2:
        M = ((matrix[0][0]) * (matrix[1][1])) - ((matrix[0][1]) * (matrix[1][0]))
        return M
print(determinant([[-5,-4],[-2,-3]]))
print(determinant([[100]]))