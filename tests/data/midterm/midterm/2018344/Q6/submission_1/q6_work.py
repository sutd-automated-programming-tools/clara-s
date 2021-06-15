import pickle

def read_stations(f):
    d = {}
    
    for i in f:
         
        if('=' in i):
            i = i[1:]
            j = i.strip('=\n')

            
        else:
            
            i = i.strip('=\n')
         
            l = (i.split(','))
            
            d[j] = l
            
    return d
            
            
#f = open('good.txt','r')
#print(read_stations(f))


def get_stationline(mrt):
    
    d = {}
    l = []
    for k,v in mrt.items():
        for i in mrt.values():
            if i in mrt[v] :
                l.append(k)
        
        d[v] = l
        
        
        


def get_interchange(stationline):
    d = {}
    for k,v in stationline.items():
        if len(v) > 1:
            d[k] = v
    return d



def find_path(f, start, end):
    mrt = read_stations(f)
    stationline = get_stationline(mrt)
    check_interchange = get_interchange(stationline)
    
    
        
        




  
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