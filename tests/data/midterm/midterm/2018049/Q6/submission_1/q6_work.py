import pickle

def read_stations(f):
    
    dic={}
    string = ""
    s= f.readlines()
    for i in s:
        string+=i
    string.split(" ")
    dic[string[0]] = string[1]

    return dic

def get_stationline(mrt):
    ans={}
    for i in mrt.values():
        ans.setdefault(i, []).append(mrt.keys(i))
    return ans

def get_interchange(stationline):
    for i in stationline.keys():
       if len(stationline[i]) == 1:
              del stationline[i]
    return stationline
              


  
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