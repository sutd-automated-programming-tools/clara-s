import pickle

def read_stations(f):
    ls=[]
    dt={}
    ls1=[]
    for lines in f.readlines():
        ls.append(lines.strip().split(", ")) #Creates a list which gets rid of the leading spaces in front of stations
    for i in ls:
        if "Line" in i[0]:
            newKey = i[0].strip("==")
            dt[newKey]=[]
        elif i==[""]:
            pass
        else:
            dt[newKey]=i
    return dt

def get_stationline(mrt):
    dt={}
    ls=[]
    for value in mrt.values():
        for i in value:
            dt[i]=[]
    for new in dt.keys():
        for key,value in mrt.items():
            if new == value:
                ls=ls+key
        dt[new]=ls
    return dt

def get_interchange(stationline):
    dt={}
    dt1={}
    dt = stationline
    for key,val in dt.items():
        if len(val)!= 1:
            dt1[key]=val
    return dt1




  
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