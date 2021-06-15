import pickle

def read_stations(f):
    stationsDict = {}
    stationList = []
    for lines in f:
        data = lines.strip()
        data = data.strip('\n')
        data = data.strip('=')
        lists = data.split(', ')
        stationList.append(lists)
    for i in stationList:
        print(i)
        c = 0
        if i != ['']:
            c += 1
            print(c)
        if i == ['']:
            del(stationList[c])
    return stationList   
def get_stationline(mrt):
    pass

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