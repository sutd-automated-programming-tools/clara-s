def read_stations(f):
    d = {}
    ls = []
    lst = f.readlines()
    for n in range(len(lst)):
        lst[n] = lst[n].split('\n')
    for m in range(len(lst)):
        for o in range(len(lst[m])):
            if lst[m][o] != '':
                ls.append(lst[m][o])
            else:
                continue
    for p in range(len(ls)//2):
        d[ls[2*p]] = [ls[2*p+1]] 
            
    return d
    
    
def get_stationline(f):
    d ={}
    d1 = {}
    a = 0
    ls = []
    lstd = list(read_stations(f).items())
    for n in range(len(lstd)):
        ls.append(lstd[n][0])
        ls.append(lstd[n][1])
    for n in range(len(ls)):
        if n //2 != 0:
            for r in range(len(ls[n])):
                ls[1] = ls[n][0].split(', ')
                
#    for n in range(len(ls)):
#        if n 
                
#    for n in range(len(ls)//2):
#        d[ls[2*n]] = ls[2*n+1]
#        
#    for m in d.values[0]:
#        d1[d.values] = d.keys
    
    return ls
