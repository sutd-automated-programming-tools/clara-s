import pickle

def read_stations(f):
    dictionary = {}
    lst = []
    for line in f:
        line = line.strip()
        line = line.replace('=','')
        line = line.split(',')
        lst.append(line)
        
    for x in lst[1]:
        dictionary[lst[0]] = x

    return dictionary
        
        

def get_stationline(mrt):
    pass

def get_interchange(stationline):
    interchange = {}
    for key in stationline:
        if len(stationline.values())>1:
            interchange[key] = stationline.values()
        
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