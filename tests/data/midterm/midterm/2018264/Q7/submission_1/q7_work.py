# MID-TERM EXAM: QUESTION 7

def decompose(pence):
    a=int(pence/200)
    if a!=0:
        a=a*2*2*2.5*2*2*2.5*2
    else:
        a=1
    b=pence%200
    b=int(b/100)
    if b!=0:
        b=b*2*2*2*2*2*2
    else:
        b=1
    c=(pence%200)%100
    c=int(c/50)
    if c!=0:
        c=c*2*2*2*2*2
    else:
        c=1
    d=((pence%200)%100)%50
    d=int(d/20)
    if d!=0:
        d=d*2*2*2*2
    else:
        d=1
    e=(((pence%200)%100)%50)%20
    e=int(e/10)
    if e!=0:
        e=e*2*2*2
    else:
        e=1
    f=((((pence%200)%100)%50)%20)%10
    f=int(f/5)
    if f!=0:
        f=f*2*2
    else:
        f=1
    g=(((((pence%200)%100)%50)%20)%10)%5
    g=int(g/2)
    if g!=0:
        g=g*2
    else:
        g=1
    if pence!=1 or pence!=2 or pence!=5 or pence!=10 or pence!=20 or pence!=50 or pence!=100 or pence!=200:
        
        ans=a*b*c*d*e*f*G
    else
        ans=a*b*c*d*e*f*G-1
    return ans
    