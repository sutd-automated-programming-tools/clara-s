import pickle

def read_stations(f):
    f = f.read()
    f = f.split('\n')
    station = []
    dct = {}
    f.append('')
    for i in range(len(f)):
        for i in range(len(f)):
            if i != 0:
                if f[i] != '':
                    station.append(f[i])
                if f[i] == '':
                    dct[f[0].strip('=')] = station
                    station = []
                    f = f[i+1:]
                    break
    return dct

def get_stationline(mrt):
    key = list(mrt.keys())
    val = list(mrt.values())
    dct = {}
    for i in range(len(val)):
        for j in range(len(val[i])):
            for k in range(len(key)):
                if val[i][j] in mrt[key[j]]:
                    dct[val[i][j]] = key[j]
        return dct

def get_interchange(stationline):
    pass


  
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