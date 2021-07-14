import pickle

def read_stations(f):
    shell = []
    for line in f:
        line.strip('=\n')
        line.strip('\n')
        shell.append(line)
    d = {shell[0]:shell[1],shell[2]:shell[3],shell[4]:shell[5]}
    return shell
    

def get_stationline(mrt):
    d = dict()
    for line in mrt:
        for station in mrt[line]:
            d[station] = []
    for line in mrt:
        for station in mrt[line]:
            d[station].append(mrt[line])
    return d

def get_interchange(stationline):
    d = dict()
    for station in stationline:
        if len(stationline[station])>1:
            d[station] = stationline[stations]
    return d


  
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