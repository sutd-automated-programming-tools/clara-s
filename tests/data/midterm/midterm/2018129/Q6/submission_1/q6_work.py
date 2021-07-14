import pickle

def read_stations(f):
    outp = {}
    for line in f:
        if line[0] is '=':
            mrtline = line.strip('=').rstrip('=\n')
            line = f.readline()
            stations = line.rstrip('\n').split(', ')
            outp[mrtline] = stations
    return outp


def get_stationline(mrt):
    outp = {}
    for line,station_list in mrt.items():
        for station in station_list:
            if station in outp:
                outp[station].append(line)
            else:
                outp[station] = [line]
    return outp

def get_interchange(stationline):
    outp = {}
    for station,line in stationline.items():
        if len(line) > 1:
            outp[station] = line
    return outp



  
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
    
    for stations_list in mrt_d.values():
        if start in stations_list and end in stations_list:
            startno = stations_list.index(start)
            endno = stations_list.index(end)
            if startno < endno:
                return stations_list[startno:endno+1]
            else:
                return stations_list[startno:endno+1:-1]
