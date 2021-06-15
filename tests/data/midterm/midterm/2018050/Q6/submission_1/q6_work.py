import pickle

def read_stations(f):
    pass

def get_stationline(mrt):
    dic = {}
    lst = []
    for line in mrt:
        for x in mrt.get(line):
            lst.append(x)
    for station in lst:
        dic[station] = []
        for line in mrt:
            if station in mrt.get(line):
                dic[station].append(line)
    return dic

def get_interchange(stationline):
    dic = {}
    for station in stationline:
        for linelist in stationline.get(station):
            if len(stationline.get(station)) > 1:
                dic[station] = stationline.get(station)
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
    with open('stations_short.pickle','rb') as f:
        mrt_d = pickle.load(f)
    with open('lines_short.pickle','rb') as f:
        lines = pickle.load(f)
    with open('interchange_short.pickle','rb') as f:
        interchange = pickle.load(f)
    pass