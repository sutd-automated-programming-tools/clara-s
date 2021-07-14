import pickle

def read_stations(f):
    
    lst = [] 
    mrt = {}
     
    for line in f:
        line = line.strip("\n")
        lst.append(line)
         
    
    mrt['EastWestLine (EW)']= lst[1:2]  
    mrt['EastWestLine (CG)']=lst[4:5]
    mrt['NorthSouthLine'] = lst[7:8]
    
    return mrt 

def get_stationline(mrt):
    d = {}
    for values in mrt.values():
        for i, j in mrt.items():
            d[j]=i
            
    return d 