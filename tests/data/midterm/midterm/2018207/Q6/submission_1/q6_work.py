import pickle

def read_stations(f):
    arr = f.readlines()
    out = dict()
    for i in range(len(arr)):
        arr[i] = arr[i].strip()
        arr[i] = arr[i].strip("=")
        
    for i in range(0,len(arr),3):
        out[arr[i]] = arr[i+1].split(", ")
    return out

def get_stationline(mrt):
    out = dict()
    key = list(mrt.keys())
    for i in key:
        for j in mrt[i]:
            if i not in out[j]:
                out[j] += i
                              
    return out

def get_interchange(stationline):
    out = dict()
    for key in stationline:
        if len(stationline[key]) > 1:
            out[key] = stationline[key]
            
    return out


  
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