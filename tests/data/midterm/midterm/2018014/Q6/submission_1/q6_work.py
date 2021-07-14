import pickle

#6a#
def read_stations(f):
    mrt = {}
    for line in f.readlines():
        a = line.split("=")
        #assign every odd index of a as key of dictionary d
        #use a.strip() to strip leading or trailing white spaces
        #assign every even index of a as value of keys in dictionary d
    return mrt

#6b#
def get_stationline(mrt):
    stationline = {}
    #access values of mrt which is a list and use each individual index as a key for a new dictionary
    for k, v in mrt:
        if k not in stationline:
            stationline[k] = []  #value of stationline[k] is an empty list
    #the values of stationline are lists that contain MRT lines as individual indexes that need to be added
    return stationline

#6c#
def get_interchange(stationline):
    d = {}
    #if the length of the value in stationline is >= 2, it is an interchange station (key)
    #keys of d are interchange stations
    #values of d are lists of MRT lines for that interchange station (key)
    return d


  
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