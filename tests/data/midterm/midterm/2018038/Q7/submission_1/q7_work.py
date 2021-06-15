# MID-TERM EXAM: QUESTION 7

def decompose(n):
	p = [1,2,5,10,20,50,100,200]
	lenp = len(p)

	table = [[0 for x in range(lenp)] for x in range(n+1)]

	for i in range(lenp):
		table[0][i] = 1

	for i in range(1, n+1):
		for j in range(lenp):
			x = table[i - p[j]][j] if i-p[j] >= 0 else 0
			y = table[i][j-1] if j >= 1 else 0

			table[i][j] = x + y

	return table[n][lenp-1]