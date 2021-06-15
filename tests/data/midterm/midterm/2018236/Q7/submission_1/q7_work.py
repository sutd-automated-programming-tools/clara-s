# MID-TERM EXAM: QUESTION 7

def decompose(p):
    ans = 0
    if n == 1:
        return 1
    if n>200:
        ans += decompose(p-200)
        ans += decompose(p-100)
        ans += decompose(p-50)
        ans += decompose(p-20)
        ans += decompose(p-10)
        ans += decompose(p-5)
        ans += decompose(p-2)
        ans += decompose(p-1)
    elif n > 100:
        ans += decompose(p-100)
        ans += decompose(p-50)
        ans += decompose(p-20)
        ans += decompose(p-10)
        ans += decompose(p-5)
        ans += decompose(p-2)
        ans += decompose(p-1)
    elif n > 50:
        ans += decompose(p-50)
        ans += decompose(p-20)
        ans += decompose(p-10)
        ans += decompose(p-5)
        ans += decompose(p-2)
        ans += decompose(p-1)
    elif 
        
        