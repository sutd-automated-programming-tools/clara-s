import pickle

def read_stations(f):
    h = f.readlines()
    v = []
    for a in h:
        z = ''
        for x in a:
            while x != ',':
                if x.isalpha() or x == '' :
                    z += x
                else:
                    z += ''
    v.append(tuple(i for i in z.split()))
    return (v)h

def get_stationline(mrt):
    h = {}
    for x in mrt:
        if i in mrt[x]:
            h[i] = h.get(i,[])
            h[i].append(x)
    return h

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