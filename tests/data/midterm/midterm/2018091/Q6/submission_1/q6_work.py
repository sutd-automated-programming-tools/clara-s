import pickle
from itertools import chain

def read_stations(f):
    dic = {}
    lines = [l.strip() for l in f.readlines() if l!='\n']
    for i in range(0, len(lines), 2):
        key = lines[i].strip('=')
        values = [station.strip() for station in lines[i+1].split(',')]
        dic[key] = values
    return dic

def get_stationline(mrt):
    dic = {}
    stations = set(chain.from_iterable(mrt.values()))
    for station in stations:
        lines = [line for line, stations in mrt.items() if station in stations]
        dic[station] = lines
    return dic

def get_interchange(stationline):
    dic = {}
    for station in stationline:
        if len(stationline[station]) > 1:
            dic[station] = stationline[station]
    return dic


  
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
    """
    with open('stations_short.pickle','rb') as f:
        mrt_d = pickle.load(f)
    with open('lines_short.pickle','rb') as f:
        lines = pickle.load(f)
    with open('interchange_short.pickle','rb') as f:
        interchange = pickle.load(f)
    """
    mrt = read_stations(f)
    for line in mrt:
        stations = mrt[line]
        if start in stations and end in stations:
            direction = 1 if stations.index(end) > stations.index(start) else -1
            return stations[stations.index(start):stations.index(end):direction] + [end]
    
    stationline = get_stationline(mrt)
    interchanges = get_interchange(stationline)
    viable_interchanges = [interchange for interchange in interchanges if 
                               set(stationline[interchange])^set(stationline[start]) and
                               set(stationline[interchange])^set(stationline[end])
                          ]
    viable_paths = [find_path(f, start, interchange)[:-1] + find_path(f, interchange, end)
                        for interchange in viable_interchanges]
    if viable_paths:
        return min(viable_paths, key=len)
    else:
        return None