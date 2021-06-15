def determinant(matrix):
    a=len(matrix) #get n by n of both matrices
    b=len(matrix[0])
    if  a == b and a <=3 and a>=1 and b <=3 and b>=1:
        if a == 1 and b == 1:
            det=matrix[0]
            
        elif a==2 and b==2:
            det=(matrix[0][0]*matrix[1][1])-(matrix[0][1]*matrix[1][0])
            
        elif a==3 and b==3:
            det00=(matrix[1][1]*matrix[2][2])-(matrix[2][1]*matrix[1][2])
            det10=(matrix[0][1]*matrix[2][2])-(matrix[2][1]*matrix[0][2])
            det20=(matrix[0][1]*matrix[1][2])-(matrix[1][1]*matrix[0][2])
            
            
            det=((matrix[0][0])*(det00))-((matrix[1][0])*(det10))+((matrix[2][0])*(det20))
            
    else:
        det=None
        
    return det

