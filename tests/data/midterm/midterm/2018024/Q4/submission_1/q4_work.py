def determinant(matrix):
    if len(matrix)==1:
        return(matrix[0])
    elif len(matrix)==2:
        x=[]
        y=[]
        x=matrix[0]
        y=matrix[1]
        if len(x)!=len(y):
            return None
        else:
            det=((x[0])*(y[1]))-((x[1])*(y[0]))
            return det
            
    elif len(matrix)==3:
        l=[]
        m=[]
        n=[]
        l=matrix[0]
        m=matrix[1]
        n=matrix[2]
        if len(l)==len(m)==len(n):
            a=l[0]
            b=l[1]
            c=l[2]
            d=m[0]
            e=m[1]
            f=m[2]
            g=n[0]
            h=n[1]
            i=n[2]
            Det= (a*((e*i)-(h*f)))-(b*((d*i)-(g*f)))+(c*((d*h)-(g*e)))
            return Det
        else:
            return None 
	pass