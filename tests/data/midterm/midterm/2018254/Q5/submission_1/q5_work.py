# MID-TERM EXAM: QUESTION 5

def nroot(n,i,num):
	val = 1
	for j in range(i):
		f = (val ** n) - num
		fPrime = n * (val**(n-1))
		val -= f / fPrime

	return round(val,3)

def nroot_complex(n,i,num):
	if not (abs(num)+1)%2:
		return nroot(n,i,num)*1j
	else:
		return nroot(n,i,num)