import pickle

def read_stations(f):
    line = f.readline().strip().split()
    result = {}
    with f:
        while len(line)>0:
            key = line.strip("=")
            line = f.readline().strip().split(", ")
            temp = []
            while len(line)> 0:
                temp.extend(line)
                line = f.readline().strip().split(", ")
            result[line] = temp
            line = f.readline().strip().split()

    return result

def get_station(mrt):
    result = {}
    for line, stations in mrt.items():
        for station in stations:
            try:
                if len(result[station]) > 0:
                    result[station].append(line)
            except:
                result[station] = line

    return result

def get_interchange(stationline):
    result = {}
    for station, line in stationline.items():
        if len(line)>1:
            result[station]= line
    
    return result


  
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

    all_stations = read_stations(f)
    station = get_station(mrt)
    interchange = get_interchange(stationline)
    result = []
    start_idx = []

    start_line = station[start]
    end_line = station[end]
    for line, stations in all_stations:
        if start in stations and end in stations:
            result = stations[stations.index(start):stations.index(start)]

                 
    return result