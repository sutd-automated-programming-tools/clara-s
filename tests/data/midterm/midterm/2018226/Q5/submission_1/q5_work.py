def nroot(n,t,num):
	x = 1
	if n ==2:
		for i in range(t):
			x = x - ((x**2-num)/(x*2))
		return round(x,3)
	elif n ==3:
		for i in range(t):
			x = x - ((x**3-num)/(3*(x**2)))
		return round(x,3)
								#assumed to be always positive

def nroot_complex(n,t,num):
	x = 1
	if num >0 and num %2 ==0:
		for i in range(t):
			x = x - ((x**2-num)/(x*2))
		return round(x,3)
	elif num < 0 and num %2 == 0:
		for i in range(t):
			x = x - ((x**2-abs(num))/(x*2))
		x = round(x,3)*1j
		return complex(x)
	elif num < 0 and num%2 != 0:
		for i in range(t):
			x = x - ((x**3-num)/(3*(x**2)))
		return round(x,3)