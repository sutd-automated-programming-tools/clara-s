import pickle

def read_stations(f):
    lines = f.readlines()
    for line in lines:
        stations =   line.rstrip()
        mrt = {str(stations[0]): stations[1:33], str(stations[34]): stations[35:37], str(stations[38]): stations[39:65]}
    return mrt

def get_stationline(mrt):
    reverse = {}
    reverse[mrt.get('EastWestLine (EW)')]= ['EastWestLine (EW)']
    reverse[mrt.get('EastWestLine (CG)')]= ['EastWestLine (CG)']
    reverse[mrt.get('NorthSouthLine')]= ['NorthSouthLine']
    return reverse

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