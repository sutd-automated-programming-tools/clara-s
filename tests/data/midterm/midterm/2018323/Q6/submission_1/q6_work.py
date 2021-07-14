import pickle

f = open('mrt_lines_short.txt', 'r')

def read_stations(f):
    stations = dict()
    for line in f:
        line = line.strip('\n').split(',')
    if 'Line' in line:
        r = line
        lst = []
        for y in range (1, len(line)):
            st.append(line[y])
            stations[r] = lst
    return stations

def get_stationline(mrt):
    stationline = dict()
    for x in mrt:
        stationline[mrt.get()] = mrt.keys()
    return stationline

def get_interchange(stationline):
    interchange = dict()
    for x in interchange: 
        for y in x:
            if x.count(y) > 1:
                interchange.append(x)
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