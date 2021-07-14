import pickle

def read_stations(f):
    data={}
    
    for line in f:
        line=line.strip()
        line=line.strip("\n")
        
        line=line.split(",")
        #print(line)
        
        if "=" in line:
            data[line.strip("=")]=1 #adds a key with name of line, then strip "="

def get_stationline(mrt):
    newdict={}
    for k,v in mrt.items():
        for stn in v:
            if stn not in newdict:
                newdict[stn]=[k]
            else:
                newdict[stn].append(k) #add another station if it is an interchange
    return newdict

def get_interchange(stationline):
    newnewdict={}
    for k,v in stationline.items():
        if len(v)>1:
            
            


  
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