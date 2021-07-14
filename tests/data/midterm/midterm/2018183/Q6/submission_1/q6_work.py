import pickle

def read_stations(f):
    aline = f.readline()
    lst = list()
    dct = {}
    while aline:
        if aline == '=EastWestLine (EW)=\n':
            aline = f.readline()
            continue
        elif aline == '=EastWestLine (CG)=\n':
            dct['EastWestLine (EW)'] = lst
            lst = []
            aline = f.readline()
            continue
        elif aline == '=NorthSouthLine=\n':
            dct['=EastWestLine (CG)='] = lst
            lst = []
            aline = f.readline()
            continue
        elif aline == 'END':
            break
        else:
            x = aline.strip('\n')
            x = x.split(' ')
            lst.append(x)
            aline = f.readline()
    dct['NorthSouthLine'] = lst
    return dct

def get_stationline(mrt):
    lstEW = mrt.get('EastWestLine (EW)')
    lstCG = mrt.get('EastWestLine (CG)')
    lstNS = mrt.get('NorthSouthLine')
    dct = {}
    for i in lstEW:
        dct['i'] = 'EastWestLine (EW)'
    for i in lstCG:
        dct['i'] = 'EastWestLine (CG)'
    for i in lstNS:
        dct['i'] = 'EastWestLine (NS)'
        

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