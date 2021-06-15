import pickle

def read_stations(f):
    s = []
    lst = []
    d = {}
    for line in f:
        if line == '=EastWestLine (EW)=\n':
            continue
        elif line == '=EastWestLine (CG)=\n':
#            s.append('EastWestLine (EW)')           
            continue
        elif line == '=NorthSouthLine=\n':
#            s.append('EastWestLine (CG)')
            continue
        elif line == '=NorthSouthLine=\n':
            continue
        
        else:
            new = line.strip('\n').strip()
            new = new.split(', ')
            lst.append(new)

    lst = lst[::2]
    
    s = ['EastWestLine (EW)', 'EastWestLine (CG)', 'NorthSouthLine']
    
    d = dict(zip(s, lst))
    return d

def get_stationline(mrt):
        lst = []
    d = {}
    for c, v in mrt.items():

        for i in v:
            d[i] = c

            
    return d

def get_interchange(stationline):
    pass


  
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