def determinant(matrix):
    if not (len(matrix) <= 3) or not (len(matrix)>0) or (len(matrix) != len(matrix[0])):
        return None
    elif len(matrix) == 1:
        return one(matrix)
    elif len(matrix) == 2:
        return two(matrix)
    elif len(matrix) == 3:
        return three(matrix)


def one(matrix):
    return matrix[0][0]

def two(matrix):
    return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]

def three(matrix):
    matr = []
    ans = 0
    for i in range(len(matrix)):
        if i == 0:
            matr = [[matrix[1][1],matrix[1][2]], [matrix[2][1],matrix[2][2]]]
        if i == 1:
            matr = [[matrix[1][0],matrix[1][2]], [matrix[2][0],matrix[2][2]]]
        if i == 2:
            matr = [[matrix[1][0],matrix[1][1]], [matrix[2][0],matrix[2][1]]]
        ans += (-1)**(i)*matrix[0][i] * (two(matr))
    return ans