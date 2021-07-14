import pickle

def read_stations(f):
    dict = {}
    biglist = []
    for i in f:
        splitter = i.split('\n')
        biglist.append(splitter)
    for x in biglist:
        for i in range(len(x)):
            if x[0] == '':
                biglist.remove(x)

def get_stationline(mrt):
    newdict = {}
    mrt = read_stations(f)
    for x in mrt.values():
        newdict[x] = 0
        print(newdict)
        

def get_interchange(stationline):
    stationline = get_stationline(mrt)
    newerdict = {}


  
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