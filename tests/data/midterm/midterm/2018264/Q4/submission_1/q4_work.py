def determinant(matrix):
    a=len(matrix)
    b=len(matrix[0])
    if a!=b:
        return None
    elif a==1 and b==1:
        return matrix[0][0]
    elif a==2 and b==2:
        det1=matrix[0][0]*matrix[1][1]
        det2=matrix[0][1]*matrix[1][0]
        det=det1-det2
        return det
    elif a==3 and b==3:
        a=matrix[0][0]
        b=matrix[0][1]
        c=matrix[0][2]
        lst1=matrix[1]
        lst2=matrix[2]
        det1=a*(lst1[1]*lst2[2]-lst1[2]*lst2[1])
        det2=b*(lst1[0]*lst2[2]-lst1[2]*lst2[0])
        det3=c*(lst1[0]*lst2[1]-lst1[1]*lst2[0])
        det=det1-det2+det3
        return det