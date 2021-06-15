def e(M):
    a = M[0][0]*M[1][1]-M[0][1]*M[1][0]
    return a
def determinant(matrix):
    M = matrix 
    if len(M) == 1:
        d = M[0][0]
    elif len(M[0])== 2 and len(M[1])==2:
        d = M[0][0]*M[1][1]-M[0][1]*M[1][0]
   
    elif len(M[0]) == 3 and len(M[1])==3 and len(M[2])==3:
       m1,m2,m3 = reduceM(M)
       d1 = M[0][0]*e(m1)
       d2 = M[0][1]*e(m2)
       d3 = M[0][2]*e(m3)
       d = d1-d2+d3
    else:
        return None
    return d
        
def reduceM(m):
    new1= []
    new2 = []
    new3=[]
    
    for row in range(1,len(m)):
        ls = []
        for num in range(1,len(m[row])):
            ls.append(m[row][num])
        new1.append(ls)
        
        
    for row in range(1,len(m)):
            ls = []
            for num in range(0,3,2):
                ls.append(m[row][num])
            new2.append(ls)
    for row in range(1,len(m)):
            ls = []
            for num in range(0,2):
                ls.append(m[row][num])
            new3.append(ls)
    
    
    return new1,new2,new3