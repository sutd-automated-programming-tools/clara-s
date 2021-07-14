def determinant(matrix):
    n=len(matrix)
    
    if n==1:
        return matrix[0][0]
    elif n==2:
        if len(matrix[0])==n and len(matrix[1])==n:
            det= (matrix[0][0])*(matrix[1][1])-(matrix[0][1])*(matrix[1][0])
            return (det)

        else:
            return None
        
    elif n==3:
        if len(matrix[0])==n and len(matrix[1])==n and len(matrix[2])==n:

            det1=(matrix[0][0])*(matrix[1][1])*(matrix[2][2])
            det2=(matrix[0][1])*(matrix[1][2])*(matrix[2][0])
            det3=(matrix[0][2])*(matrix[1][0])*(matrix[2][1])
            det4=(matrix[2][0])*(matrix[1][1])*(matrix[0][2])
            det5=(matrix[2][1])*(matrix[1][2])*(matrix[0][0])
            det6=(matrix[2][2])*(matrix[1][0])*(matrix[0][1])

            return(det1+det2+det3-det4-det5-det6)
        else:
            return None

    else:
        return None
