import pickle

def read_stations(f):
    file = open(f)
    big_ls = []
    for line in file:
        big_ls.append(line)

def get_stationline(mrt):
    new_ls = []
    EW = []
    NS = []
    CG = []
    station = {}
    d = read_stations(f)
    new_ls.append(d.keys())
    EW.append(d["EastWestLine (EW)"])
    NS.append(d["NorthSouthLine"])
    CG.append(d["EastWestLine (CG)"])
    for stations in EW:
        station[stations] = ["EastWestLine (EW)"]
        for stations in NS:
            station[stations] = ["NorthSouthLine"]
            for stations in CG:
                station[stations] = ["EastWestLine (CG)"]
    return station
          
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