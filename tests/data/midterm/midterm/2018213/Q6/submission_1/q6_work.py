import pickle

f = open('mrt_lines_short.txt','r')

def read_stations(f):
    alllines = f.readlines()
    d ={}
    for line in alllines:
        eachline = line.strip().split(", ") #space is important
        key = eachline.pop(0)
        d[key] = eachline
    return d 

def get_stationline(mrt):
    newdict = {}
    lsofmrtlinein = []
    for mrtline in mrt:
        for eachstation in mrt[mrtline]:
            
            lsofmrtlinein = []
            lsofmrtlinein.append(mrtline[0])
            
            
            newdict[eachstation] = lsofmrtlinein
    return newdict 


def get_interchange(stationline):
    d = {}
    for key in stationline:
        if len(key)>1:
            d[key] = stationline[key]
    return d 
            


  
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
    
    #if start and end not in same line, return None
    with open('stations_short.pickle','rb') as f:
        mrt_d = pickle.load(f)
    with open('lines_short.pickle','rb') as f:
        lines = pickle.load(f)
    with open('interchange_short.pickle','rb') as f:
        interchange = pickle.load(f)
    pass