import pickle

def read_stations(f):
    lines = f.readlines()
    res = {}
    for i,c in enumerate(lines):
        if c[0] == "=":
            key = c.strip()
            key = key.strip("=")
            res[key] = lines[i+1].strip().split()
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
    res={}
    for i in stationline:
        if len(stationline[i]) > 1:
            res[i]=stationline[i]
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
#    with open('lines_short.pickle','rb') as f:
#        lines = pickle.load(f)
#    with open('interchange_short.pickle','rb') as f:
#        interchange = pickle.load(f)
    res = []
#    mrt_d = read_stations(f)
    stationline = get_stationline(mrt_d)
    interchange = get_interchange(stationline)
    line = stationline[start]
    same_line = False
    for i in line:
        if i in stationline[end]:
            same_line = True
            path = i

    if same_line:
        a = mrt_d[path].index(start)
        b = mrt_d[path].index(end)
        for i in range(a,b+1):
            res.append(mrt_d[path][i])
        return res
    