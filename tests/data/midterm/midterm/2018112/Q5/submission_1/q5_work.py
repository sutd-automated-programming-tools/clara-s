# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):
	if num>0:
		for x in range(1,t+1):
            x**n = num
            fx = x**n - num
            ffx = n*x**(n-1)
			t_iteration = x - fx/ffx
		return t_iteration



def nroot_complex(n,t,num):
	if num<0: