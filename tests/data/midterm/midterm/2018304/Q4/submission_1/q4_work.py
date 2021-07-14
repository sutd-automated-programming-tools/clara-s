def determinant(matrix): #Must come back to this later 
    list_count = 0
    el_count = 0
    if len(matrix) > 1:
        for alist in matrix:
            list_count += 1
            for el in alist:
                el_count += 1
        if list_count != (el_count**2):
            return None
    if len(matrix) == 1:
        return matrix[0]
    elif list_count == 2:
        ad = matrix[0][0]*matrix[1][1]
        bc = matrix[1][0]*matrix[0][1]
        det = ad - bc
        return det
    elif list_count == 3:
        part1 = matrix[0][0]*(matrix[1][1]*matrix[2][2] - matrix[2][1]*matrix[1][2])
        part2 = matrix[0][1]*(matrix[1][0]*matrix[2][2] - matrix[2][0]*matrix[1][2])
        part3 = matrix[0][2]*(matrix[1][0]*matrix[2][1] - matrix[2][0]*matrix[1][1])
        det = part1 - part2 + part3
        return det
        