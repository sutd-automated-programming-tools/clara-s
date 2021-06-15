import pickle

def read_stations(f):
    stations=dict()
    EWLsublist=[]
    EWL=f.readline().strip('\n').strip('=')
    EWLsublist=f.readline().strip('\n').split(',')
    stations[EWL]=EWLsublist
    f.readline()
    EWLCG=f.readline().strip('\n').strip('=')
    EWLCGsublist=f.readline().strip('\n').split(',')
    stations[EWLCG]=EWLCGsublist
    f.readline()
    NSL=f.readline().strip('\n').strip('=')
    NSLsublist=f.readline().strip('\n').split(',')
    stations[NSL]=NSLsublist
    return stations

def get_stationline(mrt):
    getstation={}
    return getstation

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