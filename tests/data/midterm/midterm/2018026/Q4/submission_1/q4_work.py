def determinant(matrix):
    n=len(matrix)
    if n>4:
        return None
    for i in matrix: 

        if len(i)!=n:
            return None
    if n==1:
        det=matrix[0][0]
        return det
    if n==2:
        ad=matrix[0][0]*matrix[1][1]
        bc=matrix[0][1]*matrix[1][0]
        det=ad-bc
        return(det)
    if n==3:
        ad1=matrix[1][1]*matrix[2][2]
        bc1=matrix[2][1]*matrix[1][2]
        det1=ad1-bc1
        x1=matrix[0][0]*det1
        print(x1)

        
        ad2=matrix[1][0]*matrix[2][2]
        bc2=matrix[1][2]*matrix[2][0]
        det2=ad2-bc2
        x2=matrix[0][1]*det2
        print(x2)
        
        ad3=matrix[1][0]*matrix[2][1]
        bc3=matrix[2][0]*matrix[1][1]
        det3=ad3-bc3
        x3=matrix[0][2]*det3
        print(x3)

        ans=x1-x2+x3
        return (ans)