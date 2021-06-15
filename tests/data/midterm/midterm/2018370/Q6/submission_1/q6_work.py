import pickle

def read_stations(f):
    f.readline()
    EW_stations = f.readline()
    EW_stations = EW_stations.strip(', ')
    f.readline()
    f.readline()
    EW_CG_stations = f.readline()
    EW_CG_stations = EW_CG_stations.strip(', ')
    f.readline()
    f.readline()
    NS_stations = f.readline()
    d = {'EastWestLine(EW)':EW_stations,'EastWestLine(CG)(EWCG)':EW_CG_stations, 'NorthSouthLine': NS_stations}
    return d
    
    pass

def get_stationline(mrt):
    d = {}
    for value in mrt.itervalues():
        d[value] = mrt[value].key
    pass

def get_interchange(stationline):
    d = {}
    for i in stationline:
        if len(stationline[i]) > 1:
          d[stationline[i].key] = stationline[i].val
    pass


  
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