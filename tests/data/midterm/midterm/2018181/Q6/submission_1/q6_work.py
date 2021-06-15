import pickle

def read_stations(f):
    s = f.readline()
    d={}
    l=[]
    while s:
        s1=s.strip()
        s2=s1.split(',')
        l.append(s2)
        s=f.readline()
    c1=l.index([['=EastWestLine (EW)=']])
    c2=l.index([['=EastWestLine (CG)=']])
    c3=l.index([['=NorthSouthLine=']])
                
    d['EastWestLine','(EW)']=l[c1+1]
    d['EastWestLine (CG)']=l[c2+1]
    d['NorthSouthLine']=l[c3+1]
    return d

def get_stationline(mrt):
    c={}
    for h in mrt.values():
        for z in h:
            c[z]=[]
    for i in mrt.keys():
        for j in mrt[i]:
            c[j].append(i)
    return c

def get_interchange(stationline):
    a={}
    for e in stationline.keys():
        if len(stationline[e])>=1:
            a[e]=stationline[e]
    return a
            


  
##### Testing get_stationline ###########
with open('stations_short.pickle','rb') as f:
    mrt_d = pickle.load(f)
    print(get_stationline(mrt_d))
#########################################

##### Testing get_interchange ###########
with open('lines_short.pickle','rb') as f:
    lines = pickle.load(f)
    print(get_interchange(lines))
#########################################

###### Testing find_path ################
# You can use these three variables in your find_path
# to get the output of
# mrt_d = read_station()
# lines = get_stationline()
# interchange = get_interchange()
# even if you haven't finished these three functions
#########################################
def find_path(f,start,end):
    with open('stations_short.pickle','rb') as f:
        mrt_d = pickle.load(f)
    with open('lines_short.pickle','rb') as f:
        lines = pickle.load(f)
    with open('interchange_short.pickle','rb') as f:
        interchange = pickle.load(f)
    