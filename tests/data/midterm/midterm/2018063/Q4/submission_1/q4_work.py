def determinant(matrix):
	#Is it square? Or even a matrix?
    n = len(matrix); i = 0
    while i < len(matrix):
        if len(matrix[i]) != n:
            return None
        i += 1
    #Cofactor expansion
    if n == 1:
        return matrix[0][0]
    if n == 3:
        i = 0; acc = 0
        while i < n:
            sub = [None]*(n-1)
            j = 0
            while j < n:
                
            sub[] = [matrix[1].pop(i),matrix[2].pop(i)]
            acc += ((-1)**i)*matrix[0][i]*determinant(sub)