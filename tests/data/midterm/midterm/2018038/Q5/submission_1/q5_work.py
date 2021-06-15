# MID-TERM EXAM: QUESTION 5

def nroot(n,i,num):
	x = num
	while i > 0:
		x -= f(x,n,num)/fp(x,n)
		i -= 1
	return round(x,3)

def f(x, n, num):
	return x**n - num

def fp(x,n):
	return n * x ** (n-1)

def nroot_complex(n,i,num):
	if num >= 0:
		nroot(n,i,num)
	if num < 0 and n % 2 == 0:
		return round(nroot(n,i,num * -1),3) * 1j
	if num < 0 and n % 2 != 0:
		return round(nroot(n,i,num * -1) * -1,3)