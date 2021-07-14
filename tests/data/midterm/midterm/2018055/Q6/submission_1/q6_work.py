import pickle

def read_stations(f):
    file_lines = list(f)
    file_headers = file_lines[::2]
    file_stations = file_lines[1::2]
    
    output = {}
    for line, stations in zip(file_headers, file_stations):
        line = line.strip('=')
        output[line] = [station_raw.strip()
                        for station_raw in stations.split(',')]
    
    return output

import collections as coll
def get_stationline(mrt):
    output = coll.defaultdict(list)
    for line, stations in mrt.items():
        for station in stations:
            output[station].append(line)
    
    return dict(output)

def get_interchange(stationline):
    return {k:v for k,v in stationline.items() if len(v) > 1}

def find_path(f, start, end):
    # load map
    station_raw = read_stations(f)
    stations_by_line = get_stationline(station_raw)
    interchanges = get_interchange(stations_by_line)
    
    # where is start/end?
    start_on_line = stations_by_line[start]
    end_on_line = stations_by_line[end]
    
    # Same line?
    if start_on_line == end_on_line:
        # give direct path
        index_of_start = station_raw[start_on_line].index(start)
        index_of_end = station_raw[start_on_line].index(end)
        if index_of_start < index_of_end:
            # go forwards
            return station_raw[start_on_line][index_of_start:index_of_end+1]
        else:
            # backwards
            return station_raw[start_on_line][index_of_start:index_of_end-1:-1]
    
    # Need to find a station that is on BOTH start_on_line and end_on_line
    cand_lines = set(start_on_line + end_on_line)
    # find a station that has lines thats a subset
    
    waypoint = None
    for int_station, lines in interchanges.items():
        if cand_lines >= lines:
            # Oh my god, it worked
            waypoint = int_station
    
    if waypoint is None:
        # No route
        return None
    
    # We need to find waypoint on both lines tho
    index_of_start = station_raw[start_on_line].index(start)
    index_of_end = station_raw[end_on_line].index(end)
    index_of_waypoint_on_startline = station_raw[start_on_line].index(waypoint)
    index_of_waypoint_on_endline = station_raw[end_on_line].index(waypoint)
    
    # get part on startline
    if index_of_start < index_of_waypoint_on_startline:
        # forward
        startslice = station_raw[start_on_line][index_of_start:index_of_waypoint_on_startline]
    else:
        # backward
        startslice = station_raw[start_on_line][index_of_start:index_of_waypoint_on_startline-1:-1]
    
    # get part on startline
    if index_of_waypoint_on_endline < index_of_end:
        # forward
        endslice = station_raw[end_on_line][index_of_waypoint_on_endline:index_of_end+1]
    else:
        # backward
        endslice = station_raw[end_on_line][index_of_waypoint_on_endline:index_of_end-1:-1]
    
    return startslice + endslice


  
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