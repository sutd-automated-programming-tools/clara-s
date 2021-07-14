def determinant(matrix):
    l=len(matrix)
    if l<1 or l>3:
        return None
    for i in matrix:
        if len(i)!=l:
            return None
    if l==1:
        det=int(matrix[0][0])
    elif l==2:
        det=int(matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0])
    elif l==3:
        a=int(matrix[0][0])
        b=int(matrix[0][1])
        c=int(matrix[0][2])
        d1=[]
        d2=[]
        d3=[]
        d1.append(matrix[1][1:])
        d1.append(matrix[2][1:])
        d2.append([matrix[1][0],matrix[1][2]])
        d2.append([matrix[1][0],matrix[2][2]])
        d3.append(matrix[1][:1])
        d3.append(matrix[2][:1])
        det=a*determinant(d1)-b*determinant(d2)+c*determinant(d3)
    return det