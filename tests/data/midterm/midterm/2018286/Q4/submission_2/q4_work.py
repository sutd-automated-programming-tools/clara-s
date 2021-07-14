def determinant(m):
	# print(len(m))
	try:
		if len(m) <= 3 or len(m) > 0:

			l = len(m)
			for a in m:
				if len(a) != l:
					return None

			if len(m) == 1:
				return m[0][0]

			elif len(m) ==2:
				return (m[0][0]*m[1][1] - m[0][1]*m[1][0])

			elif len(m) ==3:
				mat = m[1:]
				mat1 = [list[1:] for list in mat]
				mat2 = [[list[0], list[2]] for list in mat]
				mat3 = [list[:2] for list in mat]

				output = m[0][0] * determinant(mat1) - m[0][1] * determinant(mat2) + m[0][2] * determinant(mat3)


				return output
