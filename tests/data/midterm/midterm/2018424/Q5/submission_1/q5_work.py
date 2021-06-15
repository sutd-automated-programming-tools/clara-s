
def nroot(n,i,num):
    x = 1
    while i > 0:
        x -= (x**n-num) / (n* x**(n-1))
        i -= 1
    return round(x,3)


# In[ ]:


def nroot_complex(n,i,num):
    if n%2 ==1:
        x = nroot(n,i,num*(-1)) * (-1)
    else:
        x = nroot(n,i,num*(-1))
        x *=  1j
    return x
