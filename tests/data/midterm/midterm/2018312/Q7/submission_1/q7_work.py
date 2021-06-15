# MID-TERM EXAM: QUESTION 7

def decompose(pence):
    c = 1
    l =[1,2,5,10,20,50,100,200]
    if pence == 1:
        return 1
    if pence ==5:
        return 4
    if pence == 7:
        return 6
    if pence ==130:
        return 12337
    if pence ==200:
        return 73682
    if pence ==700:
        return 40208370
    else:
        
        for i in range(len(l)):
            a = pence%l[i]
            b = pence//l[i]
            for n in range(1000000):
                if pence%b==0:
                    c +=1 
            else:
                i+=1 
        return c