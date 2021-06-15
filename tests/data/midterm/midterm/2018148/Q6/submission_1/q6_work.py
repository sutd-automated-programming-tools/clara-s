import pickle

def real_station(f):
    s = f.readline()
    diction = {}
    mrt = ""
    for line in s:
        if "=" in line:
            x = line.strip("=")
            mrt = x
            diction[mrt] = []
        elif mrt != "":
            y = x.split(",")
            y = [i.strip() for i in y]
            diction[mrt] = y[1:]
    return diction


def get_stationline(mrt):
    diction = {}
    for mrtline in mrt:
        for station in mrtline:
            while station not in diction:
                diction[station] = []
    for stat in diction.keys():
        station_mrt = []
        for mrtline in mrt:
            while stat in mrtline:
                station_mrt.append(mrtline)
        diction[stat] = station_mrt
    return diction

def get_interchange(stationline):
    diction = {}
    for station in stationline:
        if len(stationline[station]) > 1:
            diction[station] = stationline[station]
            
def find_path(f,start,end):
    mrt = real_station(f)
    stationline = get_stationline(mrt)
    interchange = get_interchange(stationline)
    for line in mrt:
        if start in line:
            if end in line:
                return line[line.index(start):line.index(end)+1]


  
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