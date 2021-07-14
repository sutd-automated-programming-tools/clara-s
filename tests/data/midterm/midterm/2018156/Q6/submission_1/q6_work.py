import pickle

def read_stations(f):
    dic = {}
    handle = f.read()
    difflines = handle.split('\n')
    
    for i,j in enumerate(difflines):
        if i%2==0:
            dic['j'] = j for i+1
            
    return dic

       
    
def get_stationline(mrt):
    newdic = {}
    for k,v in mrt.items():
        ls = []
        ls.append(k) 
        newdict[v] = ls
     
    return newdic
    
        
        

def get_interchange(stationline):
    newnewdic = {}
    for k,v in stationline.items():
        if len(v) > 1 :
            newnewdic[k] = v
    
    return newnewdic


  
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