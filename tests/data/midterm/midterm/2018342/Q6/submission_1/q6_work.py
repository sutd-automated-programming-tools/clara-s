import pickle

def read_stations(f):
    out = {}
    content = open(f, "r")
    currentline = ""
    for i in content.readlines():
        line = i.strip()
        if line[0] == "=":
            currentline = line[1:len(line)-1]
            out[currentline] = []
        else:
            for j in line.split(", "):
                out[currentline].append(j)
    return out

def get_stationline(mrt):
    out = {}
    for line in mrt:
        for station in mat[line]:
            out[station] = []
            if station in mrt["EastWestLine (EW)"]:
                out[station].append("EastWestLine (EW)")
            elif station in mrt["NorthSouthLine"]:
                out[station].append("NorthSouthLine")
            elif station in mrt["EastWestLine (CG)"]:
                out[station].append("EastWestLine (CG)")
    return out

def get_interchange(stationline):
    out = {}
    for station in stationline:
        if len(stationline[station]) > 1:
            out[station] = stationline[station]
        else:
            pass
    return out


  
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
    
    mrt_d = read_station(f)
    lines = get_stationline(mrt_d)
    interchange = get_interchange(lines)
    
    current_line = lines[start]
    
    