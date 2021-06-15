import pickle

def read_stations(f):
    dc={}
    station1=f.readline()
    dc[str.strip(stations1)]=list[(f.readline())]
    station2=f.readline()
    dc[str.strip(stations2)]=list[(f.readline())]
    station3=f.readline()
    dc[str.strip(stations3)]=list[(f.readline())]
    return dc

def get_stationline(mrt):
    station_name=[]
    for i in mrt('EastWestLine (EW)'):
        if i not in station_name:
            station_name.append(i)
    for i in mrt('EastWestLine (CG)'):
        if i not in station_name:
            station_name.append(i)
    for i in mrt('NorthSouthLine'):
        if i not in station_name:
            station_name.append(i)
    for l in station_name:
                    
        
def get_interchange(stationline):
    station_name=list(stationline.keys())
    line_name=list(stationline.values())
    n=0
    dc={}
    while n<len(line_name):
        if len(line_name[n])>1:
            dc[station_name[n]]=line[name][n]
    return dc


  
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