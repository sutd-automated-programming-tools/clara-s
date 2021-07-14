import pickle

def read_stations(f):
    dic = {}
    ls = [i for i in f]
    trainlines = {'EastWestLine (EW)','EastWestLine (CG)','NorthSouthLine','CircleLine','DowntownLine','NorthEastLine'}
    for item in range(len(ls)-1):
        item1 = ls[item].strip('=')
        item1 = item1[:-2]
        if item1 in trainlines:
            ls1 = ls[item+1].split(', ')
            ls2 = [i.strip() for i in ls1]              
            dic[item1] = ls2
    return (dic)

def get_stationline(mrt):
    dic = {}
    for trainline in mrt:
        for stn in mrt[trainline]:
            if stn not in dic:
                dic[stn]=[trainline]
            else:
                dic[stn] = dic[stn]+[trainline]
    return dic

def get_interchange(stationline):
    dic = {}
    for i in stationline:
        if len(stationline[i])>1:
            dic[i]=stationline[i]
    return dic


  
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
    stations = read_stations(lines)
    stationline = get_stationline(mrt_d)
    interchanges = get_interchange(stationline)
    return None