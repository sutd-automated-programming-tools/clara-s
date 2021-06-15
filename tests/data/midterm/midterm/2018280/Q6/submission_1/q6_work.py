import pickle

def read_stations(f):
    fi = open(f, 'r')
    fi = fi.read().split('\n')
    station_marker = []
    for i in range(len(fi)):
        if '=' in fi[i]:
            station_marker.append(i)
    mydict = {}
    for r in station_marker:
        y = fi[r+1].split(',')
        for l in range(len(y)):
            y[l] = y[l].strip()
        mydict[fi[r][1:-1]] = y
    
    return mydict

def get_stationline(mrt):
    f = open(mrt)
    mydict = {}
    key = mrt.keys()
    for i in key:
        y = mrt[i]
        for r in y:
            mydict.setdefault(r , {}).update([i])
    return mydict
        

def get_interchange(stationline):
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