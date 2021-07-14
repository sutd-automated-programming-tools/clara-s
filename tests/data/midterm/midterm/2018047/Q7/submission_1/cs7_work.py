# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 16:49:31 2018

@author: xinya
"""

#7
def decompose(pence):
    p = int(pence)
    count = 0
    i = range(p, -1, -coin)
    
    return range(p, -1, -coin)
    
    
    
    
    count = 0
    i = range(0,n+1)
    i = sorted(i,reverse=True)
    if (i[0]+i[1]+i[2]+i[3]+i[4])==n:
        count +=1
        if (i[0]+i[1]+i[2]+i[3])==n:
            count+=1
            if (i[0]+i[1]+i[2])==n:
                count+=1
                if (i[0]+i[1])==n:
                    count+=1
                    if i[0]==n:
                        count+=1
    return count