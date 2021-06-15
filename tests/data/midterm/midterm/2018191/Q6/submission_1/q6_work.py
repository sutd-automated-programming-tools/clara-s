import pickle

def read_stations(f):
    traind = {}
    data = f.readlines()
    for line in data:
        if line[0] == "=":
            print(line)
            line = line.replace("\n","")
            line = line.replace("=","")
            print(line)
            key = line
            traind[key] = ""
        elif line[0] != "\n":
            line = line.replace("\n","")
            line = list(line.split(", "))
            traind[key] = line     
    return traind

def get_stationline(mrt):
    out = {}
    s_list = list(mrt.values())
    s_keys = list(mrt.keys())
    print(s_list)
    print(s_keys)
    for i in range(len(s_list)):
        for j in range(len(s_list[i])):
            try: 
                out[s_list[i][j]].append(s_keys[i])
            except:
                out[s_list[i][j]] = []
                out[s_list[i][j]].append(s_keys[i])
    return out

def get_interchange(stationline):
    out = {}
    #s_list = list(stationline.values())
    s_keys = list(stationline.keys())      
    for key in s_keys:
        if len(stationline[key]) > 1:
            out[key] = stationline[key]
    return out

def find_path(f,start,end):
    stations = read_stations(f)
    l_keys = list(stations.keys())
    start_l = ""
    end_l = ""
    start_i = 0
    end_i = 0
    ans = []
    for key in l_keys:
        if start in stations[key]:
            start_l = key
        if end in stations[key]:
            end_l = key
    
    #find index of start station in line x
    if start_l == end_l:
        for i in range(len(stations[start_l])):
            if start == stations[start_l][i]:
                start_i = i
            if end == stations[end_l][i]:
                end_i = i
        print(start_i,end_i)
    if end_i > start_i:
        for j in range(start_i,end_i):
            ans.append(stations[start_l][j])
            print(stations[start_l][j])
            print(ans)
    elif start_i > end_i:
        for j in range(start_i,end_i-1,-1):
            ans.append(stations[start_l][j])
        return ans  
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