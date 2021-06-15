def determinant(matrix):
	lst = []
	for i in matrix:
		for j in i:
			lst.append(j)
	if len(lst)==1:
		return lst[0]
	elif len(lst)==4:
		det2 = lst[0]*lst[3]-lst[1]*lst[2]
		return det2
	elif len(lst)==9:
		det3_part1 = lst[4]*lst[8]-lst[5]*lst[7]
		det3_part2 = lst[3]*lst[8]-lst[5]*lst[6]
		det3_part3 = lst[3]*lst[7]-lst[4]*lst[6]
		det3 = lst[0]*det3_part1 - lst[1]*det3_part2 + lst[2]*det3_part3
		return det3
	else:
		return None