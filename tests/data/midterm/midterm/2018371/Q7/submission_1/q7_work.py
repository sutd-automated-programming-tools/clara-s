# MID-TERM EXAM: QUESTION 7

def decompose(pence):
    a = 1     #1p
    b = 2     #2p
    c = 4     #5p
    d = 11    #10p
    e = 23    #20p
    f = 56    #50p
    g = 221   #100p
    h = 441   #200p
    values = [200,100,50,20,10,5,2,1]
    numbers = [0,0,0,0,0,0,0,0]
    ways = [h,g,f,e,d,c,b,a]
    remainder = pence
    ans = 0
    for i in range(len(numbers)):
        numbers[i] += remainder // values[i]
        remainder -= numbers[i] * values[i]
        ans += numbers[i] * ways[i]
    return ans