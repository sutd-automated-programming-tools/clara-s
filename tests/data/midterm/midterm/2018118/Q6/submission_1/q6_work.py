import pickle

def read_stations(f):
    stations=[]
    output={}
    for line in f:
        if line == '=EastWestLine (EW)=':
            output[line]=0
            continue
        
        elif line == '=EastWestLine (CG)=':
            output['=EastWestLine (EW)=']=stations
            stations=[]
            continue
        
        elif line =='=NorthSouthLine=':
            output['=EastWestLine (CG)=']=stations
            stations=[]
            
        else:
            station=line.split(',')
            stations.append(station)
            
    output['=NorthSouthLine=']=stations
        
    return output

def get_stationline(mrt):
    stations=mrt.values()
    #combine all mrt station names
    combine=stations[0]+stations[1]+stations[2]
    output={}
    for i in stations:
        output[i]=mrt.get(i)
    
    return output

def get_interchange(stationline):
    output={}
    for key in stationline.keys():
        if len(key.value())>1:
            output[key]=key.value()
            
    return output
            
            
    


  
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