def byone(lerst):
    
    return lerst[0][0]

def bytwo(lerst):

    a = lerst[0][0]
    b = lerst[0][1]
    c = lerst[1][0]  
    d = lerst[1][1]

    return ((a*d)-(b*c))      

def bythree(lerst):
    
    listone = [ [lerst[1][1],lerst[1][2]] , [lerst[2][1],lerst[2][2]]]
    one = (lerst[0][0]) * (bytwo(listone))
    
    listtwo = [ [lerst[1][0],lerst[1][2]] , [lerst[2][0],lerst[2][2]]]
    two = (lerst[0][1]) * (bytwo(listtwo))
    
    listthree = [ [lerst[1][0],lerst[1][1]] , [lerst[2][0],lerst[2][1]]]
    three = (lerst[0][2]) * (bytwo(listthree))
    
    return (one - two + three)

def determinant(matrix):
    
    #barriers to entry
    for i in matrix:
        
        if len(i) != len(matrix):
            
            return None
    
    if len(matrix) < 1 or len(matrix) > 3:
        
        return None
    
    #caseone
    if len(matrix) == 1:
        
        return (byone(matrix))
    
    #casetwo
    if len(matrix) == 2:
        
        return (bytwo(matrix))
    
    #casethree
    if len(matrix) == 3:
        
        return (bythree(matrix))
    
    
    


