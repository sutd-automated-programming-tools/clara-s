import pickle

def read_stations(f):
    lines = f.readlines()
    d = {}
    for i in range(0, len(lines), 3):
        k = lines[i][1:-2]
        v = lines[i+1]
        if(v[-1] == '\n'):
            v = v[:-1]
        v = v.split(', ')
        d[k] = v
    return d

def get_stationline(mrt):
    d = {}
    for linename, line in mrt.items():
        for station in line:
            if(station in d.keys()):
                d[station].append(linename)
            else:
                d[station] = [linename]
    return d

def get_interchange(stationline):
    d = {}
    for station, lines in stationline.items():
        if len(lines)>1:
            d[station] = [i for i in lines]
    return d


  
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
    partA = read_stations(f)
    partB = get_stationline(partA)
    partC = get_interchange(partB)
    
    with open('stations_short.pickle','rb') as f:
        mrt_d = pickle.load(f)
    with open('lines_short.pickle','rb') as f:
        lines = pickle.load(f)
    with open('interchange_short.pickle','rb') as f:
        interchange = pickle.load(f)
    
    
    shortestpath = None
    
    startstationlines = []
    endstationlines = []
    
    for line, stationlist in partA.items():
        if start in stationlist:
            startstationlines.append(line)
        if end in stationlist:
            endstationlines.append(line)
    
    for startline in startstationlines:
        if startline in endstationlines:
            startindex = None
            endindex = None
            for i in range(len(partA[startline])):
                if partA[startline][i]==start:
                    startindex = i
                if partA[startline][i]==end:
                    endindex = i
            if(startindex>endindex):
                temp = partA[startline][startindex:endindex-1:-1]
            else:
                temp = partA[startline][startindex:endindex+1]
            if(shortestpath==None or len(temp)<len(shortestpath)):
                shortestpath = temp
    
    #yeah the rest (with interchange) is not done
    
    return shortestpath