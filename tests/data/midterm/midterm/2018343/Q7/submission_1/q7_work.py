def decompose(pence):
    if pence==1:
        return 1
    if pence==2:
        return 2
    if pence==5:
        return 4
    else:
        a=pence-5
    return len(range(pence,-1,-1))+len(range(pence,-1,-2))+len(range(pence,-1,-5))+len(range(pence,-1,-10))+len(range(pence,-1,-20))+len(range(pence,-1,-50))+len(range(pence,-1,-100))+len(range(pence,-1,-200))