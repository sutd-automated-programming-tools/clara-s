# MID-TERM EXAM: QUESTION 7

def decompose(pence):
	denom = 2
	ans = [1] * (pence+1)
	while denom <= pence:
		for j in range (denom, pence+1):
			ans[j] += ans[j-pence]
		denom *= 2
	return ans[-1]
#no time for slow people like me :(