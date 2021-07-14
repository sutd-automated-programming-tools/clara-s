def nroot(n, i, num): #num is non negative
    x0 = 1
    for j in range(i):
        f = x0**n - num
        fd = n*x0**(n-1)
        x1 = x0 - (f/fd)
        x0 = x1
    return round(x1,3)
    
print(nroot(3,5,8))


def nroot_complex(n, i, num):
    if num >= 0:
        return nroot(n,i,num)
    
    if num<0 and n%2==0:
        temp_num = -num
        mag = nroot(n,i,temp_num)
        return mag*1j
    
    if num<0 and n%2!=0:
        temp_num = -num
        mag = nroot(n,i,temp_num)
        return -mag

print(nroot_complex(3,5,-8))