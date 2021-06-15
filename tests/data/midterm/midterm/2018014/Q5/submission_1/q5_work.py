# MID-TERM EXAM: QUESTION 5

'''
Understanding the question:
if n > 0: nroot = nroot_complex
if n < 0 and n%2 == 0: nroot_complex gives a complex number with no real part 
                       and its magnitude = nroot when n > 0
if n < 0 and n%2 != 0: nroot_complex gives a negative real number 
                       and its magnitude is == nroot when n > 0
'''

def nroot(n, t, num): #determine the root of non-negative num
    iterations = 1
    while iterations <= t:
        #output = some code is meant to be here but I don't understand the math :/
    iterations += 1 #add one to the iteration counter until number of iterations is fulfilled
    return round(output, 3) #assuming my final variable is called output and I need to round it to 3dp
    
def nroot_complex(n, t, num): #determine the root of negative num
    #calls nroot to do the NR approximation
    if num < 0 and n % 2 == 0: #negative num and n is even
        return c.imag
    if num < 0 and n % 2 != 0: #negative num and n is odd
        return c.real
    
#my math is really bad...