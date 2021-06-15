import pickle

def read_stations(f):
    dic = {}
    for line in f:
        if 'Line' in line == True:
            mrtline = line[1:-3]
        else:
            lst = line.split(', ')
            for i in lst:
                dic[mrtline] += i
    return dic

def get_stationline(mrt):
    ndic = {}
    for k,v in mrt:
        if v not in ndic[v]:
            ndic[v]= [k]
        else:
            ndic[v] += [k]
    return ndic

def get_interchange(stationline):
    ndic = {}
    for k,v in stationline:
        if len(v) >1:
            ndic[k] = v
    return ndic


  
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
    path = None
    
    return path