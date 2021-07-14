def determinant(M):
    ls=[]
    n=0
    for i in M:
        n+=1
        for l in i:
            ls.append(l)
    #print(n)
    #print(ls)
    #print(ls[0])

    
    if n ==1:
        ans= ls[0]
        return ans
    elif  n == 2:
        ans= ls[0]*ls[3]-ls[1]*ls[2]
        return ans      
    elif n == 3:
        ans=ls[0](ls[4]*ls[8]-ls[7]*ls[5])-ls[1](ls[3]*ls[8]-ls[5]*ls[6])+ls[2](ls[3]*ls[7]-ls[4]*ls[6])
        return ans
    elif n> 3:
        return None