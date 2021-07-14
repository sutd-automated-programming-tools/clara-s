import pickle

def read_stations(f):
    ew = []
    ns = []
    cg = []
    
    a = f.readlines()
    first = a.pop(1).strip()
    station_ew = first.split(', ')
    ew=station_ew   
    
    second = a.pop(6).strip()
    station_ns = second.split(', ')
    ns = station_ns
    
    third = a.pop(3).strip()
    station_cg = third.split(', ')
    cg = station_cg
    
    dic = {'EastWestLine (CG)': cg, 'EastWestLine (EW)': ew, 'NorthSouthLine':ns}
    
    return (dic)
    
    
    

def get_stationline(mrt):
    mrt = dic
    ew = ['EastWestLine (EW)']*len()
    cg = ['EastWestLine (CG)']
    ns = ['NorthSouthLine']
    lis = []
    for station,line in mrt.items():
        for i in line:
            lis.append(i)
            
        total = dict(zip(lis,ew))
    print (total)

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