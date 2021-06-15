import pickle

def read_stations(f):
    res = {}
    t = f.readlines()
    for i in f:
        li = i.strip().split(',')
        if len(li)==1:
            s = li[0]
            res[s] = []
        else:
            for j in li:
                res.append(j)
    return res

def get_stationline(mrt):
    res = {}
    for i in mrt:
        for j in mrt[i]:
            if j not in res:
                res[j] = [i]
            else:
                res[j].append(i)
    return res

def get_interchange(stationline):
    res = {}
    for i in stationline:
        if len(stationline[i])>1:
            res[i] = stationline[i]
    return res


  
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