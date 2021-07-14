import pickle

def read_stations(f):
    l = f.readline()
    dic = {}
    while l:
        lis = []
        if 'EW' in l:
            lis.append("EastWestLine (EW)")
     
            stations = []
            stations.append(f.readline().split(", "))
            lis.append(stations)
            
            dic[lis[0]] = lis[1]
        
        elif 'CG' in l:
            lis.append("EastWestLine (CG)")
     
            stations = []
            stations.append(f.readline().split(", "))
            lis.append(stations)
            
            dic[lis[0]] = lis[1]
        
        else:
            lis.append("NorthSouthLine")
     
            stations = []
            stations.append(f.readline().split(", "))
            lis.append(stations)
            
            dic[lis[0]] = lis[1]
        
        f.readline()
    
    return dic
    
    
def get_stationline(mrt):
    stns = {}
    valuelist=list(mrt.values())
    keylist=list(mrt.keys())
    for i in range(len(valuelist)):
        for j in range(len(valuelist[i])): #iterate through every mrt station
            if valuelist[i][j] in stns: #check if mrt station is already a key in dictionary
                stns[valuelist[i][j]].append(keylist[i]) #if value already exist as list, append the list
            else:
                stns[valuelist[i][j]] = [keylist[i]] #create a new dictionary entry
    return stns

def get_interchange(stationline):
    lines = {}
    v = list(stationline.values()) #list of list of lines
    k = list(stationline.keys()) #list of station names
    for n in range(len(k)): #iterate through every mrt station
        for m in range(len(v[n])):
            if v[n][m] in lines:
                lines[v[n][m]].append(k[n])
            else:
                lines[v[n][m]].append(k[n])
    
    return lines


  
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