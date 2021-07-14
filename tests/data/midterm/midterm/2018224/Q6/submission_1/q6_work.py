import pickle

def read_stations(f):
    lst=[]
    d=dict()
    for line in f:
        values=line.split(',')
        if values==['=EastWestLine (EW)=\n']:
            values[0]='EastWestLine (EW)'
            d[values[0]]={}
        if values==['=EastWestLine (CG)=\n']:
            values[0]='EastWestLine (CG)'
            d[values[0]]={}
        if values==['=NorthSouthLine=\n']:
            values[0]='NorthSouthLine'
            d[values[0]]={}
        if 'EastWestLine (EW)' in d:
            d['EastWestLine (EW)']=values
        if 'EastWestLine (EW)' in d and 'EastWestLine (CG)' in d:
            d['EastWestLine (CG)']=values
        if 'EastWestLine (EW)' in d and 'EastWestLine (CG)' in d and 'NorthSouthLine' in d:
            d['NorthSouthLine']=values
        if values==['\n']:
            pass
    print (d)

def get_stationline(mrt):
    new=dict()
    for i in mrt:
        for a in mrt[i]:
            new[a]=mrt[i]
    print (new)

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