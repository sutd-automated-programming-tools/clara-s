import pickle

def read_stations(f):
    stations={}
    s=f.readline()
    total=[]
    while s:
        
        if s[0]=="=":
            title=s.replace('=','')
            stations[title]=0
        else:
            stationlist=s.split[',']
            
        total+=stationlist
        s=f.readline()
        
    return (stations)
        
        
        
    
        

def get_stationline(mrt):
    stationline={}
    dict_keys=list(mrt.keys())
    dict_values=list(mrt.values())
    for i in dict_values:
        for j in i:
            if j not in stationline:
                stationline[j]=[]
            for k in dict_keys:
                if j in mrt[k]:
                    stationline[j].append(k)
                    
    return(stationline)
                
        
    

def get_interchange(stationline):
    interchange={}
    inter=[]
    for i in stationline:
        if len(stationline[i])>1:
            inter.append(i)
            
    for j in inter:
        if j not in interchange:
            interchange[j]=stationline[j]
            
    return (interchange)
            
    
    


  
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