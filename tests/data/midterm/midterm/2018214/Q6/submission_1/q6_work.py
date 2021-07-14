import pickle

def read_stations(f):
    #with open('mrt_line_short.txt','r') as f
    for lines in f:
        lines = lines.strip()
        lines = lines.split(',')
        #print(lines)
  

def get_stationline(mrt):
    d = dict()
    for allstations in mrt.values():
        for station in allstations:
            print(station)
            if station not in d:
                a = []
                for i in mrt.keys():
                    a.append(i)
                d[station] = a
            else:
                a.append(mrt.keys())
    return d
                
                
    

def get_interchange(stationline):
    for i in stationline:
        if len(i) == 1:
            del stationline[i]
    return stationline
        


  
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
    start = get_stationline(start)
    end = get_stationline(start)
    if start == end:
        return read(