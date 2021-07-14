import pickle

def read_stations(f):
    d = {}
    for line in f:
        formatted =line.strip()
        ls = line.split(',')
       
        if len(ls) <2 and "Line" in ls[0]:
            x = ls[0][1:-2]
            
            d[x] = []
        elif len(ls) > 2:
            for i in range(len(ls)):
                
                y= ls[i]
                if '\n' in y:
                    y =ls[i]
                d[x].append(ls[i])
                
        
          
            
         
    return d

def get_stationline(mrt):
    d={}
    for color in mrt:
        station_list = mrt[color]
        for stations in station_list:
            if stations not in d:
                d[stations] = [color]
            else:
                d[stations].append(color)
    return d    
    

def get_interchange(stationline):
    d={}
    for stations in stationline:
        x=stationline[stations]
        if len(x)>1:
            d[stations] = x
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
    with open('stations_short.pickle','rb') as f:
        mrt_d = pickle.load(f)
    with open('lines_short.pickle','rb') as f:
        lines = pickle.load(f)
    with open('interchange_short.pickle','rb') as f:
        interchange = pickle.load(f)'
        
    
    pass