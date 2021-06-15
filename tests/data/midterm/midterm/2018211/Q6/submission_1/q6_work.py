import pickle

def read_stations(f):
    s = f.read()
    st = s.split("=")
    dict_ = {}
    for i in range(int((len(st)-1)/2)):
        dict_[st[2*i+1]] = (st[2*(i+1)].strip("\n")).split(", ")
    return dict_

def get_stationline(mrt):
    ans = {}
    for lines in mrt:
        for station in mrt[lines]:
            if station not in ans:
                ans[station] = []
                ans[station].append(lines)
            else:
                ans[station].append(lines)
    return ans

def get_interchange(stationline):
    ans = {}
    for stations in stationline:
        if len(stationline[stations]) > 1:
            ans[stations] = stationline[stations]
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
    
    a = get_interchange(mrt_d) 
    b = get_stationline(a)
    try:
        mrt_d = read_stations(f)
    except:
        pass

    for lines in mrt_d:
        if start in mrt_d[lines] and end in mrt_d[lines]:
            start_index = 0
            end_index = 0
            for i in range(len(mrt_d[lines])):
                if mrt_d[lines][i] == start:
                    start_index = start_index 
                if mrt_d[lines][i] == end:
                    start_index = end_index
            return mrt_d[lines][min(start_index,end_index):max(start_index,end_index)]
    return None
            
    