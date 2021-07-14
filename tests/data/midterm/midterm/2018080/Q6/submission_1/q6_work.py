import pickle

def read_stations(f):
    stationdict = {}
    
    station = f.read()
    stationlst = station.split('=')
    

def get_stationline(mrt):
    station_lines = {}
    
    for key in mrt:
        station = mrt[key]
        if station not in station_lines:
            station_lines[station] = [key]
        else:
            station_lines[station].append(key)
    return station_lines

def get_interchange(stationline):
    interchange = {}
    for entry in stationline:
        if len(entry)>=2:
            interchange.append(entry)
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
    with open('stations_short.pickle','rb') as f:
        mrt_d = pickle.load(f)
    with open('lines_short.pickle','rb') as f:
        lines = pickle.load(f)
    with open('interchange_short.pickle','rb') as f:
        interchange = pickle.load(f)
    pass