def check(matrix): 
    a=len(matrix[0])#d of c 
    b=0 
    for i in matrix:
        b+=1
    if a==b and (a==1 or a==2 or a==3): 
        return True
    else: 
        return None 
    




def determinant(matrix): 
    if check(matrix)==None: 
        return None 
    
    if check(matrix)== True:
        d= len(matrix[0])#check its dimension
        if d==1:
            det=matrix[0][0]
        if d==2: 
            det=det2(matrix)
        if d==3: 
            det= matrix[0][0]*det2(assignv(matrix,matrix[0][0]))-matrix[0][1]*det2(assignv(matrix,matrix[0][1]))+matrix[0][2]*det2(assignv(matrix,matrix[0][2]))
        
    return det 
    
def det2(matrix):
#     print(matrix[0][0])
    det=matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
    return det

def make2(a,b,c,d):
    return[[a,b],[c,d]]

def assignv(matrix,inputt): 
    for r in matrix:
#         print(r)
        r1=matrix[0]
        for e in r1: 
#             print(r1,e)
            e11=r1[0]
            e12=r1[1]
            e13=r1[2]
        r2=matrix[1]
        for e in r2: 
            e21=r2[0]
            e22=r2[1]
            e23=r2[2]
        r3=matrix[2]
        for e in r3: 
            e31=r3[0]
            e32=r3[1]
            e33=r3[2]
    if inputt==matrix[0][0]: 
        return (make2(e22,e23,e32,e33))
    if inputt==matrix[0][1]: 
        return (make2(e21,e23,e31,e33))
    if inputt==matrix[0][2]: 
        return (make2(e21,e22,e31,e32))
        
    