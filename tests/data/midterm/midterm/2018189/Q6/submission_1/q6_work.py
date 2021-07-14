import pickle

def read_stations(f):
    ls = f.read().strip().splitlines()
    d = {}
    c_line = ''
    for line in ls:
        if not line: continue
        if line.startswith('='):
            c_line = line.strip('=')
            d[c_line] = []
        else:
            d[c_line].extend(line.strip().split(', '))
    return d

def get_stationline(mrt):
    d = {}
    for line, station_ls in mrt.items():
        for station in station_ls:
            if station not in d: 
                d[station] = []
            d[station].append(line)
    return d

def get_interchange(stationline):
    d ={}
    for station, line_ls in stationline.items():
        if len(line_ls) > 1:
            d[station] = line_ls.copy()
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

def find_path(f, start, end):
    stations = read_stations(f)
    stationline = get_stationline(stations)
    interchanges = get_interchange(stationline)
    
    if stationline[start] == stationline[end]:
        print('same line!')
        line = stationline[start]
        print(stations[line].index(start), stations[line].index(end))