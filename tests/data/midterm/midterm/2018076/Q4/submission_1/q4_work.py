def determinant(matrix):
    if len(matrix) < 1 or len(matrix) > 3: #checking for the diemensions of the matrix
        return None
    else:
        for i in range (len(matrix)+1): #looking at each row of the matrix
            for j in range (len(matrix[0])+1): #looking at each coloumn of the matrix
                #if i > j+1 and j > i+1:
                a = [i][j]*[i+1][j+1]-[i][j+1]*[i+1][j] + a
                return a
	