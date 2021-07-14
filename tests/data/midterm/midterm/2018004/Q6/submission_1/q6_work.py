import pickle

def read_stations(f):
    lines = [] 
    stations = [] 
    for line in f: 
        if line[0] == "=": 
            lines.append(line[1:-2])
        else: 
            ls = line.split(",") 
            for i in range(len(ls)): 
                ls[i] = ls[i].strip()
            stations.append(ls)
    mydict = {} 
    for i in range(len(lines)): 
        mydict[lines[i]] = stations[i]
    return mydict

def get_stationline(mrt):
    mydict = {}
    for line in mrt.keys():
        for station in mrt[line]:
            if station not in mydict.keys():
                mydict[station] = [line]
            else:
                mydict[station].append(line)
    return mydict 

def get_interchange(stationline):
    mydict = {}
    for station in stationline.keys(): 
        if len(stationline[station]) > 1: 
            mydict[station] = stationline[station]
    return mydict


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
        
    #if start and end contain the same station lines: return dictionary of stations of that line from start to end 
    #else if different station lines: run through the starting station line till interchange is reached. check if stationline has same stationline as end. change to other stationline and read until end. 
    #else: return None 
    get_stationline(mrt_d)
    get_interchange(lines)
    return None 