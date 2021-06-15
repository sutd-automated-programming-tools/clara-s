import pickle

def read_stations(f):
    c = f.readlines()
    md = {}
    removed =[]
    for line in range(len(c)):
        lst = c[line].split()
        removed.append(lst)
    #print(removed)
    stations = [removed[1],removed[4],removed[7]]
    #print(stations)
    md["EastWestLine (EW)"] = stations[0]
    md["EastWestLine (CG)"] = stations[1]
    md["NorthSouthLine"] = stations[2]
    #print(md)
    return md

def get_stationline(mrt):
    sl = {}
    for n in range(len(mrt[NorthSouthLine]):
        sl[mrt[NorthSouthline][n]= "NorthSouthLine"]
           
                   

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