# MID-TERM EXAM: QUESTION 5
import math

def nroot(n,t,num):
	if n == 2: 
		ans = math.sqrt(num)
		return round(ans,3)
	else: 
		ini_x = num
		for times in range(1,t+1): 
			ans = ini_x - (poly_1(ini_x) / poly_2(ini_x))
			ini_x = ans
		return round(ans, 3)	

def nroot_complex(n,t,num):
	if n % 2 == 0: 
		newnum = -num
		ans = nroot(n,t,newnum) 
		return ans , 'j'
	else:
		pass
	return round(ans, 3)

def poly_1(num): 
	ans = num**2 - num
	return ans 

def poly_2(num): 
	ans = 2 * math.sqrt(num)
	return ans

print (nroot(2,5,4))
print (nroot_complex(2,5,-4))