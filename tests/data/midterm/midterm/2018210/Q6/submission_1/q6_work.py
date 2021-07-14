import pickle

# if the lines has "=" take the line and append it to MRT_line
# if the line does not have "=" append each one to a new list
def read_stations(f):
    d = {}
    MRT_lines = []
    MRT_stations= []
    key = ""
    stations = ""
    for line in f:
        if line[0] == "=":
            MRT_lines.append(line.strip().split("="))
            key = MRT_lines[0][1]
        else:
            MRT_stations.append(line.strip().split(","))
            stations = MRT_stations[0]
        d[key] = stations
        MRT_lines = []
        MRT_stations = []
    return d

#swap the old value as new keys and the old keys as the  new values instead
def get_stationline(mrt):
    mrt_new = {}
    for keys in mrt:
        for values in mrt[keys]:
            mrt_new[values] = [keys]
    return mrt_new


def get_interchange(stationline):
    interchanges = {}
    for keys in stationline:
        


  
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
    station_start = lines(start)
    station_end = lines(end)
    path = []
    if mrt_d[station_start] == mrt_d[station_end]:
        from mrt_d[station_start]
        path.append[start:end]
        return path
    elif: mrt_d[station_start] != mrt_d[station_end]:
            for keys in mrt_d:
            if mrt_d.keys in interchange(start) == interchange(end):
            from mrt_d[station_start]
            path.append[start:keys]
            from mrt_d[station_end]
            path.append[keys:end]
            return path
    else:
        return None
            
            
            
   
#check if both stations are on same line
# if on same line print from the the start station to the end station in order
#if not, find the interchanges first. jump to the next dictionary and continue from there. as it has only one interchange
        