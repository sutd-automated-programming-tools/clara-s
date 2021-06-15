import pickle

def read_stations(f):
    dic = {}
    line = f.readlines().split(", ")
    
    for i in range(len(line)):
        if line[i].isalphanum():
            dic[line[i]] = line[i+1]
        else: 
            pass
    
    
    return dic

def get_stationline(mrt):
    dic = {}
    for i in range(len(mrt)):
        for j in mrt[i]:
            if j not in dic:
                dic[j] = []
                dic[j].append(mrt[i])
    
    for i in dic:
        for j in mrt:
            if i in j[0]:
                dic[i].append(j)
    
    return dic

def get_interchange(stationline):
    dic = {}
    
    for i in stationline:
        if len(stationline[i]) > 1:
            dic[i] = stationline[i]
    
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
    line_dic = read_stations(f)
    stations_dic = get_stationline(line_dic)
    
    path = []
    for i in line_dic:
        if start in line_dic[i] and end in line_dic[i]:
            start = line_dic[i].index(start)
            end = line.dic[i].index(end)
            path = line_dic[i][start + 1:end]
            return path
            break