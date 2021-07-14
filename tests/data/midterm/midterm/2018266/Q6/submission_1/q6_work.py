import pickle

def read_station(file):
    final = {}
    mrtlines = []
    stations_temp = []
    stations = []
    for line in file:
        if line[0] == '=':
            name = line[1:-2]
            mrtlines.append(name)
        else:
            temp = line.split(", ")
            stations_temp.append(temp)
    for i in stations_temp:
        if i != ['\n']:
            stations.append(i)
    for item in range(len(mrtlines)):
        final[mrtlines[item]] = stations[item]
    for a in final:
        final[a][-1] = final[a][-1][:-1]
    return final

def get_stationline(mrt):
    final = {}
    for line in mrt:
        for station in mrt[line]:
            final[station] = line
    return final

def get_interchange(stationline):
    final = {}
    for first in stationline:
        for second in stationline:
            temp = []
            if stationline[first] == stationline[second]:
                temp.append(stationline[second])
        if len(temp) > 0:
            final[first]=temp
    return final


  
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