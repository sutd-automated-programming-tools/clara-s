import pickle

def read_stations(f):
    ansdict = {}
    keys = []
    stations = [[],[],[]]
    stations.append(f.strip(=))
    f.readlines()
    a = f.split(",")
    for i in a:
        stations[0].append(strip(i))
    f.readlines()
    b = f.split(",")
    for i in b:
        stations[0].append(strip(i))
    f.readlines()
    c = f.split(",")
    for i in c:
        stations[0].append(strip(i))
    f.readlines()
    d = f.split(",")
    for i in d:
        stations[0].append(strip(i))
    f.readlines()
    e = f.split(",")
    for i in e:
        stations[0].append(strip(i))

def get_stationline(mrt):
    dict = {}
    for k, v in mrt.items(): #analysing each item in the dictionary mrt
        for j in v: #for loop to look at each station in the list that is the valsue for the mrt line key
            if j not in dict.keys(): #if the mrt station is not a key in the new dict yet add it do the dict with the value of the mrt line
                dict[j] = [k]
            else: # if the station is already inside the new dict add the mrt line to it's corresponding value
                dict[j].append(k)
    return dict

def get_interchange(stationline):
    dict2 = {}
    for k, v in stationline.items():
        if length v <2:
            pass
        elif:
            dict2[k] = v
    return dict2


  
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
    