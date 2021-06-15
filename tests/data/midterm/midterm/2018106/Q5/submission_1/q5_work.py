# MID-TERM EXAM: QUESTION 5

def nroot(n,i,num):
    x=1
    iteration=1
    while iteration<=i:
        function=x**2-num
        deriv=2*x
        new_x=x-(function/deriv)
        x=new_x
        iteration +=1
    return round(x,3)

def nroot_complex(n,i,num):
    if num>0:
        x=nroot(n,i,num)
    else:
        if n%2!=0:
            x=1
            iteration=1
            while iteration<=i:
                function=x**2-num
                deriv=2*x
                new_x=x-(function/deriv)
                x=new_x
                iteration+=1
                return x
        elif n%2==0:
            pass
        
