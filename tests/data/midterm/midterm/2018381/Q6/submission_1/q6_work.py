import pickle

def read_stations(f):
    opdic = {}

    for i in range(3):
        reader = f.readline()
        reader = reader.replace('=','')
        reader = reader.replace('\n','')
        opdic[reader] =0
        reader2 = f.readline()
        reader2 = reader2.replace('\n','')
        reader2 = reader2.split(', ')
        opdic[reader] = reader2
        reader3 = f.readline()

    return opdic

def get_station_line(mrt):
    opdic ={}
    for key,value in mrt.items():
        #print(value)
        for i in range(len(value)):
            opdic[value[i]] = []
    for key,value in mrt.items():
        for i in range(len(value)):
            opdic[value[i]].append(key)
            
    return opdic

def get_interchange(stationline):
    opdic = {}
    for key,value in stationline.items():
        if len(value) >1:
            opdic[key] = value
    return opdic

  
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
       
    path = []
    mrt = read_stations(f)
    station = get_station_line(mrt)
    inter = get_interchange(station)
    startline = ''
    endline = ''
    startpos = -1
    endpos = -1
    for key,value in mrt.items():
        print(key)
        for i in range(len(value)):
            if value[i] == start:
                startline = key
                startpos = value.index(value[i])
            if value[i] == end:
                endline = key
                endpos = value.index(value[i])
    print(startpos)
    print(endpos)
    if startline == endline: #for same line
        if startpos>endpos:
            for i in range(startpos,endpos,-1):
                path.append(mrt[startline][i])
        if startpos<endpos:
            for i in range(startpos,endpos,1):
                path.append(mrt[startline][i])
    if startline != endline:
        #find if there are ways to transit from startline to endline
        #if no such paths exist,return None
        pass
    return path