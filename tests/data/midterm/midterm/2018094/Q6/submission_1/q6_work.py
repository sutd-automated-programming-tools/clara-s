import pickle

def read_stations(f):
    d = {}
    for i in f:
        if '=' in i:
            d[i.strip().strip('=')] = []
            var = i.strip().strip('=')
        elif i.strip() != '':
            d[var].extend(i.strip().split(', '))
    return d

def get_stationline(mrt):
    d = {}
    for idx, i in enumerate(mrt.values()):
        for j in i:
            if j not in d:
                d[j] = [list(mrt.keys())[idx]]
            else:
                d[j].append(list(mrt.keys())[idx])
    return d

def get_interchange(stationline):
    d = {}
    for i in stationline.keys():
        if len(stationline[i]) > 1:
            d[i] = stationline[i]
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

    mrt = read_stations(f)
    stationline = get_stationline(mrt)
    interchange = get_interchange(stationline)

    for i in stationline[start]:
        if i in stationline[end]:
            if mrt[i].index(start) < mrt[i].index(end):
                return mrt[i][mrt[i].index(start):mrt[i].index(end) + 1]
            else:
                return list(reversed(mrt[i][mrt[i].index(end): mrt[i].index(start) + 1]))