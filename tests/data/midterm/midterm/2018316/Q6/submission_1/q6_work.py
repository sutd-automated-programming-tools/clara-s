import pickle

def read_stations(f):
    count = 0
    stations = {}
    for line in f:
        if count == 0:
            count = line[1:len(line)-2]
            stations[count] = ''
        elif count == 1:
            count = 0
        else:
            s = line[0:len(line)-1].strip(', ')
            stations[count] = s
            count = 1 
    return(stations)

def get_stationline(mrt):
    stations2 = {}
    for mrtname in list(mrt.keys()):
        for stationname in mrt[mrtname]:
            if mrtname not in stations2:
                stations2[mrtname] = [stationname]
            else:
                stations2[mrtname].append(stationname)
    return stations2

def get_interchange(stationline):
    stations3 = {}
    for mrtname in stationline:
        if len(stationline[mrtname] > 1):
            stations3[mrtname] = stationline[mrtname]
    return stations3

def find_path(f, start, end):
    station1 = read_stations(f)
    station2 = get_stationline(station1)
    station3 = get_interchange(station2)

    if station2[start] == startion2[end]:
        return False


  
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