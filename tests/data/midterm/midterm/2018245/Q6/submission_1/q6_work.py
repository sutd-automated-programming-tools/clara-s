import pickle

def read_stations(f):
    mrt_lines = {}
    for line in f.readlines():
        line = line.strip()
        if line.startswith("="):
            line_name = line[1:-1]
            #print("line:", line_name)
        elif len(line) < 1:
            pass
        else:
            stations_name = line
            mrt_lines[line_name] = list(stations_name.split(", "))
    return mrt_lines

def get_stationline(mrt):
    output = {}
    for line_name in mrt:
        stations = mrt[line_name]
        for station in stations:
            try:
                lst = output[station]
                lst.append(line_name)
                output[station] = lst
            except:
                output[station] = [line_name]
    return output

def get_interchange(stationline):
    output = {}
    for station in stationline:
        if len(stationline[station]) > 1:
            output[station] = stationline[station]
    return output


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
'''def find_path(f,start,end):
    with open('stations_short.pickle','rb') as f:
        mrt_d = pickle.load(f)
    with open('lines_short.pickle','rb') as f:
        lines = pickle.load(f)
    with open('interchange_short.pickle','rb') as f:
        interchange = pickle.load(f)
    pass'''

def find_path(f, start, end):
    mrt = read_stations(f)
    station_lines = get_stationline(mrt)
    interchanges = get_interchange(station_lines)
    start_line = station_lines[start]
    end_line = station_lines[end]
    if start_line == end_line:
        start_index = mrt[start_line[0]].index(start)
        end_index = mrt[end_line[0]].index(end)
        if start_index > end_index:
            return mrt[start_line[0]][end_index:start_index+1][::-1]
        else:
            return mrt[start_line[0]][start_index:end_index+1]
        return mrt[start_line[0]][start_index:end_index+1]
    else:
        return None