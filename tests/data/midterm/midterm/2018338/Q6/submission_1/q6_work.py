import pickle

def read_stations(f):
    content=readlines()
    mark=0
    result={}
    for i in content:
        if i=='=EastWestLine (EW)=':
            mark=1
            result{'EastWest (EW)'}=i+1
        if i=='=EastWestLine (CG)=':
            mark=2
            result{'EastWestLine (CG)'}=(i+1).strip.split
        if i=='=NorthSouthLine=':
            mark=3
            result{'NorthSouthLine'}=(i+1).strip().split()
    
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