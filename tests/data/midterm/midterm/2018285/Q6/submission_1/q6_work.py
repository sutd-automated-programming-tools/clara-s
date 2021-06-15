import pickle

def read_stations(f):
    lines = {}
    stations = []
    line = None
    for i in f.readlines():
        if len(i.split()) <= 2:
            line = i.replace('=', '')
            line = line.strip()
            continue
        
        stations = i.split(', ')
        stations = [stations[i].strip() for i in range(len(stations))]
        lines[line] = stations
        stations = []
        
    return lines

def get_stationline(mrt):
    stations = {}
    for key, value in mrt.items():
        for i in value:
            stations.setdefault(i, []).append(key)
    
    return stations

def get_interchange(stationline):
    interchange = {}
    for key, value in stationline.items():
        if len(value) >= 2:
            interchange['{}'.format(key)] = value
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
    path = []
    mrt = read_stations(f)
    all_stations = get_stationline(mrt)
    interchanges = get_interchange(all_stations)
    
    line_to_ride = all_stations[start]
    line_to_stop = all_stations[end]
    interchange = None
    if line_to_ride == line_to_stop:
        for i in mrt[line_to_ride]:
            if i == start:
                continue
            while i != end:
                path.append(i)
        path.append(end)
        return path
    
    if line_to_ride != line_to_stop:
        for key, value in interchanges.items():
            for i in value:
                if i == line_to_ride or i == line_to_stop:
                    interchange = key
                else:
                    return None
        for i in mrt[line_to_ride]:
            if i == start:
                continue
            while i != interchange:
                path.append(i)
            path.append(interchange)
            
        for i in mrt[line_to_end]:
            if i == interchange:
                continue
            while i != end:
                path.append(i)
            path.append(end)
        return path