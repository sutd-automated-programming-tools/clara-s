# MID-TERM EXAM: QUESTION 5
#Q5
def nroot(n,i,num):

	fx=num**n
	x=num
	while i>0:
		i-=1
		print (i)
		x=nroot(n, i-1, num)-(fx/2*num)
		print (x)
	return x

print (nroot(2,5,2))

def nroot_complex(n,i,num):
	pass