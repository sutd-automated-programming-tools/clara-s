# MID-TERM EXAM: QUESTION 5

#QN 5
def nroot(n,i,num):
    
    for i in range(n): #loop i times
        ## the part where the code is suppose to work or something
        x = -10000
        fx = x**n - num
        fx1 = n*x
        x = x - (fx/fx1)
        
    return x 
print(nroot(1,1,1))
def nroot_complex(n,i,num):
    #call function nroot
    #code magically works