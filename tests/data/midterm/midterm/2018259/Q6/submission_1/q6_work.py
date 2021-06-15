import pickle

mrt = open('mrt.txt','r')
def getMRT(mrt):
    mrtline=dict()
    for i in mrt:
        i=i.strip()
        arr=i.split(', ')
        mrtline[arr[0]]=arr[1:]
    return mrtline

def get_stationline(mrt):
    outdict = dict()
    for i in mrt:
        for x in mrt[i]:
            outdict[x] = i
        return outdict

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