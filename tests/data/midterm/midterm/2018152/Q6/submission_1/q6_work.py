import pickle

def read_stations(f):
    lines = f.readlines()
    tlines = {}
    for x in range(len(lines)):
        if lines[x][0] == "=":
            stations = lines[x+1]
            yone = 0
            stationslist = []
            for y in range(len(stations)):
                if stations[y] == ",":
                    yone = y
                    stationslist.append(str(stations[yone:y])
            tlines[lines[x][1:-1]] = stationslist
    return tlines

def get_stationline(mrt):
    stations = []
    dic = {}
    for x in range(len(list(mrt.values()))):
        for y in range(len(list(mrt.values())[x])):
            if list(mrt.values())[x][y] not in stations:
                stations.append(list(mrt.values())[x][y])
    for z in stations:
        dic[z] = []
        for alpha in list(mrt.keys()):
            if z in mrt[alpha]:
                dic[z].append(alpha)
    return dic

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