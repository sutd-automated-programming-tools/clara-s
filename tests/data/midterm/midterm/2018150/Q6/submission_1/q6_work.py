import pickle

def read_stations(f):
    line = f.read().strip().splitlines()
    dic = {}
    for i in range(len(line)):
        x = line[i].split(",")
        lst = []
        if "=" in line[i]:
            line[i] = line[i].replace("=","",2)
            keyindex = i
        elif len(x) > 1:
            for t in range(len(x)):
                lst.append(x[t].strip())
                dic[line[keyindex]] = lst
    return dic

def get_stationline(mrt):
    dic = {}
    for k,v in mrt.items():
        for i in range(len(v)):
            if v[i] in dic.keys():
                dic[v[i]] = dic[v[i]].append(k)
            else:
                dic[v[i]] = [k]
    return dic

def get_interchange(stationline):
    dic = {}
    for k,v in stationline.items():
        if len(v) > 1:
            dic[k] = v
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