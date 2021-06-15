import pickle

def read_stations(f):
    stations = f.read().split('\n')
    d = {}
    new = stations[0].strip(' ')
    Header = new.strip('=')
    l = [stations[1]]
    d[Header] = l
    
def get_stationline(mrt):
    d = {}
    for i in mrt:
        for j in mrt[i]:
            if j not in d:
                d[j] = [(str(i))]
            elif j in d:
                d[j] += [str(i)]
    return d


def get_interchange(stationline):
    d = {}
    for j in stationline:
        if len(stationline[j]) >1:
            d[j] = stationline[j]
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
        u = get_interchange(p)
        b = read_stations(j)
        k = get_stationline(f)
    pass