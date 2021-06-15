import pickle

def read_stations(f):
    mixed = f.readlines()
    mrt = {}
    while '\n' in mixed:
        mixed.remove('\n')
    for i in range(len(mixed)//2):
        line = mixed[2*i].strip()
        line = line[1:-1]
        mrt[line] = mixed[2*i+1].strip().split(', ')
    return mrt
def get_stationline(mrt):
    all_stations = []
    stations = {}
    for line in mrt:
        for station in mrt[line]:
            if station not in all_stations:
                all_stations.append(station)
    for station in all_stations:
        stations[station] = []
    for station in stations:
        for line in mrt:
            if station in mrt[line]:
                stations[station].append(line)
    return stations
def get_interchange(stationline):
    interchanges = {}
    for station in stationline:
        if len(stationline[station]) > 1:
            interchanges[station] = stationline[station]
    return interchanges


  
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