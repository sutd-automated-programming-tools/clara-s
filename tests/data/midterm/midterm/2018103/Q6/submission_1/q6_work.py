import pickle

def read_stations(f):
    dict1 = {}
    station = []
    data = f.readlines()
    for line in data:
        value = line.strip()
        value = value.strip('=')
        value = value.split('=')
        station.append(value)
    dict1[station[0][0]] = station[1]
    dict1[station[6][0]] = station[7]
    return dict1

def get_stationline(mrt):        
    dict2 = {}
    station = []
    for i in mrt:
        for x in mrt[i]:
            if x not in dict2:
                dict2[x] = 1
    for i in dict2:
        station = []
        for x in mrt:
            if i in mrt[x]:
                station.append(x)
        dict2[i] = station
    return dict2

def get_interchange(stationline):
    dict3 = {}
    for i in stationline:
        if len(stationline[i]) > 1:
            dict3[i] = stationline[i]
    return dict3

  
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