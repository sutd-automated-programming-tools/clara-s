def determinant(matrix):
    if len(matrix) < 1 or len(matrix) >3:
        return None

    if len(matrix) == 1:
        det = 0
        for l in matrix:
            for i in l:
                det = l[0]
        return det

    if len(matrix) == 2:
        det = 0
        for l in matrix:
            list1 = matrix[0]
            list2 = matrix[1]
            if len(list1) != len(list2):
                return None
            else:
                det = (list1[0] * list2[1]) - (list1[1] * list2[0])
        return det

    if len(matrix) == 3:
        det = 0
        det1 = 0
        det2 = 0
        det3 = 0
        for l in matrix:
            list1 = matrix[0]
            list2 = matrix[1]
            list3 = matrix[2]
            if len(list1) != len(list2) or len(list1) != len(list3) or len(list2) != len(list3):
                return None
            else:
                det1 = (list1[0] * ((list2[1] * list3[2]) - (list2[2] * list3[1])))
                det2 = (list1[1] * ((list2[0] * list3[2]) - (list2[2] * list3[0])))
                det3 = (list1[2] * ((list2[0] * list3[1]) - (list2[1] * list3[0])))
                det = det1 - det2 + det3
        return det