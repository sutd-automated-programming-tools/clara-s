import pickle

def read_stations(f):
    dictionary={}
    while True:
        aList=[]
        cur_line=f.readline()
        if len(cur_line)==0:
            break
        ms = cur_line.strip()
        ls = ms.split(",")
        for i in range(len(ls)):
            if i==0:
                key=ls[i]
            else:
                aList.append(ls[i])
        dictionary[key]=aList
    return dictionary

def get_stationline(mrt):
    for i in dictionary:
        keys = dictionary.values()
        dic[keys] = 

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