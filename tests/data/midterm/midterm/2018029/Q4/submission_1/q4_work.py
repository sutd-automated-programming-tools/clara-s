'''def determinant(matrix):
	pass'''
def determinant(matrix):

    if len(matrix)!= range(len([1,2,3])):
        return None
        
    elif len(matrix)==1 and (len(matrix[0]))**0.5!=1:

       return None
    elif len(matrix)==2 and (len(matrix[0])+len(matrix[1]))**0.5!=2:

        return None
    elif len(matrix)==3 and (len(matrix[0])+len(matrix[1])+len(matrix[2]))**0.5!=3:

        return None
    elif len(matrix)==1:
        det=matrix[0]
        return det
    elif len(matrix)==2:
        a=matrix[0][0]
        b=matrix[0][1]
        c=matrix[1][0]
        d=matrix[1][1]
        det=a*d-b*c
        return det
    elif len(matrix)==3:
        A=(matrix[0][0])*(matrix[1][1]*matrix[2][2]-matrix[1][2]*matrix[2][1])
        B=(matrix[0][1])*(matrix[1][0]*matrix[2][2]-matrix[1][2]*matrix[2][0])
        C=(matrix[0][2])*(matrix[1][0]*matrix[2][1]-matrix[1][1]*matrix[2][0])
        det=A-B+C
        return det
      