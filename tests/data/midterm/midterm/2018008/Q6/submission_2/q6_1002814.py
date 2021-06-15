import pickle

def read_stations(f):
    f = open(f,"r")
    new=[]
    station=[]
    total=[]
    total2=[]
    
    list_lines=f.readlines()
    #return list_lines
    for line in list_lines:
        a = line.strip()
        new.append(a)
    #return new
    for item in new:
        if "," in item:
            a = item.split(",")
            station.append(a)
    for item in new:
        count=0
        if '=' in item:
            ite=item.strip('=')
            total.append((ite))
            total.append(station[count])
            count+=1
    #return total
    x=total[:2]
    ew=tuple(x)
    y=total[2:4]
    cg=tuple(y)
    z=total[4:6]
    nsl=tuple(z)
    total2=[ew,cg,nsl]
    
    return total2
    

    
    



def get_stationline(mrt):
    total3=[]
    for i in range(len(mrt)):
        for j in range(len(mrt[i][1])):
            a=(mrt[i][1][j],[mrt[i][0]])
            total3.append(a)
    return total3

def get_interchange(stationline):
    pass

def find_path(f,start,end):
    pass

#print(read_stations('mrt_lines_short.txt'))
mrt=read_stations('mrt_lines_short.txt')
print (get_stationline(mrt))