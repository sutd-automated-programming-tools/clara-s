# MID-TERM EXAM: QUESTION 5

def nroot(n,i,num):
    val1=1
    
    count=0
    while count<i:
        var= val1**n - num
        varder= n*(val1*(n-1))
        val1= val1- (var/varder)
        count+=1
    return round(val1,3)
def nroot_complex(n,i,num):
    if num>=0:
        return nroot(n,i,abs(num))
    elif abs(n)%2==0:
        a= nroot(n,i, abs(num))
        b=complex(0,a)
        return b
    else:
        b= nroot(n,i, abs(num))
        b2=-1*b
        return b2
        