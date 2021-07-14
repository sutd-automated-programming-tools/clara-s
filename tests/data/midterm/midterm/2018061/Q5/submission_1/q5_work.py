# MID-TERM EXAM: QUESTION 5

def nroot(n,i,num):
    j = 0
    number = num
    while j<i+1:
        number = number - (((number**n)-num)/(n*(number)**(n-1)))
        j +=1
    return round(number,3)
def nroot_complex(n,i,num):
    if num >0:
        return(nroot(n,i,num))
    else:
        if n % 2 !=0:
            return -(nroot(n,i,abs(num)))
        else:
            a = abs(num)
            b = nroot(n,i,a)
            c = b*1j
            return c