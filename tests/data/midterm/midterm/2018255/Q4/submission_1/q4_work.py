def determinant(lst):
    if len(lst) < 1 or len(lst) >3:
        return None          
    elif len(lst) == 1:
        return lst[0][0]
    elif len(lst) == 2:
        if len(lst[0]) != 2 or len(lst[1]) != 2:
            return None
        else:
            deter = (lst[0][0]*lst[1][1]) - (lst[0][1]*lst[1][0])
            return deter
    elif len(lst) == 3:
        part1 = lst[0][0]*(lst[1][1]*lst[2][2]-lst[2][1]*lst[1][2])
        part2 = lst[0][1]*(lst[1][0]*lst[2][2]-lst[2][0]*lst[1][2])
        part3 = lst[0][2]*(lst[1][0]*lst[2][1]-lst[2][0]*lst[1][1])
        total = part1 - part2 + part3
        return total
            