import pickle

def read_stations(f):
    output = {}
    for line in f:
        x = line.strip()
        if 'Line' in x:
            key = x
            output[key] = []
            stations = []
        else :
            ans = stations.append(x.split())
            output[key]  = ans
    return output
            
def get_stationline(mrt):
    output = {}
    interchange = []
    interchange.append(mrt.keys)
    for line in mrt:
        for station in mrt[line]:
            x = []
            x.append(line)
            output[station] = x
            for i in interchange:
                if station in mrt[i]:
                    x.append(i)
                    output[station] = x
    return output 
               
    
def get_interchange(stationline):
    output = {}
    for key in stationline:
        if len(stationline[key]) > 1 :
            output[key] = stationline[key]
         
    
    return output

  
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
