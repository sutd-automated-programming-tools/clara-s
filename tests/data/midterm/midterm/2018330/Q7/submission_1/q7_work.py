# MID-TERM EXAM: QUESTION 7

def decompose(pence):
    c=1 #for make up of 1 pence definately okay
    if pence%2==0:
        c+=1
    if pence%5==0:
        c+=1
    if pence%10==0:
        c+=1
    if pence%20==0:
        c+=1
    if pence%100==0:
        c+=1
    if pence%200==0:
        c+=1
    for i in range(pence):
        pence=pence-1
                
        if pence%5==0:
            c+=1
        if pence%10==0:
            c+=1
        if pence%20==0:
            c+=1
        if pence%100==0:
            c+=1
        if pence%200==0:
            c+=1
    for i in range(pence):
        pence=pence-2
                
        if pence%5==0:
            c+=1
        if pence%10==0:
            c+=1
        if pence%20==0:
            c+=1
        if pence%100==0:
            c+=1
        if pence%200==0:
            c+=1
            
        
    return c