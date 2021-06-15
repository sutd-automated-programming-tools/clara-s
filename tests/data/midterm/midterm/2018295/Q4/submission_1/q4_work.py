def determinant(matrix):
    if(len(matrix)==1):
        det=matrix[0][0]
    else:
        one=matrix[0]
        two=matrix[1]
        if(len(one)==len(two)):
            if(len(matrix)==2):
                det=(matrix[0][0]*matrix[1][1])-(matrix[0][1]*matrix[1][0])
            else:
                three=matrix[2]
                if(len(one)==len(two)==len(three)):
                    if(len(matrix)==3):
                        a=matrix[0][0]
                        b=matrix[0][1]
                        c=matrix[0][2]
                        d=matrix[1][0]
                        e=matrix[1][1]
                        f=matrix[1][2]
                        g=matrix[2][0]
                        h=matrix[2][1]
                        i=matrix[2][2]     
                        det=(a*((e*i)-(f*h)))-(b*((d*i)-(f*g)))+(c*((d*h)-(e*g)))
                else:
                    return None
        else:
            return None
    
    return det