import pickle

def read_stations(f):
    d = {}
    for line in f:
        if line[0] == '=':
            branch = line.strip().strip('=')
            d[branch] = []
        else:
            stations = line.strip().split(', ')
            d[branch].extend(stations)
    for branch in d:
        for station in d[branch]:
            if station == '':
                d[branch].remove(station)
    return(d)

def get_stationline(mrt):
    #mrt = d
    all_stations= []
    for branch in mrt:
        for station in mrt[branch]:
            if station not in all_stations:
                all_stations.append(station)
    stationline = {}
    for station in all_stations:
        if station not in stationline:
            stationline[station] = []
        for branch in mrt:
            if station in mrt[branch]:
                stationline[station].append(branch)
    return stationline

def get_interchange(stationline):
    interchange = {}
    for station in stationline:
        if len(stationline[station]) > 1:
            interchange[station] = stationline[station]
    return interchange


  
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
    
    mrt_d = read_stations(f)
    lines = get_stationline(mrt_d)
    interchange = get_interchange(lines)
    
    start_branches = lines[start]
    print(start_branches)
    for branch in start_branches:
        if end in mrt_d[branch]:
            start_index = mrt_d[branch].index(start)
            print(start_index)
            end_index = mrt_d[branch].index(end)
            print(end_index)
            if start_index < end_index:
                return mrt_d[branch][start_index:end_index+1]
            else:
                temp = mrt_d[branch][::-1]
                start_index = len(temp) - start_index - 1
                end_index = len(temp) - end_index - 1
                return temp[start_index:end_index+1]