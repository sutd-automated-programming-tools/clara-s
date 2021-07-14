import pickle

def read_stations(f):
    ans = {}
    ls_of_sta = []
    gotthing = False
    for line in f:
        if line[0] == '=':
            if gotthing == False:
                dict_key = line.strip('=')
            else:
                ans[dict_key] = ls_of_sta
                dict_key = ''
                ls_of_sta = []
                gotthing = False
        elif line[0] != ' ' or line[0] != '=':
            line.strip('/n')
            sub_ls = line.split(', ')
            ls_of_sta.append(sub_ls)
            gotthing = True
    if gotthing == True:
        ans[dict_key] = ls_of_sta
    return ans
        
def get_stationline(mrt):
    ans = {}
    for key,value in mrt.items():
        for station in value:
            if station not in ans.keys():
                ans[station] = [key]
            else:
                ans[station] = ans[station].append(key)
    return ans

def get_interchange(stationline):
    ans = {}
    for key,value in stationline.items():
        if len(value) > 1:
            ans[key] = value
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
        
        
        
    dic = read_stations(f)
    stations = get_stationline(dic)
    interchange = get_interchange(stations)
    start_line = stations[start]
    end_line = stations[end]
    if end_line in start_line:
        route = end_line[0]
        dic[route] = 