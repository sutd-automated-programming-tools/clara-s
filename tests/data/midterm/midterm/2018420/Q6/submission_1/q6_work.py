import pickle

def read_stations(f):
    lines = f.readlines()
    lines_s = line.strip("\n") for line in lines
    lines_r = line.strip("=") for line in lines_s
    final = line.split(" ") for line in lines_r

    stations = {}
    for i in final:
        stations.setdefault(a, {}).update({b:1})
        a,b = b,a
        g.setdefault(a, {}).update({b:1})
    return g

def get_stationline(mrt):
    new_dict={}
    for i in mrt:
        

def get_interchange(stationline):
    new_dict_1={}
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