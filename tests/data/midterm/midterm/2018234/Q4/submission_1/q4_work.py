

def determinant(matrix):
    outmatrix = []
    for i in range(len(matrix[0])): #builds rows
        if range(len(matrix)) > 3 and range(len(matrix)) < 1: #if n < 1 and n > 3
            return None                                       #return None 
        else:                                                 #if condition passes 
            innermatrix = []                                   #create inner list 
            
            for j in range(len(matrix)):                         #reading columns of inner matrix 
               
                innermatrix.append(matrix[j][i])
        outmatrix.append(innermatrix)  
    return outmatrix
                