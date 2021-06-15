import pickle

def read_stations(f):
    a=f.realdine()
    k={'=EastWestLine (EW)='=[],'=EastWestLine (CG)='=[],'=NorthSouthLine='=[]}
    while a:
        while a=='=EastWestLine (EW)=':
            a=f.readline()
            while a! = '=EastWestLine (CG)=':
                r=a.split().strip()
                k['=EastWestLine (EW)='][0]+=[r]
                a=f.readline()
        while a=='=EastWestLine (CG)=':
            a=f.readline()
            while a! = '=NorthSouthLine=':
                r=a.split().strip()
                k['=EastWestLine (CG)='][0]+=[r]
                a=f.readline()
        while a=='=NorthSouthLine=':
            a=f.readline()
            while a:
                r=a.split().strip()
                k['=NorthSouthLine='][0]+=r
                a=f.readline()
    return k
        

def get_stationline(mrt):
    k={}
    for i in mrt.values():
        for j in mrt.keys():
            if i in mrt[j]:
                if i not in k:
                    k[i]=j
                elif i in k:
                    k[i][0]+=j
    return k

def get_interchange(stationline):
    k={}
    for i in stationline.keys():
        if len(i)>1:
            k[i]=stationline[i]
    return k

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