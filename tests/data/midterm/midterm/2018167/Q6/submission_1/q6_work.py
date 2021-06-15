import pickle

f = open("mrt_lines_short.txt", "r")

def read_stations(f):
    lines = f.readlines()
    result = {}
    for line in lines:
        line = line.strip().split("\n")[0].split(' ')
        if len(line) == 1:
            if line[0] == '=EastWestLine (EW)=':
                result.setdefault('station', [])
                cache = 'station'
                continue
                
            elif line[0] == "=EastWestLine (CG)=":
                result.setdefault('cg', [])
                cache = 'cg'
                continue
            elif line[0] == '=NorthSouthLine=':
                result.setdefault('NorthSouthLine', [])
                cache = 'NorthSouthLine'
                continue
        result[cache].append(line)
    return result


    
    
    
    
    
    
    
    
    

def get_stationline(mrt):
    result = {}
    for key, value in mrt.iteritems():
        values
#get the value out from the old dict and use as key in the new dict
# get the key from the dict and put as value in the new dict








def get_interchange(stationline):
    a={}
    for values in stationline:
        if len(values)>1：
            add key and value in the new dictionary a
            return a 
            
            
            #check if the value for each key in the dictionary if values>1 then the key is an interchange add to the new dictionary
    


  
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