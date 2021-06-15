def determinant(list1):
    if len(list1) != len(list1[0]):
        return None
    else:
        if len(list1) == 1:
            return list1[0][0]
        elif len(list1) == 2:
            res = list1[0][0]*list1[1][1] - list1[0][1]*list1[1][0]
            return res
        elif len(list1) == 3:
            list2 = [[list1[1][1],list1[1][2]],[list1[2][1],list1[2][2]]]
            list3 = [[list1[1][0],list1[1][2]],[list1[2][0],list1[2][2]]]
            list4 = [[list1[1][0],list1[1][1]],[list1[2][0],list1[2][1]]]
            res = list1[0][0]*determinant(list2) - list1[0][1]*determinant(list3) + list1[0][2]*determinant(list4)
            return res
        else:
            return None
