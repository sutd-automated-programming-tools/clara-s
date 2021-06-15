import pickle

def read_stations(f):
    data = f.readlines()
    current = ''
    ew = False
    cg = False
    ns = False
    ewlst = []
    nslst = []
    cglst = []
    for line in data:
        formatted = line.strip('\n').strip('=')
        if "EW" in formatted:
            ew = True
            cg = False
            ns = False
        elif "CG" in formatted:
            ew = False
            cg = True
            ns = False
        elif "North" in formatted:
            ew = False
            cg = False
            ns = False
        elif 'Line' not in formatted:
            if ew:
                ewlst = formatted.split(', ')
            elif cg:
                cglst = formatted.split(', ')
            elif ns:
                nslst = formatted.split(', ')
        dic = {'EasWestLine (EW)': ewlst, 'EastWestLine (CG)':cglst, 'NorthSouthLine':nslst}
        return dic
     

def get_stationline(mrt):
    stats = {}
    for k,v in mrt.items():
        stats[v] = [k]
    return stats
        

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