import pickle

def read_stations(f):
    dic={}
    track = ""   
    x = ""
    for ln in f:
        line = (ln.split())
        if len(line) == 2 or len(line) == 1:
            x = ln.strip()
            track = x.strip("=")
            stops = []
        elif len(line)==0:
            stops = []
        else:
            stops = ln.strip()
            stops = stops.split(",")
            dic[track] = stops
    return dic

def get_stationline(mrt):
    new_dict={}
    
    for line in mrt.keys():
        for station in mrt[line]:
            new_dict[station]=line
    return new_dict  
        

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