import pickle

f = open ('mrt_lines_short.txt', 'r')

def read_stations(f):
    data = open(f,"r")
    data = data.readlines()
    out = []
    for i in data:
        a = i.split()
        a = list(map(int,a)) ########################## CONVERT ALL DATA INTO INT IN ARRAY
        out.append((a[0],a[1]))
    print(out)
    return out

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