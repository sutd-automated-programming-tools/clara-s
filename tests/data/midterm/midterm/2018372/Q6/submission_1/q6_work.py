import pickle

def read_stations(f):
    matrix = {}
    temp = []
    rline = f.readlines()
    #print(rline)
    for i in rline:
        stsp = i.strip().split(',')
        #print(stsp)
        temp.append(stsp)
        #print(temp)
    ew = temp.index(['=EastWestLine (EW)='])
    cg = temp.index(['=EastWestLine (CG)='])
    print(cg)
    nsl = temp.index(['=NorthSouthLine='])
    print(nsl)
    ew_ls = temp[ew+1:cg-1]
    #print(ew_ls)
    cg_ls = temp[cg+1:nsl-1]
    #print(cg_ls)
    nsl_ls = temp[nsl+1:]
    #print(nsl)
    matrix['EastWestLine (EW)'] = ew_ls[0]
    matrix['EastWest (CG)'] = cg_ls[0]
    matrix['NorthSouthLine'] = nsl_ls[0]
    return matrix

def get_stationline(mrt):
    dic = {}
    for k,v in mrt:
        if v in :
            ls.append(key)
    return ls

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