import pickle

def read_stations(f):
    dict1={}
    for line in f:
        line=line.strip()
        if line:
            if line[0]=='=':
                current=line.replace('=','')
            
            elif not current in dict1:
                dict1[current]=[x.strip for x in line.split(',')]
                
            else:
                ls1=[x.strip for x in line.split(',')]
                for i in ls1:
                    dict1[current].append(i)
    return dict1
    




def get_stationline(mrt):
    dict1={}
    for line in mrt:
        for station in line:
            if station in dict1:
                dict1[station].append(line)
            else:
                dict1[station]=[line]
    return dict1

def get_interchange(stationline):
    dict1={}
    for line in stationline:
        if len(stationline[line])>1:
            dict1[line]=stationline[line]
    return dict1


  
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
    return None