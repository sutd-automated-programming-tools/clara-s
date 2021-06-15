# MID-TERM EXAM: QUESTION 5

def nroot(n,t,num):
    x0 = 1.0
    cur = 1
    while cur <= t:
        fx0 = x0**n - num
        f_x0 = (n*x0)**(n-1)
        x1 = x0 - ((fx0)/(f_x0))
        #return x1
    #print(nroot(4))
        x0 =x1
        cur +=1
    return round(x1,3)
#print(nroot(2,5,2))


def nroot_complex(n,t,num):
    if num < 0  and n%2 == 0:
        new_num = (-1)*num
        root = str(int(nroot(n,t,new_num)))+'j'
        return root
    elif num > 0:
        root = nroot(n,t,num)
        return root
    elif num < 0 and n%3 == 0:
        new_num = (-1)*(num)
        root = (nroot(n,t,new_num))*(-1)
        return int(root-1)
    else:
        None
print(nroot_complex(3,5,-8))
    