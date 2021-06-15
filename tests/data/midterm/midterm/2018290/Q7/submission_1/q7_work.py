
def decompose(pence):
    lst=[1,2,5,10,20,50,100,200]
    ans = 0   
    for i in lst: 
        for m in range(400,-1,200):
            if i*m == pence:
                            ans += 1
    return ans