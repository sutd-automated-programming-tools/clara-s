import pickle

def read_stations(f):
    s = f.readlines()
    EW = 0
    EWL = []
    EWCG = 0
    EWCGL = []
    NS = 0
    NSL = []
    ret = {}
    for index, line in enumerate(s):
        if line == "=EastWestLine (EW)=":
            EW = index
        elif line == "=EastWestLine (CG)=":
            EWCG = index
        elif line == "=NorthSouthLine=":
            NS = index
    for line in s[EW:EWCG]:
        x = line.strip()
        EWL.append(x)
    for line in s[EWCG:NSL]:
        x = line.strip()
        EWCGL.append(x)
    for line in s[NSL:]:
        x = line.strip()
        NSL.append(x)
    ret[EW] = EWL
    ret[EWCG] = EWCGL
    ret[NS] = NSL
    return ret

def get_stationline(mrt):
    
    
def get_interchange(stationline):
    ret = {}
    for i in stationline.keys():
        if len(stationline[i]) > 1:
            ret[i] = stationline[i]
    return ret
            


  
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