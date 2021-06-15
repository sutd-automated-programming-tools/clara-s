import pickle

def read_stations(f):
    files = list(f)
    #files = ["=sth=","something, someone, somewhere,nowhere","=nth=","nowhere, noone","noplace"]
    stnLs = []
    rtnDic = {}
    stnStr = []
    for i in files :
        if len( i.strip() )>0 :
            if i[0] == "=" :
                if len(stnStr) >0 :
                    stnLs.append(stnStr)
                stnStr = i.strip()[1:-1]
                stnLs.append(stnStr)
                stnStr = []
            else :
                ls = i.strip().split(",")
                for k in ls :
                    if k.strip() != "" :
                       stnStr.append(k.strip())
    stnLs.append(stnStr)
    
    for j in range(0, len(stnLs), 2) :
        rtnDic[stnLs[j]] = stnLs[j+1]
    return rtnDic

def get_stationline(mrt):
    rtnDic = {}
    for lines,stations in mrt.items() :
        for i in stations :
            if i not in rtnDic:
                rtnDic[i] = []
            rtnDic[i].append(lines)
    return rtnDic
   
def get_interchange(stationline) :
    rtnDic = {}
    for key,value in stationline.items() :
        if len(value)>1 :
            rtnDic[key] = value
    return rtnDic

def find_path(f,start,end) :
    stns = read_stations(f)
    stnLine = get_stationline(stns)
    inter = get_interchange(stnLine)
    lineStart = stnLine[start]
    lineEnd = stnLine[end]
    print("stn:", lineStart)
    print("stn:", lineEnd)
    pos = []
    for i in lineStart :
        if i in lineEnd:
            pos.append(i)
    if len(pos)>0 :
        posWays = []
        for i in pos :
            line = stns[i]
            startIndex = line.index(start)
            endIndex = line.index(end)
            print(startIndex, endIndex)
            direction = (startIndex-endIndex)
            if direction>0 :
                posWays.append(line[startIndex:endIndex-1:-1])
            else: 
                posWays.append(line[startIndex:endIndex+1])
        if len(posWays) == 1:
            return posWays[0]
        elif len(posWays) > 1:
            shorter = 0
            short = len(posWays(0))
            for j in len(posWays) :
                if len(posWays[j])<short :
                    shorter = j
            return posWays[j]
        else:
            exchange = []
            for interStn in inter:
            if lineStart in interStn and lineEnd in interStn:
                exchange.append(interStn)
            for i in interStn :
                line = stns[i]
                startIndex = line.index(start)
                midIndex = line.index(i)
                endIndex = line.index(end)
                direction1 = (startIndex-midIndex)
                direction2 = (midIndex-finalIndex)
                
                if direction>0 :
                        posWays.append(line[startIndex:endIndex-1:-1])
                    else: 
                        posWays.append(line[startIndex:endIndex+1])
                if len(posWays) == 1:
                    return posWays[0]
                   
                
  
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
'''
def find_path(f,start,end):
    with open('stations_short.pickle','rb') as f:
        mrt_d = pickle.load(f)
    with open('lines_short.pickle','rb') as f:
        lines = pickle.load(f)
    with open('interchange_short.pickle','rb') as f:
        interchange = pickle.load(f)
    pass
    '''