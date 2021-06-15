import pickle

def read_stations(f):
    pass

def get_stationline(mrt):
    pass

def get_interchange(stationline):
    pass

def read_stations(f):
    lines = f.readlines()
    
    mrt = {}
    minicount = 0
    for i in lines:
        i = i.strip()
        if i != "":
            if i[0] == "=":
                mrt[i.strip("=")] = lines[minicount + 1].strip()
                
        minicount += 1
    return mrt
   

def get_stationline(mrt):
    reverse = {}
    for line, stations in mrt.items():
        for i in stations:
             reverse[i] = []
    for line, station in mrt.items():
        for i in station:
         reverse[i].append(line)
    return reverse

def get_interchange(stationline):
    interchange = {}
    for k in stationline:
        if len(stationline[k]) > 1:
            interchange[k] = stationline[k]
    return interchange



  
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