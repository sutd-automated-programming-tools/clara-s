import pickle

def read_stations(f):
    station={}
    while True:
        line = f.readline()
        if line=="":
            break
        line = line.strip("=\n")
        colourline = line
        line = f.readline()
        line = line.strip("\n")
        lst = line.split(", ")
        station[colourline]=lst
        f.readline()
    return station
def get_stationline(mrt):
    stationline={}
    for i in mrt:
        station=[]
        station.append(i)
        for a in mrt[i]:
            station.append(a)
        for b in range(1,len(station)):
            stationline[station[0]]=station[b]
    return stationline
        
        

def get_interchange(stationline):
    stations=[]
    interchange=[]
    ans={}
    for i in stationline:
        stations.append(i)
    for i in stations:
        no=stations.count(i)
        if no>1 and i not in interchange:
            interchange.append(i)
    for i in interchange:
        line=[]
        for a in stationline:
            if i == a:
                line.append(stationline[a])
        ans[i]=line
    return ans
        
def find_path(f,start,end):
    stations=read_stations(f)
    path=[]
    for i in stations:
        if start in stations[i] and end in stations[i]:
            indexend=stations[i].index(end)
            indexstart=stations[i].index(start)
            for a in range(indexstart,indexend+1):
                path.append(station[i][a])
                return path
    elif:
        for i instations
            

  
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