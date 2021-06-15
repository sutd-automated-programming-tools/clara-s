# MID-TERM EXAM: QUESTION 5

def nroot(n, i,number):
	x = 1
	i = 0
	for i in range(i+10):
		numerator  = x**n-number
		denominator = (x**(n-1))*n
		x = x-(numerator/denominator)
	return round(x, 3)

def nroot_complex(n, i, num):
	if num>=0:
		return nroot(n,i,num)
	if num<0 and n%2==1:
		return -nroot(n,i,-num)
	x = nroot(n,i,-num)
	return (x*(1j))