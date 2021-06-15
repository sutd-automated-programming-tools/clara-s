import pickle

def read_stations(f):
    a=f.readlines()
    ew=a[1].strip().split(',')
    output={}
    output['EastWestLine (EW)']=ew
    ns=a[7:9]
    ns=ns[0].split(',')
    output['NorthSouthLine']=ns
    ewcg=a[4].strip().split(',')
    output['EastWestLine(CG)']=ewcg
    return output
    
def get_stationline(mrt):
    a=read_stations(f)
    m=a[0]
    n=a[1]
    output={}
    for k in m.values():
        output[k]="['EastWestLine (EW)']"# same method for n
    return output
        
        
        

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