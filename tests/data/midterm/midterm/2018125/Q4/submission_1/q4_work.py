def determinant_matrix(matrix):
    for i in matrix:
        lst=[]
        if len(i)==1:
            return i[0]
        if len(i)!=len(i[1]):
            return None
    
        else:
            for innerlist in i:
                a=innerlist[0]
                b=innerlist[1]
                lst.append(a)
                lst.append(b)
            a=lst[0][0]
            b=lst[1][1]
            c=lst[0][1]
            d=lst[1][0]
            det=int(a)*int(d)- int(b)-int(c)
        return det
                
                