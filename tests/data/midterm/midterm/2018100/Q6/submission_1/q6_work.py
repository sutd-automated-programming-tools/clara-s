import pickle

def read_stations(f):
    lines = f.readlines()
    dt = {}
    lineName = ''
    for line in lines:
        line.strip('\n')
        if line[0] == '=': #check header
            lineName = line[1:-2]
            continue
        linels = line.split(', ')
        if linels[-1][-1] == '\n':
            linels[-1] = linels[-1][:-1]
        if len(linels) != 1:
            dt.setdefault(lineName, linels)
            lineName = ''
            linels = []
    return dt

def get_stationline(mrt):
    dt = {}
    for lineName,stationls in mrt.items():
        for station in stationls:
            dt[station] = dt.get(station,[]) + [lineName]
    return dt

def get_interchange(stationline):
    dt = {}
    for station,linels in stationline.items():
        if len(linels) > 1:
            dt.setdefault(station, linels)
    return dt


  
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
    with open('mrt_lines_short.txt','r') as f:    
        mrt = read_stations(f)
        stationline = get_stationline(mrt)
        print('statline',stationline)
        interchange = get_interchange(stationline)

        #no change line

        startline = lines[start]
        endline = lines[end]

        sameline = False
        #print(startline,endline)
        for el in startline:
            if el in endline:
                sameline = True
                line = el
        if sameline:
            #print(line)
            path = mrt[line]
            #print('path',path)
            startindex = path.index(start)
            #print('starti',startindex)
            endindex = path.index(end)
            #print('endi', endindex)
            if startindex < endindex:
                path = path[startindex:endindex+1]
            else:
                path = path[startindex:endindex-1:-1]
            return path
        changels = []
    lines = startline + endline
    #print(lines)
    for statname,linels in interchange.items():
        #print(linels)
        if set(lines) == set(linels):
            changels.append(statname)
    #print(changels)
    possiblepath = []
    for inter in changels:
        start2inter = []