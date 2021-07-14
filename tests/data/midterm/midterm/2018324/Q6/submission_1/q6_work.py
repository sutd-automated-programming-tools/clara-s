import pickle

def read_stations(f):
    dictans = {}
    EWdata = f.readlines()[1:2]
    EWlist = []
    for i in EWdata:
        EWlist.append(i)
    print(EWlist)
    
    NSlist = []
    f.seek(0)
    NSdata = f.readlines()[9:11]
    for i in NSdata:
        NSlist.append(i)
    print(NSlist)
    
    dictans['EastWestLine (EW)'] = EWlist
    dictans['NorthSouthLine'] = NSlist
    
    return dictans

def get_stationline(mrt):
    output = {}
    for i in mrt['EastWestLine(EW)']:
        if c in mrt['EastWestLine(EW)']:
            output[c] = ['EastWestLine(EW)']
        
        if c in mrt['EastWestLine(CG)']:
            output[c] = ['EastWestLine(CG)']
        
        if c in mrt['NorthSouthLine']:
            output[c] = ['NorthSouthLine']
    
    for i in mrt['EastWestLine(CG)']:
        if c in mrt['EastWestLine(EW)']:
            output[c] = ['EastWestLine(EW)']
        
        if c in mrt['EastWestLine(CG)']:
            output[c] = ['EastWestLine(CG)']
        
        if c in mrt['NorthSouthLine']:
            output[c] = ['NorthSouthLine']
    
    for i in mrt['NorthSouthLine']:
        if c in mrt['EastWestLine(EW)']:
            output[c] = ['EastWestLine(EW)']
        
        if c in mrt['EastWestLine(CG)']:
            output[c] = ['EastWestLine(CG)']
        
        if c in mrt['NorthSouthLine']:
            output[c] = ['NorthSouthLine']
    return output

def get_interchange(stationline):
    output = get_stationline(mrt)
    newoutput = {}
    for i in output[stationline]:
        if len(i) >= 2:
            newoutput[i] = stations


  
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