def determinant(matrix):
	pass
def detminant(matrix):
    i=list()
    for i in matrix :
        for j in i:
            if len(i)==len(j)==1:
                det=sum(j)
                return det
            #elif len(i)==len(j)==2:
                #det=                   
                
            #elif len(i)==len(j)==3:
                #det=
            else:
                return "None"