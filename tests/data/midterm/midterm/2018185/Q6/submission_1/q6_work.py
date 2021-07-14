import pickle

def read_station(f):
    dic={}
    lst=[]
    for line in f.realines():
        a=line.strip()
        b=a.split()
        if len(b[0])==14:
            string=b[0]
        elif len(b[0])<14:
            lst.append(b[0])
            dic[string]=lst
    return dic
            

def get_stationline(mrt):
    dic={}
    lst=[]
    for i in mrt.keys():
        for stations in mrt[i]:
            lst.append(i)
            dic[stations]=lst
    return dic
            
d=read_station(f)
d1=get_stationline(d)

def get_interchange(stationline):
    dic={}
    lst=[]
    for i in stationline


  
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