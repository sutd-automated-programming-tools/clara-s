import pickle

def read_stations(f):
    d = {}
    for line in f:
        line = line.strip("\n")
        line = line.strip("=")
        d[line[0]]=[]
        if 
        # make lines 1,4 and 5 keys
        #make line 2,5,8 into seperate lists
        lst = line.strip(", ")
        # print("l",line[0])
        # d[line[0]] = []
        # station = line
        # # print(station)
        # for idx, val in enumerate(station):
        #     if idx > 0:
        #         d[line[0]].append(val)
        #         # for i in range(1,len(line)):
        
        
    return d

def get_stationline(mrt):
    interchange = {}
    for k,v in mrt.items:
        station = v
        
        

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