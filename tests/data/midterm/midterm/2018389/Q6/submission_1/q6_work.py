import pickle

def read_stations(f):
    dic = {}
    text = f.readline()
    line = None
    while len(text) != 0:
        if text[0] == "=":
            a = text.split("=")
            line = a[1]
            dic[line] = []
        else:
            b = text.split(", ")
            for i in b:
                if b!= " ":
                    dic[line].append(i.strip())
                else:
                    pass
        text = f.readline()
    return dic 

def get_stationline(mrt):
    dic = {}
    for i in mrt:
        for j in i:
            if j not in dic:
                dic[j] = []
                dic[j].append(str(i))
            else:
                dic[j].append(str(i))
    return dic

def get_interchange(stationline):
    dic = {}
    for i in stationline:
        if len(i) > 1:
            dic[i] = stationline[i]
        else:
            pass
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