import pickle

def read_stations(f):
    ret = {}
    alllines = f.readlines()
    for aline in alllines:
        aline = aline.strip()
        if "=" in aline:
            ret[aline.strip("=")] = []

    for aline in alllines:
        aline = aline.strip("\n")
        if "=" in aline:
            hi = ret[aline.strip("=")]
        elif "," in aline:
            hi.append(aline.split(', '))
    for key,value in ret.items():
        ret[key] = value[0]
    return ret
            
def get_stationline(mrt):
    ret = {}
    for lst in mrt.values():
        for values in lst:
            ret[values] = []
    
    for line,val in mrt.items():
        for station in ret.keys():
            if station in val:
                ret[station] += [line]
    return ret

def get_interchange(stationline):
    ret = {}
    for key, val in stationline.items():
        if len(val)>1:
            ret[key] = val
    return ret


  
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
    stations = read_stations(f)
    for val in stations.values():
        if start in val and end in val:
            #get the list of stations in the mrt line
            #get index of start and end stations
            #return list by splicing 
                   
                   
        elif start in val and end not in val:
                   #get the mrt lines of start and end station
                  #using get_interchange, check if there is an interchange station for these lines
                    #