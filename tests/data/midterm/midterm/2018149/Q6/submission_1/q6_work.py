import pickle

def read_stations(f):
    mrt = ['EastWestLine (EW)', 'EastWestLine (CG)', 'NorthSouthLine']
    outdict = {}
    datalst = []
    
    for line in f:
        line = line.strip()
        row = line.strip('=')
        
        if row in mrt:            #1 if row is a day eg 'Monday' make it a key 
            datalst = []           #2 reset datalst if new key if found
            key = row              #3 making the keys must come after
            #print(key)
            
        else:                                      #if the row is not a day
            data = row.split(',')                  #split the numbers '9 11' and save as list
            for el in data:
                datalst.append(el)
                #print(datalst)
            
        outdict[key] = datalst     #rewrites each index with updated list until key is changed.
    return outdict

def get_stationline(mrt):
    outdict = {}
    #print(mrt.values())
    for line in mrt.keys():
        for stn in mrt.values():
            outdict[line] = stn
    print(outdict)            
    return outdict

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