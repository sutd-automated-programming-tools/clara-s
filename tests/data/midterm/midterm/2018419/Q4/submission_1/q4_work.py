def determinant(matrix):
    count = len(matrix)
    if count==1:
        ans=0
        ans=sum(matrix[0])
        return ans
    elif count==2:
        if (len(matrix[0])==2 and len(matrix[1])==2):
            total = (matrix[0][0]*matrix[1][1] )- (matrix[0][1]*matrix[1][0])
            return total
        else:
            return None
    elif count==3:
        n1=len(matrix[0])
        n2=len(matrix[1])
        n3=len(matrix[2])
        if (n1==3 and n2==3 and n3==3):
            a=sum(matrix[0][0])
            b=sum(matrix[0][1])
            c=sum(matrix[0][2])
            d=sum(matrix[1][0])
            e=sum(matrix[1][1])
            f=sum(matrix[1][2])
            g=sum(matrix[2][0])
            h=sum(matrix[2][1])
            i=sum(matrix[2][2])
            de=a((e*i)-(f*h))-b((d*i)-(f*g))+c((d*h)-(e*g))
            return de
        else:
            None
    else:
        return None
        