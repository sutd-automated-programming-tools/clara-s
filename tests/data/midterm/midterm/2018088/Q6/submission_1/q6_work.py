import pickle

def read_stations(f):
    pass
"""
        fin = open(f,'r')
        text = fin.read()
        print ("print fin\n")
        print(fin)
        print ("print txt\n")
        print (text)
        print ("split\n \n")
        splitted = text.split("=")
        print (splitted) 
        # split in line , (stations), line, (stations), line ,(stations)

        dic = {}
        i = 0
        for i in range(len(splitted)):
            key = splitted [i]
            dic[key] = splitted[i]
            i += 2   
            
        print (dic)
        return dic
"""    
def get_stationline(mrt):
    stationlines = {}
    for line in mrt:
        for station in mrt[line]:
            stationlines[station] = line
    return stationlines

def get_interchange(stationline):
    interchanges = {}
    for station in stationline:
        if len(stationline[station]) >= 2:
            if station not in stationline:
                interchanges[station] = stationline[station]
            else:
                pass
        else:
            pass
        
    return interchanges

  
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