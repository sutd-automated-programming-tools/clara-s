import pickle

def read_stations(f):
    file = f.splitlines()
    new = []
    for thing in file:
        if thing != ''
        new.append(thing)
    for i in new:
        i.strip()
    new2 = []
    for x in new1:
        new2.append(x.split())
    length = len(new2)
    dic =  {}
    for num in range(0, length, 2):
        dic[num] = new2[num + 1]
  
    return dic
   
        
        
        

def get_stationline(mrt):
    newkey = list(mrt.values())
    newval = list(mrt.keys())
    newdic = {}
    length1 = len (newval)
    
    
    for i in range (length):
        for j in range len(newkey[i]):
            dic[newkey[i][j] = newval[i]                
    
    return dic
        
    
      

def get_interchange(stationline):
    allkey = stationline.keys()
    outlist = []
    for key in allkey:
        outputlist.append(stationline[key]) 
    for output in outlist:
        if len(output)>1:
                
                    
          


  
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