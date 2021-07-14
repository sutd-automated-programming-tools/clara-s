def detof2x2(matrix):
    det=((matrix[0][0])*(matrix[1][1]))-((matrix[0][1])*(matrix[1][0]))
    return(det)

def determinant(matrix):
    if len(matrix)!= len(matrix[0]) or len(matrix)<1 or len(matrix)>3:
        return None
    elif len(matrix)==1:
        return(matrix[0][0])
    elif len(matrix)==2:
        return(detof2x2(matrix))
    elif len(matrix)==3:
        a=matrix[0][0]
        b=matrix[0][1]
        c=matrix[0][2]
        d=matrix[1][0]
        e=matrix[1][1]
        f=matrix[1][2]
        g=matrix[2][0]
        h=matrix[2][1]
        i=matrix[2][2]
        det=(a*(detof2x2([[e,f],[h,i]])))-(b*(detof2x2([[d,f],[g,i]])))+(c*(detof2x2([[d,e],[g,h]])))
        return(det)
        
        
        
