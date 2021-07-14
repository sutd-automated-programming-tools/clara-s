import pickle

def read_stations(f):
    myfile = open(f,"r")
    line = myfile.read()
    line.strip()
    
    

    

def get_stationline(mrt):
    oup = {}
    for i in mrt:
        for j in mrt[i]:
            oup[j] = []
        oup[j].append(i)
    return oup


def get_interchange(stationline):
    newdic = {}
    for i in stationline:
        if len(stationline[i])>1:
            newdic[i] = stationline[i]
    return newdic


  
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
    