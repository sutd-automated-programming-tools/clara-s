# MID-TERM EXAM: QUESTION 7

def decompose(pence):

    ans=0
    if pence <= 0:
        ans=0
    if pence %1 == 0:
        ans+=1
    if pence %2==0:
        if pence/2<1:
            ans+=1
        elif pence/2>=1:
            ans+=(pence/2)
            
    if pence %5 == 0:
                
         if pence/5<1:
            ans+=1
         elif pence/5>=1:
            ans+=(pence/5)
    if pence%10==0:
         ans+=1
    if pence%20==0:
         ans+=1
    return ans