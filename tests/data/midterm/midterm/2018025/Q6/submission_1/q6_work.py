import pickle

def read_stations(f):
    dic = {}
    ls= f.readlines()
    for i in range(len(ls)):
        if i % 2 ==0:
            line = ls.pop(i)
        else: 
            station = ls[i].strip().split(",")
         
        dic[line]=station
    return dic


def get_stationline(mrt):
    dic = {}
    ls = list(mrt.values())
    for key in mrt:
        for i in ls:
            if i in mrt[key]:
                dic[i]=key
    return dic

def get_interchange(stationline):
    dic = {}
    for k in stationline:
        if len(stationline[k])>1:
            dic[k] = stationline[k]
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
    pass