import pickle

def read_stations(f):
    x = f.readlines()
    n1 = x[0].lstrip('=')
    n1 = n1.rstrip()
    n1 = n1.rstrip('=')
    n2 = x[3].lstrip('=')
    n2 = n2.rstrip()
    n2 = n2.rstrip('=')
    n3 = x[6].lstrip('=')
    n3 = n3.rstrip()
    n3 = n3.rstrip('=')
    print(n1)
    
    d = {n1: [x[1].strip()],n2:[x[4].strip()],n3:[x[7].strip()]}
    return d
          
    

def get_stationline(mrt):
    pass
    new = {}
    for i in mrt:
        for j in mrt[i]:
            if new.get(j):
                new[j] = new.get(j), i
            else:
                new[j] = i
    return new

def get_interchange(stationline):
    new = {}
    for i in stationline:
        if len(stationline[i]) >1:
            new[i] = stationline[i]
    return new
       
        

  
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
    x = read_stations(f)
    y = get_stationline(x)
    z = get_interchange(y)
    rep = 0
    nop = 0
    for i in x:
        if start in x[i] and end in x[i]:
            return x[i]
        if start in x[i]:
            rep = 1
        if end in x[i]:
            nope = 1
    if rep == 0 or nop == 0:
        return None
        