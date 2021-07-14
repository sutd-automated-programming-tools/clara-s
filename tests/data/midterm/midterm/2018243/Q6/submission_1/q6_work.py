import pickle

def read_stations(f):
    d = {}
    count = 1
    for line in f:
        if count = 1:
            key = line.strip("=")
            key = key.strip()
            
            

def get_stationline(mrt):
    stationline = {}
    for i in mrt:
        for station in mrt[i]:
            if station not in stationline
                stationline[station] = list(i)
            else:
                stationline[station].append(i)
    return stationline
            
def get_interchange(stationline):
    d = {}
    for i in stationline:
        if len(stationline[i]) >= 2:
            d[i] = stationline[i]
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