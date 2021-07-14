import pickle

def read_stations(f):
    text = f.readlines()
    result = {}
    mrt_lines = []
    mrt_stations = []
    for line in text:
        if len(line) > 3 and line[0] != '=':
            mrt_stations.append(line)
        if len(line) > 3 and line[0] == '=':
            mrt_lines.append(line.strip('\n').strip('='))
    for i in range(len(mrt_lines)):
        result[mrt_lines[i]] = mrt_stations[i].strip('\n').split(', ')
    return result

def get_stationline(mrt):
    result = {}
    all_lines = list(mrt.keys())
    all_stations = []
    for line in all_lines:
        all_stations.extend(mrt[line])
    for station in all_stations:
        part_of = []
        for line in all_lines:
            if station in mrt[line]:
                part_of.append(line)
        result[station] = part_of
    return result

def get_interchange(stationline):
    result = {}
    for station in stationline:
        if len(stationline[station]) > 1:
            result[station] = stationline[station]
    return result

  
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