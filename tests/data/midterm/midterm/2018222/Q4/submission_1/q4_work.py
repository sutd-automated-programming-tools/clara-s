def determinant(matrix):
    length = len(matrix)
    #return length
    if length ==1 :
        ans = matrix[0][0]
        return ans
    if length==2:
        a = len(matrix[0])
        b= len(matrix[1])
        #return a,b
        if a ==b:
            ans=(matrix[0][0])*(matrix[1][1])-(matrix[0][1])*(matrix[1][0])
            return ans
        else:
            return None
    if length==3:
        a=len(matrix[0])
        b=len(matrix[1])
        c= len(matrix[2])
        if a ==b and b==c:
            ans = (matrix[0][0])*((matrix[1][1])*(matrix[2][2])-(matrix[1][2])*(matrix[2][1])) - (matrix[0][1])*((matrix[1][0])*(matrix[2][2])-(matrix[1][2])*(matrix[2][0])) + (matrix[0][2])*((matrix[1][0])*(matrix[2][1])-(matrix[1][1])*(matrix[2][0]))
            return ans
        else:
            return None