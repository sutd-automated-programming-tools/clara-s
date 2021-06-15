import pickle

def read_stations(f):
    pass

def get_stationline(mrt):
        
    stationairy = {}
    
    for i in mrt:
        
        for j in mrt[i]:
            
            if j in stationairy.keys():
                
                stationairy[j].append(i)
                
            else:
                stationairy[j] = [i]
            
    return stationairy      


def get_interchange(stationline):
     
    interchangenairy = {}
    
    for i in stationline:
        
        if len(stationline[i]) > 1:

            interchangenairy[i] = stationline[i]     
            
    return interchangenairy



  
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
    
        
    parta = read_stations(f)
    stationairy = get_stationline(parta)
    interchangenairy = get_interchange(stationairy)
    
    pathsame = []
    pathchange = []
    
    #whichline?
    
    startline = stationairy[start]
    finishline = stationairy[end]
    
    #sameline?
    
    if startline == finishline:
        
        count = 0
        
        while 
        
        parta[startline][start]
  