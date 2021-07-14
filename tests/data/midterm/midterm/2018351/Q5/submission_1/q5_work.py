# MID-TERM EXAM: QUESTION 5
def nroot(n,i,num):
    x = num**(1/n)
    return round(x,3)
def nroot_complex(n,i,num):
    x = num**(1/n)
    for x in range(i):
        f1= x**n-num #function of x
        f2= n*x**(n-1) #function of derivative of x
        x_new = x-f1/f2 #first iteration of x
        i +=1
    
        if num>=0: #in this case, nroot_complex shoudld get the same result as nroot
            result=  
            return round(result,3)
        if num <0:
            if n%2 == 0:# in this case, nroot_complex has a result with no real part, its magnitude is the same as result of nroot when num is positive
                result= 
                return result
            elif n%2 != 0:#in this case,result is a negative real number, magnitude is the same
                result=  
                return result