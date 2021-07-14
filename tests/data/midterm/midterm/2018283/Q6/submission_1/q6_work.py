import pickle

def read_stations(f):
    dict_stations = {}
    for line in f:
        if line == '\n':
            line = f.readline()
        if line[0] == '=':
            line = line[1:-2]
        stations = f.readline()
        stations = stations.split(',')
        dict_stations[line] = [station.strip() for station in stations]
    return dict_stations
        
def get_stationline(mrt):
    mydict = {}
    for line, stations in mrt.items():
        for station in stations:
            #print(station)
            mydict.setdefault(station,[]).append(line)
    return mydict

def get_interchange(stationline):
    mydict = {}
    for station,lines in stationline.items():
        if len(lines) > 1:
            mydict.update({station: lines})
    return mydict


  
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