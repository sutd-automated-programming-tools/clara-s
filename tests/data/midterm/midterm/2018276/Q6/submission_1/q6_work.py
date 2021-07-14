import pickle

def read_stations(f):
    file = f.readlines()
    lines = {}
    for i in range(len(file)):
        if file[i][0] == '=':
            line = file[i].strip('\n').strip('=')
            stations = list(map(lambda x: x.strip('\n').strip(' '), file[i+1].split(',')))
            lines[line] = stations
    return lines

def get_stationline(mrt):
    station_line = {}
    print(mrt)
    for line in mrt:
        for station in mrt[line]:
            if station in station_line:
                station_line[station].append(line)
            else:
                station_line[station] = [line]
    print(station_line)
    return station_line

def get_interchange(stationline):
    return {i:stationline[i] for i in stationline if len(stationline[i]) > 1}


  
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
    stationline = get_stationline(mrt_d)
    interchange = get_interchange(stationline)
    for line in mrt_d:
        if start in line:
            if end in line:
                s = None
                e = None
                for i in range(len(line)):
                    if line[i] == start:
                        s = i
                    if line[i] == end:
                        e = i
                if s < e:
                    return line[s:e+1]
                else:
                    return reversed(line[e:s+1])
    return None