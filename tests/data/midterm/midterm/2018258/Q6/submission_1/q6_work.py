import pickle

def read_stations(f):
    pass

def get_stationline(mrt):
    lst = []
    for i in mrt:
        for k,v in i.items():
            lst.append(v) # add the values to the new list for the diff mrt names
            lst[v]=k #add the station name as values into the key of the diff mrt names
    return lst
            
        
            
      
def get_interchange(stationline):
    lst = []
    for i in stationline:
        for k,v in i.items(): #keys are station names as k and v is the value in it as lines
            if v not in lst: 
                lst.append(v) #add the station lines that are not inside lst to it
    return lst
        


  
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