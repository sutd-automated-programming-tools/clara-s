import pickle

def read_stations(f):
    lines = f.readlines()
    dct = {}
    for line in lines:
        line = line.replace('\n','')
        line = line.replace('=', '')
        
        

def get_stationline(mrt):
    new = {}
    for k,v in mrt.items():
        for each in v:
            if each not in new.keys():
                new[each] = [k]
            else:
                new[each].append(k)
    return new
            

def get_interchange(stationline):
    inter = {}
    for k,v in stationline:
        if len(v) > 1:
            inter[k] = v
        else:
            continue
    return inter
            


  
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