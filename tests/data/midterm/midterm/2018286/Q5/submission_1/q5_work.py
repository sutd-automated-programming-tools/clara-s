# MID-TERM EXAM: QUESTION 5

def nroot(n, i, num):
	x_old = 1
	count = 0
	num = abs(num)
	while count < i:
		x_new = x_old - ((x_old**n - num) / (n*(x_old)**(n-1)))
		x_old = x_new
		count+=1

	return round(x_new,3)

def nroot_complex(n,i,num):
	if num >= 0:
		return nroot(n,i,num)

	#odd
	elif n % 2 == 1:
		return (-nroot(n,i,num))

	else:
		return (nroot(n,i,num)*1.0j)