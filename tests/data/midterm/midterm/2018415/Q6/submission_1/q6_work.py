import pickle

def read_stations(f):
    lines = f.readlines()
    lines_s = [line.strip('\n') for line in lines]
    lines_r = [line.strip('\r') for line in lines_s]
    return lines_r

def get_stationline(mrt):
    for x in range(len(mrt)):
        if lst[x]["mrt"] == name:
            return lst[x][key]

def get_details(name, key, lst):
    for x in range(len(lst)):
        if lst[x]["name"] == name:
            return lst[x][key]

def get_interchange(stationline):
    pass


  
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