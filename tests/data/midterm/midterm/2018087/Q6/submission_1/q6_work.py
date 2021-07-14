import pickle

def read_stations(f):
    ls = []
    for line in read_stations:
        item = line.split()
        for i in range(len(item[i])):
            ls.append(item)        
    return ls


def get_stationline(mrt):
    ls = []
    for item in mrt:
       if j in in mrt[0]:#items are the mrtline j is station
           ls.append(item[j])#appending the list 
    return ls

def get_interchange(stationline):
    ls = []
    for line in stationline:
        item = line.split()
        for i in range(len(item[i])):
            ls.append(item)        
    return ls

def find_path(f,start,end):
#convert textfile to a list


  
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