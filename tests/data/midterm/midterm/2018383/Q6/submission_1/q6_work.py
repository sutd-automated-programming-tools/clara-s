import pickle

def read_stations(f):
    dic = {}
    curKey = ""
    lines = f.read().split('\n')
    for line in lines:
        if not line:
            pass
        elif line[0] == '=':
            curKey = line[1:-1]
            dic[curKey] = []
        else:
            dic[curKey] = line.split(', ')
    
    return dic

def get_stationline(mrt):
    dic = {}
    for k,v in mrt.items():
        for station in v:
            if station not in dic:
                dic[station] = [k]
            else:
                dic[station].append(k)
    return dic

def get_interchange(stationline):
    dic = {}
    for k,v in stationline.items():
        if len(v)>1:
            dic[k] = v
    return dic

def find_path(f, start, end):
    stationDic = read_stations(f)
    lineDic = get_stationline(stationDic)
    interDic = get_interchange(lineDic)
    
        
    
    for line,stations in stationDic.items():
        s, e = -1, -1
        for i in range(len(stations)):
            if stations[i]==start:
                s = i
            elif stations[i]==end:
                e = i
        if s!=-1 and e!=-1:
            ans = stations[min(s,e):max(s,e)+1]
            return ans if s<e else ans[::-1]
    ans = []
    curLen = 9999
    for line1 in lineDic[start]:
        for line2 in lineDic[end]:
            for inter,inLines in interDic.items():
                if line1 in inLines and line2 in inLines:
                    temp = find_path(start,inter)[:-1] + find_path(inter,end)
                    if len(temp)<curLen:
                        ans = temp
                        curLen = len(temp)
    if curLen != 9999:
        return ans
    return None
    
            
  
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
def find_path2(f,start,end):
    with open('stations_short.pickle','rb') as f:
        mrt_d = pickle.load(f)
    with open('lines_short.pickle','rb') as f:
        lines = pickle.load(f)
    with open('interchange_short.pickle','rb') as f:
        interchange = pickle.load(f)
    pass