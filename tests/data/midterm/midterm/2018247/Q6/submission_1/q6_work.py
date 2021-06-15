import pickle

def read_stations(f):
    station_dict = {}
    total = ''
    lines = f.readlines()
    for line in lines:
        total+= line
    newls = total.split('=')
    for i in range(len(newls)//2):
        key = newls[2*i+1]
        stripstr = newls[2*i+2].strip(' \n')
        value = stripstr.split(',')
        station_dict[key]=value
    return station_dict
        
    
    
    
def get_stationline(mrt):
    linedict = {}
    for line,stationls in mrt.items():
        for station in stationls:

                linedict[station] = linedict.get(station)+ line +','
            
    return linedict

def get_interchange(stationline):
    exchange = {}
    for k,v in stationline.items():
        if len(v)>1:
            exchange[k] = v
    return exchange


  
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
    mrt_d = read_station(f)
    lines = get_stationline(mrt_d)
    start_lines = lines[start]
    end_lines = lines[end]
    for i in start_lines:
        for j in end_lines:
            if i == j:
                one_line = i
                return mrt_d[line]
    
    interchange = get_interchange(lines)