# MID-TERM EXAM: QUESTION 7

def  decompose(n):
    lis = [1,2,5,10,20,50,100,200]
    for i in lis:
        if i > n:
            lis = lis[:lis.index(n)]
    count = 1
    def a(n):
        for i in lis:
            for x in range(n,-1,-i):

        if n == 0:
            return 1
        return a(n)
