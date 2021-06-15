import pickle

def read_stations(f):
    lines = []
    stations = []
    for line in f:
        line = line.strip()
#        print(line.split(", "))
        line_list = line.split(", ")
        if len(line_list) == 1:
            lines.append(line_list[0][1:-1])
        else:
            stations.append(line_list)
    for item in lines:
        if len(item) < 3:
            lines.remove(item)
    outputd = dict()
    for i in range(len(lines)):
        key = lines[i]
        outputd[key] = stations[i]
    return ( outputd)
            

def get_stationline(mrt):
    indict = mrt
    outdict = {}
    for key in mrt:
        for station in mrt[key]:
            outdict[station] = outdict.get(station,[]) + [key]
    return (outdict)

def get_interchange(stationline):
    outdict = {}
    for key in stationline:
        if len(stationline[key]) > 1:
            outdict[key] = stationline[key]
    return(outdict)

  
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