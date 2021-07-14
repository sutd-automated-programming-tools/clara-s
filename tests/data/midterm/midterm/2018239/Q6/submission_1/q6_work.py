import pickle

def read_stations(f):
    a=[]
    c={}
    for line in f:
        line=line.strip()
        a.append(line)
    b=[]
    for i in range(len(a)):
        if bool(a[i])==True:
            station=a[i].strip("=")
            b.append(station)
    a=[]
    for i in b:
        d=i.split(',').strip()
        a.append(d)
    b=[]
    e=[]
    for i in a:
        if len(i)==1:
            stations=(str(i[0]))
            c.update({stations:b})
        if len(i)>1:
            c.update({stations:i})
    return c
    pass

def get_stationline(mrt):
    #make a list of all the stations that are in the values. if there is a repeat in the stations 
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