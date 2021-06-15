import pickle

def read_stations(f):
    c=[]
    for line in f:
        b = line.strip()
        c.append(b.split())
       # d = {b[0]:b[1]}
        print(b)
        #print(d)
        #c = b
        #del c[0]
        #d = {}
        #d[b[0]] = c
        
    d = {}
    d[c[0]] = c[1]
        
    return d

def get_stationline(mrt):
    c = {}
    for keys in mrt.keys:
        lst = mrt.get
        
        

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