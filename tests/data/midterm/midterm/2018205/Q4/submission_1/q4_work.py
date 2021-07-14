
#Given base matrix A with following format:
#    [ [1,2,3]  ,  [4,5,6]  ,  [7,8,9] ]
#       j = 0       j = 1       j = 2
#Drawn out:
#       i=0  i=1  i=2
# j=0   [1   ,2   ,3]
# j=1   [4   ,5,   6]
# j=2   [7   ,8,   9]


def determinant(matrix):
    row_n = len(matrix)
    col_n = len(matrix[0])
    
    if row_n != col_n:
        return None
    else:
        if row_n == 1:
            return matrix
        elif row_n ==2:
            d = i[0]*j[1] - i[1]*[j[0]]
            return d
        elif row_n ==3:
            d = i[0]*(i[1]*j[2] - i[2]*[j[1]]) - i[1](i[2]*j[2] - i[2]*[j[2]]) + i[2](i[0]*j[1] - i[1]*[j[0]])
    
print(determinant([[23],[-4,4]])) 
print(determinant([100]))    
	