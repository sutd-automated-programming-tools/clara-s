import pickle




def read_stations(f):
    x=[]
    a=[]
    d=dict()
    for i in f:
        i=i.strip()
        x=x+[i.split(",")]
    for i in x:
        if i!=[""]:
            a=a+[i]
    for i in range(len(a)):
        if len(a[i])==1:
            d[a[i][0][1:len(a[i][0])-1]]=a[i+1]
    return d

def get_stationline(mrt):
    d=dict()
    for i in mrt:
        for j in mrt[i]:
            if j not in d:
                d[j]=[i]
            else:
                d[j].append(i)
    return d

def get_interchange(stationline):
    d=dict()
    for i in stationline:
        if len(stationline[i])>1:
            d[i]=stationline[i]
    return d

def find_path(f,start,end):
    for i in f:
        if start in f[i] and end in f[i]:
            return f[i]

  
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