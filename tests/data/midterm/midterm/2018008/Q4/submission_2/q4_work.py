def determinant(matrix):
    if len(matrix)>4 or len(matrix)<1:
        return None
    for i in range(len(matrix)-1):
        if len(matrix[i])!=len(matrix[i+1]):
            return None
    if len(matrix)==1 :
        return matrix[0][0]
    if len(matrix)==2 :
        return (matrix[0][0]*matrix[1][1])-(matrix[0][1]*matrix[1][0])
    if len(matrix)==3 :
        a=matrix[0][0]
        x=(matrix[1][1]*matrix[2][2])-(matrix[2][1]*matrix[1][2])
        b=matrix[0][1]
        y=(matrix[1][0]*matrix[2][2])-(matrix[2][0]*matrix[1][2])
        c=matrix[0][2]
        z=(matrix[1][0]*matrix[2][1])-(matrix[1][1]*matrix[2][0])
        return a*x-b*y+c*z

print(determinant([[100]]))
print(determinant([[-5,-4],[-2,-3]]))
print(determinant([[2,-3,1],[2,0,-1],[1,4,5]]))
print(determinant([[0,3,5],[5,5,2],[3,4,3]]))
print(determinant([[23],[-4,4]]))
