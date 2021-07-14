import pickle

def read_stations(f):
    dic = {}
    counter = 0
    for line in f:
        liney = f.readline()
        if line[0] == "=":
            station = liney.strip("=")
            dic[station] = []
        if str.isalpha(line) == True: 
            listy = liney.split(",")
            listyy = []
            for i in range(len(listy)):
                name = listy[i].strip()
                listyy.append(name)
                dic[station] = listyy
                        
    return dic

def get_stationline(mrt):
    newdic = {}
    for i in range(len(mrt)):
        mrtline = mrt[i]
        listy = mrt[mrtline]
        for j in listy:
            station = listy[j]
            newdic[mrtline] = station
    return newdic

def get_interchange(stationline):
    newdic = {}
    for station in stationline:
        if len(stationline[station]) > 1:
            newdic[station] = stationline[station]
    return newdic


  
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
    
    mrt = read_stations(f)
    stationline = get_stationline(mrt)
    interchange = get_interchange(stationline)
    for station in stationline:
        if start == station:
            start_stationline = stationline[station]
        if end == station:
            end_stationline = stationline[station]
    if end_stationline == start_stationline:
        for station in stationline:
            if end_stationline == station:
                Return 
    elif end_stationline != start_stationline:
        Return
    else:
        Return None
        
        
                