import pickle

def read_stations(f):
   
    f = open('stations_short.pickle','r')
    content_f=f.readlines
    
    m = open('mrt_lines_short.txt','r')
    content_m=m.readlines
    
    return content_f, content_m
    
   
def get_stationline(mrt):
    
    lst = []
    for k,v in mrt.items():
        for i in v:
            lst.append([k])
            lst.append(i)
            
    d = dict(lst)
    
    return d

def get_interchange(stationline):
    
    lst = []
    for k,v in stationline.items():
        lst.append(k)
    
    
    
        


  
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