def determinant_matrix(matrix):
    determinant = ((matrix[0][0]) * (matrix[1][1])) - ((matrix[0][1])*(matrix[1][0]))
    return determinant 
    
def determinant(matrix):
    if len(matrix) < 1 or len(matrix) > 3:
        return None
    else:
        if len(matrix) == 1:
            return matrix[0][0]
        elif len(matrix) == 2:
            determinant = ((matrix[0][0]) * (matrix[1][1])) - ((matrix[0][1])*(matrix[1][0]))
            return determinant 
        elif len(matrix) == 3:
            my_list = []
            my_another_list = []
            lst = []
            first_part = [matrix[1][1],matrix[1][2]]
            first_part_2 = [matrix[2][1],matrix[2][2]]
            my_another_list.append(first_part)
            my_another_list.append(first_part_2)
            b = determinant_matrix(my_another_list)
            second_part = [matrix[1][0],matrix[1][2]]
            second_part_2 = [matrix[2][0],matrix[2][2]]
            my_list.append(second_part)
            my_list.append(second_part)
            c = determinant_matrix(my_list)
            third_part = [matrix[1][0],matrix[1][1]]
            third_part_2 = [matrix[2][0],matrix[2][1]]
            lst.append(third_part)
            lst.append(third_part_2)
            d = determinant_matrix(lst)
            return(b*matrix[0][0] + c*matrix[0][1] + d*matrix[0][2])
