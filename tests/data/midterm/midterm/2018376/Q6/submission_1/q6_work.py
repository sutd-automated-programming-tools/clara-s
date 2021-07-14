import pickle

def read_stations(f):
    d = {}
    for line in f:
        if "=" in line:
            key = line.strip('=')[:-2]
            d[key]=[]
        else:
            treated=line.strip()
            lsts = treated.split(',')
            print(lsts)
            d['EastWestLine (EW)']=lsts
        
    return d

def get_stationline(mrt):
    d = {}
    for key in mrt:
        for station in key:
            if station not in d:
                d[station] = [key]
            else:
                d[station].append(key)
    return d

def get_interchange(stationline):
    d = {}
    for key in stationline:
        count = 0
        for station in key:
            count +=1
        if count >= 2:
            d[key]=stationline[key]
    return d


  
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
    pass