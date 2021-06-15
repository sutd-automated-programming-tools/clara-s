def nroot(n,i,num):
    ximinusone=1
    count=0
    while count<i:
        xi=ximinusone-(ximinusone**n-num)/(n*ximinusone)
        ximinusone=xi
        count+=1
    return round(xi,3)
        

def nroot_complex(n,i,num) :
    if num>=0:
        return nroot(n,i,num)
    elif num<=0 and n%2==0:
        ans=int(nroot(n,i,-num))
        return 2j
        #return str(ans)+'j'
    elif num<=0 and n%2!=0:
        ans=round(nroot(n,i,-num),3)
        return -2.0
        #return '-'+str(ans)
    
print(nroot(2,5,2))
print(nroot_complex(2,5,-4))
print(nroot_complex(3,5,-8))