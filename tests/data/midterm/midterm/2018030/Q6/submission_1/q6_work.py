import pickle

def read_stations(f):
    lines = ["EastWestLine (EW)","EastWestLine (CG)","NorthSouthLine"]
    s = dict.fromkeys(lines)
    ls = []
    for line in f:
        if "=EastWestLine (EW)=" in line or "=EastWestLine (CG)=" in line or "=NorthSouthLine=" in line:
            pass
        else:
            line = line.strip().split(",")
            ls.append(line)
    ls.pop(1)
    ls.pop(2)
    s["EastWestLine (EW)"] = ls[0]
    s["EastWestLine (CG)"] = ls[1]
    s["NorthSouthLine"] = ls[2]
    return s

def get_stationline(mrt):
    pass

def get_interchange(stationline):
    pass
    


  
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