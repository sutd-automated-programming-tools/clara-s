def determinant(matrix):
	mat = list(matrix)
    det = []
    if len(mat) == 1:
        det = det.append(mat[0])
    
    elif len(mat) == 2:
        det = mat[1][1]*mat[0][0] - mat[1][0]*mat[0][1]
        
    elif len(mat) == 3:
        
        
    ans = str(det)
    
        