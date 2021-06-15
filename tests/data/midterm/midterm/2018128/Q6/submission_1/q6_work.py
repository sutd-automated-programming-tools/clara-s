import pickle

def read_stations(f):
    a = f.read()
    a = a.split('\n')
    output = {}

    EW_list = a[1]
    list_station_EW = ['']
    c = 0
    for i in EW_list:    
        if i == ',':
            list_station_EW.append('')
            c+=1    
        list_station_EW[c] += i
    output['=EastWestLine (EW)='] = list_station_EW    

    

        
    CG_list = a[4]
    list_station_CG = ['']
    c = 0
    for i in CG_list:    
        if i == ',':
            list_station_CG.append('')
            c+=1    
        list_station_CG[c] += i
    output['=EastWestLine (CG)='] = list_station_CG   


    NSL_list = a[7]

def get_stationline(mrt):
    output = {}
    for line in mrt:
        stations = mrt[line]
        for each_station in stations:
            output[each_station] = line
    return output

def get_interchange(stationline):
    output = {}
    for station in stationline:
        if len(stationline[station])> 1:
            output[station]= stationline[station]
    return output


  
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