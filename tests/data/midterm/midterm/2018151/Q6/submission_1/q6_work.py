import pickle

def read_stations(f):
    file = f.read()
    print (file)
    
    
    
    
    
    
def get_stationline(mrt):
    lines =[]
    for i in mrt:
        lines.append(i)
    dic = {}
    for i in mrt:
        stations = mrt[i]
        for j in stations:
            dic[j] = []
    
    
    for i in dic:
        for j in lines:
            if i in mrt[j]:
                dic[i].append(j)
    return (dic)
            
        


def get_interchange(stationline):
    


  
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

    x = read_stations(f)
    if start in x['EastWestLine (CG)']:
        if end in x['NorthSouthLine']:
            return (None)
    if end in x['EastWestLine (CG)']:
        if start in x['NorthSouthLine']:
            return (None)