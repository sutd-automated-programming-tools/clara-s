import pickle

def read_stations(f):
    ans={'EastWestLine (EW)':'3','EastWestLine (CG)':'4', 'NorthSouthLine':'5'}
    EW1=[]
    EW2=[]
    NS=[]
    everything=[]
    for line in f:
        line=line.strip()
        data=line.split()
        everything.append(data)
    for i in range(1,34):
        EW1.append(everything[i])
    for i in range(35,38):
        EW2.append(everything[i])
    for i in range(39,66):
        NS.append(everything[i])
    ans['EastWestLine (EW)']=EW1
    ans['EastWestLine (CG)']=EW2
    ans['NorthSouthLine']=NS
    return ans

def get_stationline(mrt):
    ans={}
    station=[]
    for key in dic:
        lst=mrt['key']
        if lst[0] not in station:
            station.append(lst[0])
            lt=[]
            ans[lst[0]]=lt
        lt.append(key)
     return ans

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