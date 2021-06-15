import pickle

def read_stations(f):
    
    mydict = {}
    for lines in f:
        x = lines.strip()
        x = x.split(",")
        alist = []
        for i in x:
            if len(x)==1 and i!='' :
                mydict[i] = 0
            
            elif len(x) >1:
                alist.append(i)
        mydict[i] = alist
        
    return mydict
                

def get_stationline(mrt):
    
    mydict = {}
    alist = []
    for i in mrt.keys():
        
        mydict[i] = 0
        
        
    

def get_interchange(stationline):
    newdict = {}
    if len(stationline.values()) >1:
        newdict[stationline.keys()] = stationline.values()
    return newdict
        


  
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